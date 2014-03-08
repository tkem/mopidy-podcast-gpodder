from __future__ import unicode_literals

import logging
import requests

from urlparse import urljoin

from mopidy_podcast.directory import PodcastDirectory
#from mopidy_podcast.models import Ref

SEARCH_PATH = '/search'

logger = logging.getLogger(__name__)


class gPodderDirectory(PodcastDirectory):

    name = 'gpodder'

    genre = None

    def __init__(self, backend):
        super(gPodderDirectory, self).__init__(backend)
        self.label = self.config['label']
        self.session = requests.Session()
        self.search_url = urljoin(self.config['base_url'], SEARCH_PATH)

    @property
    def config(self):
        return self.backend.config['podcast-gpodder']

    def browse(self, path):
        return []

    def search(self, terms=None, attribute=None):
        if not terms:
            return []
        return []

    def request(self, url, params=None):
        timeout = self.config['timeout']
        response = self.session.get(url, params=params, timeout=timeout)
        return response.json()
