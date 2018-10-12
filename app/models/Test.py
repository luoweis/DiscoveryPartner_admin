#!/usr/bin/env python
# -*- coding=utf-8 -*-

from flask import current_app
from app import db


class Test(db.Model):
    # define table name
    __tablename__ = 't_test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    info = db.Column(db.String(32), nullable=False)
    status = db.Column(db.SmallInteger, nullable=False, default=1, doc="用户状态，0-禁用，1-启动")
    create_datetime = db.Column(db.DateTime, server_default=db.text("CURRENT_TIMESTAMP"), doc="创建时间")
    update_datetime = db.Column(db.DateTime, nullable=False,server_default=db.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), doc="更新时间")

    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)

    def __repr__(self):
        return "User<name:%r>" % self.name
