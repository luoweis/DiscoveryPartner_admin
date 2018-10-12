# -*- coding=utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

"""
定义登录页面的表单
"""


class LoginForm(FlaskForm):
    """表单的域初始化时，第一个参数设置lable属性"""
    username = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('RememberMe', default=False)
