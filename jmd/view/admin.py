#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.admin.contrib.mongoengine import ModelView

from jmd import admin
from jmd.model.models import User


class UserView(ModelView):
    pass


admin.add_view(UserView(User))
