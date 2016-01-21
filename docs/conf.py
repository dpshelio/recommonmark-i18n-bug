#!/usr/bin/env python3
# -*- coding: utf-8 -*-

source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

source_parsers = {
    '.md': CommonMarkParser,
    }


locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.

# app setup hook
def setup(app):
    app.add_transform(AutoStructify)
