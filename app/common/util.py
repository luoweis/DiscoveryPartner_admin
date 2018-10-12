#!/usr/bin/env python
# -*- coding=utf-8 -*-
from flask import jsonify
from app.common.code import Code
import json
import datetime


def return_result(data=None, code=Code.SUCCESS):
    return jsonify({
        "code": code,
        "data": data,
        "msg": Code.msg.get(code),
    })


def get_sex(num):
    sex = '-'
    if num == 0:
        sex = "男"
    elif num == 1:
        sex = "女"
    return sex


# 重写json类，遇到日期特殊处理
# 解决json 日期格式报错"not JSON serializable"
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
