from __future__ import unicode_literals

from mopidy import config, ext

__version__ = '0.0.1'


class Extension(ext.Extension):

    dist_name = 'Mopidy-Podcast-gPodder'
    ext_name = 'podcast-gpodder'
    version = __version__

    def get_default_config(self):
        import os
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['base_url'] = config.String()
        schema['label'] = config.String()
        schema['timeout'] = config.Integer(optional=True)
        return schema

    def setup(self, registry):
        from .directory import gPodderDirectory
        registry.add('podcast:directory', gPodderDirectory)
