#!/usr/bin/env python
# -*- coding=utf-8 -*-

from flask_restful.reqparse import RequestParser

parser = RequestParser()

'''
默认参数类型为str
允许传入的是空值，None
通过required=True,不允许为空值
'''
parser.add_argument(
        "id",
        type=int,
        required=True,
        # action="append",# 允许传入多个值，最终是一个列表形式
        help="传入的值不能为空，只接收数值类型的数据"
    )


webhook_parser = RequestParser()

webhook_parser.add_argument(
        "password",
        type=str,
        required=True,
        # action="append",# 允许传入多个值，最终是一个列表形式
        help="密码不能为空"
    )