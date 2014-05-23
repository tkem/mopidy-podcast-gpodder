from __future__ import unicode_literals

import logging
import requests
import string
import urllib2
import urlparse

from mopidy_podcast.directory import PodcastDirectory
from mopidy_podcast.models import Ref

from . import Extension

_TAG_PATH = '/api/2/tag/{tag}/{count}.json'
_TAGS_PATH = '/api/2/tags/{count}.json'
_SEARCH_PATH = '/search.json'

logger = logging.getLogger(__name__)


class Formatter(string.Formatter):

    def get_value(self, key, args, kwargs):
        try:
            return super(Formatter, self).get_value(key, args, kwargs)
        except KeyError:
            return None


formatter = Formatter()


class GPodderDirectory(PodcastDirectory):

    name = 'gpodder'

    def __init__(self, config):
        super(GPodderDirectory, self).__init__(config)
        self._config = config[Extension.ext_name]
        self._session = requests.Session()

        base_url = self._config['base_url']
        self._tag_url = urlparse.urljoin(base_url, _TAG_PATH)
        self._tags_url = urlparse.urljoin(base_url, _TAGS_PATH)
        self._search_url = urlparse.urljoin(base_url, _SEARCH_PATH)

        self.root_name = self._config['root_name']  # for browsing

    def browse(self, uri, limit=None):
        if not uri or uri == '/':
            return self._tags(self._tags_url, limit)
        else:
            return self._podcasts(self._tag_url, limit, tag=uri.strip('/'))

    def search(self, uri, terms, attr=None, type=None, limit=None):
        if uri and uri != '/':
            return None  # no tag-related searches in gpodder.net
        if attr is not None:
            return None  # no attribute searches in gpodder.net
        if type not in (None, Ref.PODCAST):
            return None  # no searching for episodes in gpodder.net
        return self._podcasts(self._search_url, query=terms, limit=limit)

    def _tags(self, url, limit=None, **kwargs):
        refs = []
        count = limit or self._config['count']
        format = self._config['tag_format']
        for item in self._request(url, limit=limit, count=count, **kwargs):
            uri = urllib2.quote(item['tag'].encode('utf-8'))
            name = formatter.vformat(format, [], item)
            refs.append(Ref.directory(uri=uri, name=name))
        return refs

    def _podcasts(self, url, limit=None, **kwargs):
        refs = []
        count = limit or self._config['count']
        format = self._config['podcast_format']
        for item in self._request(url, limit=limit, count=count, **kwargs):
            uri, _ = urlparse.urldefrag(item['url'])
            name = formatter.vformat(format, [], item)
            refs.append(Ref.podcast(uri=uri, name=name))
        return refs

    def _request(self, url, query=None, limit=None, **kwargs):
        response = self._session.get(
            url.format(**kwargs),
            params={'q': query},
            timeout=self._config['timeout']
        )
        response.raise_for_status()
        logger.debug('Retrieving %s took %s', response.url, response.elapsed)
        return response.json()[:limit]
