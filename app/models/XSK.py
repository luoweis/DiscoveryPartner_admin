#!/usr/bin/env python
# -*- coding=utf-8 -*-

from flask import current_app
from app import db


class XSKStudent(db.Model):
    # define table name
    __tablename__ = 'xsk_students'
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('xsk_class.id'), nullable=True, unique=True)
    student_name = db.Column(db.String(32), unique=False, nullable=False, index=True)
    student_age = db.Column(db.SmallInteger, nullable=False, doc="学生年龄")
    student_sex = db.Column(db.SmallInteger, nullable=False, default=1, doc="性别，0-男性，1-女性")
    student_phone = db.Column(db.String(32), nullable=True, unique=True)
    student_ID = db.Column(db.String(32), nullable=True, unique=True)
    student_info = db.Column(db.String(100), nullable=True)
    status = db.Column(db.SmallInteger, nullable=False, default=1, doc="学生状态，0-禁用，1-启动")
    student_image = db.Column(db.String(100), nullable=True)
    create_datetime = db.Column(db.DateTime, server_default=db.text("CURRENT_TIMESTAMP"), doc="创建时间")
    update_datetime = db.Column(db.DateTime, nullable=False,server_default=db.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), doc="更新时间")

    def __init__(self, **kwargs):
        super(XSKStudent, self).__init__(**kwargs)

    def __repr__(self):
        return "Student<name:%r>" % self.student_name


class XSKTeacher(db.Model):
    # define table name
    __tablename__ = 'xsk_teachers'
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('xsk_class.id'), nullable=True,unique=True)
    teacher_name = db.Column(db.String(32), unique=False, nullable=False, index=True)
    teacher_age = db.Column(db.SmallInteger, nullable=False, doc="年龄")
    teacher_phone = db.Column(db.String(32), nullable=True, unique=True)
    teacher_ID = db.Column(db.String(32), nullable=True, unique=True)
    teacher_sex = db.Column(db.SmallInteger, nullable=False, default=1, doc="教师性别，0-男性，1-女性")
    teacher_info = db.Column(db.String(100), nullable=True)
    status = db.Column(db.SmallInteger, nullable=False, default=1, doc="教师状态，0-禁用，1-启动")
    teacher_image = db.Column(db.String(100), nullable=True)
    create_datetime = db.Column(db.DateTime, server_default=db.text("CURRENT_TIMESTAMP"), doc="创建时间")
    update_datetime = db.Column(db.DateTime, nullable=False,server_default=db.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), doc="更新时间")

    def __init__(self, **kwargs):
        super(XSKTeacher, self).__init__(**kwargs)

    def __repr__(self):
        return "Teacher<name:%r>" % self.teacher_name


class XSKClass(db.Model):
    # define table name
    __tablename__ = 'xsk_class'
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(32), unique=False, nullable=False, index=True)
    class_info = db.Column(db.String(100), nullable=True)
    class_period = db.Column(db.String(32), nullable=True)
    class_start = db.Column(db.String(32), nullable=True)
    status = db.Column(db.SmallInteger, nullable=False, default=1, doc="课程状态，0-禁用，1-启动")
    class_image = db.Column(db.String(100), nullable=True)
    create_datetime = db.Column(db.DateTime, server_default=db.text("CURRENT_TIMESTAMP"), doc="创建时间")
    update_datetime = db.Column(db.DateTime, nullable=False,server_default=db.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), doc="更新时间")

    def __init__(self, **kwargs):
        super(XSKClass, self).__init__(**kwargs)

    def __repr__(self):
        return "Class<name:%r>" % self.class_name

