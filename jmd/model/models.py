#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongoengine import *


class User(Document):
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    validated = BooleanField(default=False)
    type = StringField(default='user')
    active = BooleanField(default=True)
