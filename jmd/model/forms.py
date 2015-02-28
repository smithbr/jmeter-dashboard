#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms.validators import Required, Email
from wtforms import TextField, PasswordField


class SignupForm(Form):
    email = TextField('Email', validators=[Required(), Email()])
    passwd = PasswordField('Password', validators=[Required()])
    passwd_verify = PasswordField('Verify Password', validators=[Required()])
