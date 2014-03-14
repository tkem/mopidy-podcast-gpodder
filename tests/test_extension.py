from __future__ import unicode_literals

import unittest

from mopidy_podcast_gpodder import Extension


class ExtensionTest(unittest.TestCase):

    def test_get_default_config(self):
        ext = Extension()
        config = ext.get_default_config()
        self.assertIn('[podcast-gpodder]', config)
        self.assertIn('enabled = true', config)

    def test_get_config_schema(self):
        ext = Extension()
        schema = ext.get_config_schema()
        self.assertIn('display_name', schema)
        self.assertIn('base_url', schema)
        self.assertIn('top_tags_count', schema)
        self.assertIn('podcasts_count', schema)
        self.assertIn('timeout', schema)
