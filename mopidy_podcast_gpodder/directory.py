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


class GPodderDirectory(PodcastDirectory):

    name = 'gpodder'

    def __init__(self, backend):
        super(GPodderDirectory, self).__init__(backend)
        self.label = self.config['display_name']
        self.tag_url = urljoin(self.config['base_url'], TAG_PATH)
        self.tags_url = urljoin(self.config['base_url'], TAGS_PATH)
        self.search_url = urljoin(self.config['base_url'], SEARCH_PATH)
        self.session = requests.Session()

    @property
    def config(self):
        return self.backend.config['podcast-gpodder']

    def browse(self, uri):
        if not uri or uri == '/':
            count = self.config['top_tags_count']
            return self._get_tags(self.tags_url, count=count)
        elif uri.startswith('/'):
            tag = uri.strip('/')
            count = self.config['podcasts_count']
            return self._get_podcasts(self.tag_url, tag=tag, count=count)
        else:
            return super(GPodderDirectory, self).browse(uri)

    def search(self, terms=None, attribute=None, limit=None):
        if not terms or attribute:
            return []
        refs = self._get_podcasts(self.search_url, query='+'.join(terms))
        return refs[:limit]

    def _get_tags(self, url, **kwargs):
        refs = []
        for item in self._request(url, **kwargs):
            refs.append(Ref.directory(uri=item['tag'], name=item['tag']))
        return refs

    def _get_podcasts(self, url, **kwargs):
        refs = []
        for item in self._request(url, **kwargs):
            refs.append(Ref.podcast(uri=item['url'], name=item['title']))
        return refs

    def _request(self, url, query=None, **kwargs):
        response = self.session.get(url.format(**kwargs), params={
            'q': query
        }, timeout=self.config['timeout'])
        logger.debug('Retrieving %s took %s', response.url, response.elapsed)
        response.raise_for_status()
        return response.json()
