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
        for name in Extension.config_schema().keys():
            setattr(self, name, config[Extension.ext_name][name])
        self._tag_url = urljoin(self.base_url, _TAG_PATH)
        self._tags_url = urljoin(self.base_url, _TAGS_PATH)
        self._search_url = urljoin(self.base_url, _SEARCH_PATH)
        self._session = requests.Session()

    def browse(self, uri, limit=None):
        uri = uri.strip('/')
        count = limit or self.count
        if not uri:
            return self._tags(self._tags_url, count=count)
        else:
            return self._podcasts(self._tag_url, tag=uri, count=count)

    def search(self, uri, terms, attr=None, type=None, limit=None):
        if uri and uri != '/':
            return None  # no tag-related searches in gpodder.net
        if attr is not None or type == Ref.EPISODE:
            return None  # no attribute or episode searches in gpodder.net
        return self._podcasts(self._search_url, query=terms, limit=limit)

    def _tags(self, url, **kwargs):
        refs = []
        for item in self._request(url, **kwargs):
            uri = quote(item['tag'].encode('utf-8'))
            name = self.tag_name.format(**item)
            refs.append(Ref.directory(uri=uri, name=name))
        return refs

    def _podcasts(self, url, **kwargs):
        refs = []
        for item in self._request(url, **kwargs):
            uri, _ = urldefrag(item['url'])  # remove excess fragment
            name = self.podcast_name.format(**item)
            refs.append(Ref.podcast(uri=uri, name=name))
        return refs

    def _request(self, url, query=None, limit=None, **kwargs):
        response = self._session.get(
            url.format(**kwargs),
            params={'q': query},
            timeout=self.timeout
        )
        logger.debug('Retrieving %s took %s', response.url, response.elapsed)
        response.raise_for_status()
        return response.json()[:limit]
