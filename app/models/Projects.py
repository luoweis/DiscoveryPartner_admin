#!/usr/bin/env python
# -*- coding=utf-8 -*-

from app import db


class DiscoveryPartnerProjects(db.Model):
    # define table name
    __tablename__ = 'projects_info'
    id = db.Column(db.Integer, primary_key=True)
    # id = db.Column(db.Integer, db.ForeignKey('xsk_class.id'), nullable=True, unique=True)
    name = db.Column(db.String(32), unique=False, nullable=False, index=True)
    status = db.Column(db.SmallInteger, nullable=False, default=0, doc="项目状态，0-立项阶段，1-项目启动, 2-持续开发阶段, 3-产品交付")
    client = db.Column(db.String(100), unique=False, nullable=False, doc="客户信息")
    info = db.Column(db.String(200), nullable=True)
    members = db.Column(db.String(500), nullable=True, unique=False, default=None, doc="组员信息")
    image = db.Column(db.String(200), nullable=True)
    create_datetime = db.Column(db.DateTime, server_default=db.text("CURRENT_TIMESTAMP"), doc="创建时间")
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=db.text(
        "CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
                                doc="更新时间")

    def __init__(self, **kwargs):
        super(DiscoveryPartnerProjects, self).__init__(**kwargs)

    def __repr__(self):
        return "Student<name:%r>" % self.name