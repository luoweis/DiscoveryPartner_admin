# -*- coding=utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


"""
添加学生的form表单
"""


class ProjectAddForm(FlaskForm):
    """表单的域初始化时，第一个参数设置lable属性"""
    project_name = StringField(label='project_name', validators=[DataRequired()],)
    project_ID = StringField('project_ID', validators=[DataRequired()])
    project_info = TextAreaField('project_info',)