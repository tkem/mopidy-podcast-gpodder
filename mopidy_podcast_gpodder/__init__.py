from __future__ import unicode_literals

from mopidy import config, ext

__version__ = '0.2.0'


class Extension(ext.Extension):

    dist_name = 'Mopidy-Podcast-GPodder'
    ext_name = 'podcast-gpodder'
    version = __version__

    def get_default_config(self):
        import os
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['display_name'] = config.String()
        schema['base_url'] = config.String()
        schema['tags'] = config.Integer(minimum=1)

        # config values no longer needed
        schema['top_tags_count'] = config.Deprecated()
        schema['podcasts_count'] = config.Deprecated()
        schema['timeout'] = config.Deprecated()
        return schema

    def setup(self, registry):
        from .directory import GPodderDirectory
        registry.add('podcast:directory', GPodderDirectory)
