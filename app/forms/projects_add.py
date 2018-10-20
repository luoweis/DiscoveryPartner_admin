# -*- coding=utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired


"""
添加项目信息的form表单
"""


class ProjectAddForm(FlaskForm):
    """表单的域初始化时，第一个参数设置lable属性"""
    project_name = StringField(label='project_name', validators=[DataRequired()],)
    project_ID = StringField('project_ID', validators=[DataRequired()])
    project_info = TextAreaField('project_info',)
    project_status = SelectField(
        label="project_status",
        validators=[DataRequired()],
        choices=[
            ("0", "立项阶段"),
            ("1", "项目启动"),
            ("2", "持续开发阶段"),
            ("3", "产品交付"),
        ]
    )
    project_client = StringField('project_client', validators=[DataRequired()])
    project_members = StringField('project_members',)

