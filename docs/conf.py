#!/usr/bin/env python3
# -*- coding: utf-8 -*-

source_suffix = '.md'

# The master toctree document.
master_doc = 'index'

extensions = [
    'recommonmark',
]

from recommonmark.transform import AutoStructify

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.

# app setup hook
def setup(app):
    app.add_config_value('recommonmark_config', {
        'enable_eval_rst': True
    }, True)
    app.add_transform(AutoStructify)
