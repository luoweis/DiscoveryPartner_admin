#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask_restful import Api
from .views.apis.view import *
import os

# 登陆的蓝本
authBP = Blueprint(
    'authBP', __name__, url_prefix='/auth',
    template_folder=os.path.join(os.path.dirname(__file__), "templates/auth"))

# 首页内容的蓝本
mainBP = Blueprint(
    'mainBP', __name__, url_prefix='/',
    template_folder=os.path.join(os.path.dirname(__file__), "templates/main"))

# projects 内容蓝本
projectsBP = Blueprint(
    "projectsBP", __name__, url_prefix="/projects",
    template_folder=os.path.join(os.path.dirname(__file__), "templates/projectManagement")
)
# # 教学资源内容的蓝本
# teachingBP = Blueprint(
#     'teachingBP', __name__, url_prefix='/resources/',
#     template_folder=os.path.join(os.path.dirname(__file__), "templates/teachingResources"))
#
# # 接口的模版
# apisBP = Blueprint(
#     'apisBP', __name__, url_prefix="/apis",
# )

# # 注册接口的路由
# resource = Api(apisBP)
#
# resource.add_resource(WebhookXSK, "/webhook/xsk/v1.0/")
# resource.add_resource(WebhookDevopsAdmin01, "/webhook/devopsAdmin01/v1.0/")

