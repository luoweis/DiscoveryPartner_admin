#!/usr/bin/env python
# -*- coding=utf-8 -*-
from app.models.Projects import *
from app import db
from flask import jsonify


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


def delete_projects(project_id):
    """
    删除数据
    :param args:
    :return:
    """
    try:
        DiscoveryPartnerProjects.query.filter_by(id=project_id).delete()
        db.session.commit()
    except Exception as error:
        return {"error_msg": error}
    else:
        return {
            "msg": "删除成功",
        }


def modify_project(**kwargs):
    project_id = kwargs.get('id')
    kwargs.pop("id")
    # print(kwargs)
    DiscoveryPartnerProjects.query.filter_by(id=project_id).update(kwargs)
    db.session.commit()
    return


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


def find_project_by_id(project_id):
    """
    根据id值进行数据的查询
    :param
    :return:
    """
    project_info = DiscoveryPartnerProjects.query.filter_by(id=project_id).first()

    return jsonify({
        "project_id": project_info.id,
        "project_name": project_info.name,
        "project_info": project_info.info,
        "project_status": project_info.status,
        "project_client": project_info.client,
        "project_members": project_info.members,
        "project_image": project_info.image,
    })
