from __future__ import unicode_literals

import logging
import requests

from urllib2 import quote
from urlparse import urljoin, urldefrag

from mopidy_podcast.directory import PodcastDirectory
from mopidy_podcast.models import Ref

from . import Extension

_TAG_PATH = '/api/2/tag/{tag}/{count}.json'
_TAGS_PATH = '/api/2/tags/{count}.json'
_SEARCH_PATH = '/search.json'

logger = logging.getLogger(__name__)


class GPodderDirectory(PodcastDirectory):

    name = 'gpodder'

    def __init__(self, config):
        super(GPodderDirectory, self).__init__(config)
        self.root_name = config[Extension.ext_name]['name']
        self._count = config[Extension.ext_name]['count']
        self._timeout = config[Extension.ext_name]['timeout']
        self._session = requests.Session()

        base_url = config[Extension.ext_name]['base_url']
        self._tag_url = urljoin(base_url, _TAG_PATH)
        self._tags_url = urljoin(base_url, _TAGS_PATH)
        self._search_url = urljoin(base_url, _SEARCH_PATH)

    def browse(self, uri, limit=None):
        count = limit or self._count
        uri = uri.strip('/')
        if not uri:
            return self._get_tags(self._tags_url, count=count)
        else:
            return self._get_podcasts(self._tag_url, tag=uri, count=count)

    def search(self, uri, terms, attr=None, type=None, limit=None):
        if attr is not None or type == Ref.EPISODE:
            return None
        refs = self._get_podcasts(self._search_url, query=' '.join(terms))
        return refs[:limit]

    def _get_tags(self, url, **kwargs):
        refs = []
        for item in self._request(url, **kwargs):
            uri = quote(item['tag'].encode('utf-8'))
            refs.append(Ref.directory(uri=uri, name=item['tag']))
        return refs

    def _get_podcasts(self, url, **kwargs):
        refs = []
        for item in self._request(url, **kwargs):
            uri, _ = urldefrag(item['url'])  # remove excess fragment
            refs.append(Ref.podcast(uri=uri, name=item['title']))
        return refs

    def _request(self, url, query=None, **kwargs):
        response = self._session.get(url.format(**kwargs), params={
            'q': query
        }, timeout=self._timeout)
        logger.debug('Retrieving %s took %s', response.url, response.elapsed)
        response.raise_for_status()
        return response.json()
