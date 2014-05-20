from __future__ import unicode_literals

from mopidy import config, ext

__version__ = '0.3.0'


class Extension(ext.Extension):

    dist_name = 'Mopidy-Podcast-GPodder'
    ext_name = 'podcast-gpodder'
    version = __version__

    def get_default_config(self):
        import os
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = self.config_schema(super(Extension, self).get_config_schema())
        schema['tags'] = config.Deprecated()
        schema['top_tags_count'] = config.Deprecated()
        schema['podcasts_count'] = config.Deprecated()
        return schema

    def setup(self, registry):
        from .directory import GPodderDirectory
        registry.add('podcast:directory', GPodderDirectory)

    @classmethod
    def config_schema(cls, schema=config.ConfigSchema('podcast-gpodder')):
        schema['base_url'] = config.String()
        schema['root_name'] = config.String()
        schema['tag_name'] = config.String()
        schema['podcast_name'] = config.String()
        schema['count'] = config.Integer(minimum=1)
        schema['timeout'] = config.Integer(optional=True, minimum=1)
        return schema
