#!/usr/bin/env python
# -*- coding=utf-8 -*-

from app import db


class DiscoveryPartnerProjects(db.Model):
    # define table name
    __tablename__ = 'projects_info'
    id = db.Column(db.Integer, primary_key=True)
    # id = db.Column(db.Integer, db.ForeignKey('xsk_class.id'), nullable=True, unique=True)
    name = db.Column(db.String(32), unique=False, nullable=False, index=True)
    # student_age = db.Column(db.SmallInteger, nullable=False, doc="学生年龄")
    # student_sex = db.Column(db.SmallInteger, nullable=False, default=1, doc="性别，0-男性，1-女性")
    # student_phone = db.Column(db.String(32), nullable=True, unique=True)
    # student_ID = db.Column(db.String(32), nullable=True, unique=True)
    info = db.Column(db.String(100), nullable=True)
    status = db.Column(db.SmallInteger, nullable=False, default=1, doc="项目状态，0-立项阶段，1-项目启动, 2-持续开发阶段, 3-产品交付")
    image = db.Column(db.String(100), nullable=True)
    create_datetime = db.Column(db.DateTime, server_default=db.text("CURRENT_TIMESTAMP"), doc="创建时间")
    update_datetime = db.Column(db.DateTime, nullable=False, server_default=db.text(
        "CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
                                doc="更新时间")

    def __init__(self, **kwargs):
        super(DiscoveryPartnerProjects, self).__init__(**kwargs)

    def __repr__(self):
        return "Student<name:%r>" % self.name