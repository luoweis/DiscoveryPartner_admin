#!/usr/bin/env python
# -*- coding=utf-8 -*-
from app.models.XSK import *
from app.models.Users import *
from app import db
import json


def get_students_limit(num=10):
    """
    定义获取学生表信息的数量
    :param num:
    :return:
    """
    students_10 = XSKStudent.query.limit(num)
    return students_10


def get_students_all():
    """
    获取所有的名单
    :return:
    """
    students = XSKStudent.query.all()
    return students


def get_students_onepage(pageSize, offset):
    """
    获取单页数量的名单
    :param pageSize:
    :param offset:
    :return:
    """
    res = XSKStudent.query.limit(pageSize).offset(offset).all()
    return res


def get_students_total():
    """
    获取总数
    :return:
    """
    total = XSKStudent.query.count()
    return total


def add_student_single(**kwargs):
    """
    一次只增加一个学生的信息，写入数据库中
    :param kwargs:
    :return:
    """
    """判断添加的元素是否存在"""
    waring = ""
    if XSKStudent.query.filter_by(student_ID=kwargs.get("student_ID")).all():
        return {"msg": "该学生已经注册了信息"}
    try:
        student1 = XSKStudent(**kwargs)
        db.session.add(student1)
        db.session.commit()
    except Exception as error:
        return {"error_msg": error}
    else:
        return {"msg": "添加成功"}


def add_student_multiple(ps):
    """
    批量插入数据
    :param args:
    :return:
    """
    students = []

    try:
        for p in ps:
            xsk_student = XSKStudent(**p)
            students.append(xsk_student)
        db.session.add_all(students)
        db.session.commit()
    except Exception as error:
        return {"error": error}
    else:
        return {"msg": "批量添加成功"}


