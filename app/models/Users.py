#!/usr/bin/env python
# -*- coding=utf-8 -*-

from flask import current_app
from app import db
from flask_login import UserMixin


class DiscoveryPartnerUsers(db.Model, UserMixin):
    # define table name
    __tablename__ = 'discovery_partner'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), nullable=True, default="XSK")
    userPhone = db.Column(db.String(20), nullable=True)
    status = db.Column(db.SmallInteger, nullable=False, default=1, doc="用户状态，0-禁用，1-启动")
    create_datetime = db.Column(db.DateTime, server_default=db.text("CURRENT_TIMESTAMP"), doc="创建时间")
    update_datetime = db.Column(db.DateTime, nullable=False,server_default=db.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), doc="更新时间")

    def __init__(self, **kwargs):
        super(DiscoveryPartnerUsers, self).__init__(**kwargs)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return "User<name:%r>" % self.username
