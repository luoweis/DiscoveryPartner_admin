#!/usr/bin/env python
# -*- coding=utf-8 -*-
from flask import render_template, request, flash, redirect, url_for
from app.bpurls import authBP
from app.forms.login import LoginForm
from app.models.Users import DiscoveryPartnerUsers
from flask_login import login_user, login_required, logout_user
from app import login_manager


@login_manager.user_loader
def load_user(user_id):
    return DiscoveryPartnerUsers.query.get(int(user_id))


@authBP.before_request
def before_request():
    pass


@authBP.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        if not form.validate_on_submit():
            # print(form.errors)
            return render_template("auth/signin.html", form=form)
        user = DiscoveryPartnerUsers.query.filter(DiscoveryPartnerUsers.username == form.username.data).first()
        if not user:
            flash("该用户不存在", "error")
        else:
            if user.password != form.password.data:
                flash("用户密码错误", "error")
            else:
                login_user(user)
                next_url = request.args.get("next")
                return redirect(next_url or url_for("mainBP.main"))
    return render_template("auth/signin.html", form=form)


@authBP.route('/logout/', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("mainBP.main"))
