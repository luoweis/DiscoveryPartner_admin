#!/usr/bin/env python
# -*- coding=utf-8 -*-
from app.models.Projects import *
from app import db


def add_project_single(**kwargs):
    """
    一次只增加一个项目的信息，写入数据库中
    :param kwargs:
    :return:
    """
    """判断添加的元素是否存在"""
    waring = ""
    if DiscoveryPartnerProjects.query.filter_by(id=kwargs.get("project_id")).all():
        return {"msg": "该项目已经被添加"}
    try:
        project = DiscoveryPartnerProjects(**kwargs)
        db.session.add(project)
        db.session.commit()
    except Exception as error:
        return {"error_msg": error}
    else:
        return {"msg": "添加成功"}


def projects_onepage_datas(pageSize, offset):
    """
    获取单页数量的名单
    :param pageSize:
    :param offset:
    :return:
    """
    res = DiscoveryPartnerProjects.query.limit(pageSize).offset(offset).all()
    return res


def projects_total_count():
    """
    获取总数
    :return:
    """
    total = DiscoveryPartnerProjects.query.count()
    return total