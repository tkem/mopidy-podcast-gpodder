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

    def __init__(self, config, timeout):
        super(GPodderDirectory, self).__init__(config, timeout)
        self.config = config[Extension.ext_name]
        self.display_name = self.config['display_name']
        self.timeout = timeout

        base_url = self.config['base_url']
        self._tag_url = urljoin(base_url, _TAG_PATH)
        self._tags_url = urljoin(base_url, _TAGS_PATH)
        self._search_url = urljoin(base_url, _SEARCH_PATH)
        self._session = requests.Session()

    def browse(self, uri, limit=None):
        if not uri or uri == '/':
            return self._get_tags(self._tags_url, count=self.config['tags'])
        elif uri.startswith('/'):
            tag = uri.strip('/')
            count = limit or self.config['tags']
            return self._get_podcasts(self._tag_url, tag=tag, count=count)
        else:
            return super(GPodderDirectory, self).browse(uri)

    def search(self, terms=None, attribute=None, type=None, limit=None):
        if not terms or attribute or type == Ref.EPISODE:
            return None
        refs = self._get_podcasts(self.search_url, query=' '.join(terms))
        return refs[:limit]

    def _get_tags(self, url, **kwargs):
        refs = []
        for item in self._request(url, **kwargs):
            uri = '/' + quote(item['tag'].encode('utf-8'))
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
        }, timeout=self.timeout)
        logger.debug('Retrieving %s took %s', response.url, response.elapsed)
        response.raise_for_status()
        return response.json()
