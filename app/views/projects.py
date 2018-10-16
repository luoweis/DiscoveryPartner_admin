#! /usr/bin/env python
# -*- coding=utf-8 -*-

from flask import render_template, request, redirect, url_for
from app.bpurls import projectsBP
from flask_login import login_required
from app.common.discoveryPartner_mysql_projects_utils import *
from app.forms.projects_add import ProjectAddForm
from app.common.util import *


@projectsBP.route('/info',methods=['GET'])
@login_required
def info():
    context = {}
    form = ProjectAddForm()
    context["form"] = form
    context["title"] = "同道中人"
    context["content"] = "同道中人"
    return render_template('projectManagement/projectsInfo.html', **context)


@projectsBP.route('/show/', methods=['GET'])
@login_required
def projects_show():
    """
    获取项目的信息
    :return:
    """

    """提取参数"""
    pageSize = request.args.get("pageSize")
    offset = request.args.get("offset")
    sort = request.args.get("sort")
    sortOrder = request.args.get("sortOrder")
    """根据偏移量和每一页人数进行数据库的查询工作"""
    projects = projects_onepage_datas(pageSize, offset)

    """格式化数据"""
    def format(project):
        return {
            "project_id": project.id,
            "project_name": project.name,
            "project_status": project.status,
            "project_info": project.info,
            "project_create": project.create_datetime,
        }

    rows = list(map(format, projects))
    total = projects_total_count()
    return json.dumps({
        "rows": rows,
        "total": total,
    }, cls=DateEncoder)


@projectsBP.route('/project/add/', methods=['POST'])
@login_required
def project_add():
    """
    表单的方式提交项目信息
    :return:
    """
    project = {
        "name": request.form.get("project_name"),
        "info": request.form.get("project_info"),
        "status": 0
    }

    add_project_single(**project)
    return redirect(url_for("projectsBP.info"))


@projectsBP.route('/project/modify/', methods=['POST'])
@login_required
def project_modify():
    """
    表单的方式修改项目信息
    :return:
    """
    project = {
        "name": request.form.get("project_name"),
        "info": request.form.get("project_info"),
        "status": 0
    }

    add_project_single(**project)
    return redirect(url_for("projectsBP.info"))