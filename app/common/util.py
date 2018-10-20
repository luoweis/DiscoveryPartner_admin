#!/usr/bin/env python
# -*- coding=utf-8 -*-
from flask import jsonify
from app.common.code import Code
import json
import datetime
import hashlib
from app.common.project_life_cycle import project_lift_cycle

def return_result(data=None, code=Code.SUCCESS):
    """
    api接口返回消息格式
    :param data:
    :param code:
    :return:
    """
    return jsonify({
        "code": code,
        "data": data,
        "msg": Code.msg.get(code),
    })


def get_sex(num):
    """
    获取性别
    :param num:
    :return:
    """
    sex = '-'
    if num == 0:
        sex = "男"
    elif num == 1:
        sex = "女"
    return sex


def project_life_cycle_content(num):
    """
    根据status中的状态值返回状态内容
    :param num:
    :return:
    """

    return project_lift_cycle.get(str(num))

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


def do_encryption(word, t='md5'):
    """
    对内容进行加密操作，默认为md5加密的方式
    :param word:
    :param t:
    :return:
    """
    if isinstance(word, bytes):
        return hashlib.new(t, word).hexdigest()
    elif isinstance(word, str):
        return hashlib.new(t, word.encode(encoding="utf-8")).hexdigest()


