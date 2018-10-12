#!/usr/bin/env python
# -*- coding=utf-8 -*-
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

'''优化前端返回中文数据进行正常显示,用于flask restful api接口开发使用'''
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
app.config['JSON_AS_ASCII'] = False
app.secret_key = os.urandom(32)

login_manager = LoginManager()
# 指定未登录时跳转的页面，即被拦截后跳转到我们定义的authBP/login的路由中
login_manager.login_view = "authBP.login"
login_manager.login_message = '请登录以访问此页面'
login_manager.init_app(app)

# 数据库的相关信息
"""
username: 用户名
pwd: 密码
addr: 地址
port：端口号
dbname：数据库的名称
"""

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:luoweis123456@127.0.0.1:13306/DiscoveryPartnerAdmin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = False
db = SQLAlchemy(app, use_native_unicode='utf8')


from app.views import auth,  main
# 注册蓝本模块
# 验证登陆的模块
from app.bpurls import authBP
app.register_blueprint(authBP)
# 接口模块
# from app.bpurls import apisBP
# app.register_blueprint(apisBP)
# 首页模块
from app.bpurls import mainBP
app.register_blueprint(mainBP)


# 初始化数据库创建表
def db_init():
    db.create_all()


# drop all tables
def db_drop():
    db.drop_all()
