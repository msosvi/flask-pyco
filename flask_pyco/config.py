# -*- coding: utf-8 -*-

import yaml

class ConfigAttribute(object):
    """Makes an attribute forward to the config"""

    def __init__(self, name, get_converter=None):
        self.__name__ = name
        self.get_converter = get_converter

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        rv = obj[self.__name__]
        if self.get_converter is not None:
            rv = self.get_converter(rv)
        return rv

    def __set__(self, obj, value):
        obj[self.__name__] = value


class Config(dict):

    # Default configuration parameters.
    defaults = {
            'development': False,
            'markdown_ext': '.md',
            'html_ext': '.html',
            'order_pages_by': 'date',
            'reverse_order': False,
            'date_format' : '%d/%m/%Y',
            'theme' : 'default',
            'contentdir': 'content'
            }

    markdown_ext = ConfigAttribute('markdown_ext')
    html_ext = ConfigAttribute('html_ext')
    development = ConfigAttribute('development')
    theme = ConfigAttribute('theme')
    contentdir = ConfigAttribute('contentdir')
    reverse_order = ConfigAttribute('reverse_order')

    def __init__(self):
        dict.__init__(self,self.defaults)


    def from_ymal(self,filename):
        try:
            with open(filename,'r') as config_file:
                self.update (yaml.load(config_file.read()))

        except IOError as e:
            e.strerror = 'Unable to load configuration file (%s)' % e.strerror
            raise

    def dump(self):
        return yaml.dump(self)

