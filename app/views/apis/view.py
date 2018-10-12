#!/usr/bin/env python
# -*- coding=utf-8 -*-

from flask_restful import Resource, request
from app.common.util import return_result
from app.views.apis.parser import *
import pprint
from app.views.apis.utils import *
import os

class WebhookXSK(Resource):
    """
    wehbook 针对XSK的gitee项目
    """
    def post(self):
        args = webhook_parser.parse_args()
        webhook_password = args.get("password")
        if webhook_password != "P@ssword123456":
            data = {"error": "密码错误"}
        else:
            # 可以提取wehbook反推给我们的json数据
            res = request.json
            data = get_data_from_webhook_json(res)
            branch = data.get("branch")
            ret_value = os.system(f"bash renewCode.sh {branch} &")
        return return_result(data=data)


class WebhookDevopsAdmin01(Resource):
    """
    webhook 针对DevopsAdmins_01 gitee 项目
    """
    def post(self):
        args = webhook_parser.parse_args()
        webhook_password = args.get("password")

        if webhook_password != "P@ssword123456":
            data = {"error": "密码有误"}
        else:
            res = request.json
            data = get_data_from_webhook_json(res)
            # 自动运行代码更新的脚本
            ret_value = os.system("bash renewCode.sh &")
            data["comm_value"] = ret_value
        return return_result(data=data)