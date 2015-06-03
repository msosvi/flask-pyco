# -*- coding: utf-8 -*-
import slugify as sl


def slugify(url, delim='-/_'):
    return sl.slugify(url,delim)
