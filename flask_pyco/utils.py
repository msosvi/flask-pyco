# -*- coding: utf-8 -*-
import re
from unicodedata import normalize

##_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
_punct_re = re.compile(r'[\t !"#$%&\'()*\-<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug."""
    
    text = unicode(text.lower())
    text = normalize('NFKD', text).encode('ascii', 'ignore')

    words = filter(None,_punct_re.split(text))
    return unicode(delim.join(words))


  
