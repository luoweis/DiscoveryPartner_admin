#! /usr/bin/env python
# -*- coding=utf-8 -*-

from flask import render_template, request, redirect, url_for, flash
from app.bpurls import projectsBP
from flask_login import login_required
from app.common.discoveryPartner_mysql_projects_utils import *
from app.forms.projects_add import ProjectAddForm
from app.common.util import *
from flask_socketio import emit
from app import socketio
import time

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
            "project_status": project_life_cycle_content(project.status),
            "project_info": project.info,
            "project_create": project.create_datetime,
            "project_client": project.client,
            "project_members": project.members,
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
        "status": request.form.get("project_status"),
        "client": request.form.get("project_client"),
        "members": request.form.get("project_members"),
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
        "id": request.form.get("project_ID"),
        "name": request.form.get("project_name"),
        "info": request.form.get("project_info"),
        "status": request.form.get("project_status"),
        "client": request.form.get("project_client"),
        "members": request.form.get("project_members"),
    }

    modify_project(**project)
    return redirect(url_for("projectsBP.info"))


@projectsBP.route('/get/project/', methods=['POST'])
@login_required
def get_project_by_id():
    """
    通过传递过来的id值提取数据
    :return:
    """
    if request.method == "POST":
        datas = eval(request.data)
        project_id = datas.get("project_id")
        project_info = find_project_by_id(project_id)
    else:
        return
    return project_info


@socketio.on('request_for_response', namespace='/deleteProjects')
def give_response(data):
    projects_info = data.get('projects')
    if not projects_info:
        return

    projects = json.loads(projects_info)

    while projects:
        project = projects.pop()
        # delete project from mysql by 'id'
        delete_projects(project.get("project_id"))
        emit('response', {'code': '200', 'msg': project.get("project_name")})
        continue
