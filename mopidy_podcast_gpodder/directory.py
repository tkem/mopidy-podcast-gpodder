from __future__ import unicode_literals

import logging
import requests

from urlparse import urljoin

from mopidy_podcast.directory import PodcastDirectory
from mopidy_podcast.models import Ref

TAG_PATH = '/api/2/tag/{tag}/{count}.json'
TAGS_PATH = '/api/2/tags/{count}.json'
SEARCH_PATH = '/search.json'

logger = logging.getLogger(__name__)


def _to_directory_refs(results):
    refs = []
    for result in results:
        try:
            refs.append(Ref.directory(uri=result['tag'], name=result['tag']))
        except Exception as e:
            logger.error('gPodder format error: %r %r', e, result)
    return refs


def _to_podcast_refs(results):
    # TODO: try to filter duplicates
    refs = []
    for result in results:
        try:
            refs.append(Ref.podcast(uri=result['url'], name=result['title']))
        except Exception as e:
            logger.error('gPodder format error: %r %r', e, result)
    return refs


class gPodderDirectory(PodcastDirectory):

    name = 'gpodder'

    genre = None

    def __init__(self, backend):
        super(gPodderDirectory, self).__init__(backend)
        self.label = self.config['label']
        self.session = requests.Session()
        self.tag_url = urljoin(self.config['base_url'], TAG_PATH)
        self.tags_url = urljoin(self.config['base_url'], TAGS_PATH)
        self.search_url = urljoin(self.config['base_url'], SEARCH_PATH)

    @property
    def config(self):
        return self.backend.config['podcast-gpodder']

    def browse(self, tag):
        tag = tag.strip('/')
        if not tag:
            results = self.request(self.tags_url, count=10)
            return _to_directory_refs(results)
        else:
            results = self.request(self.tag_url, tag=tag, count=10)
            return _to_podcast_refs(results)

    def search(self, terms=None, attribute=None):
        if not terms:
            return []
        results = self.request(self.search_url, params={
            'q': '+'.join(terms)
        })
        return _to_podcast_refs(results)

    def request(self, url, params=None, **kwargs):
        url = url.format(**kwargs)
        timeout = self.config['timeout']
        response = self.session.get(url, params=params, timeout=timeout)
        return response.json()
