# -*- coding=utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


"""
添加学生的form表单
"""


class StudentAddForm(FlaskForm):
    """表单的域初始化时，第一个参数设置lable属性"""
    student_name = StringField('student_name', validators=[DataRequired()])
    student_sex = StringField('student_sex', validators=[DataRequired()])
    student_age = StringField('student_age', validators=[DataRequired()])
    student_phone = StringField('student_phone', validators=[DataRequired()])
    student_ID = StringField('student_ID', validators=[DataRequired()])
    student_info = TextAreaField('student_info',)
