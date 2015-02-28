#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

SECRET_KEY = os.urandom(32)

# This is obvious, isn't it?
MONGODB_SETTINGS = {
    'db': 'jmd',
    'host': 'localhost:27017'
}

# Login Settings
LOGIN_VIEW = "login"

# Debug Toolbar
DEBUG_TB_PROFILER_ENABLED = True
