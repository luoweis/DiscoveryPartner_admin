#!/usr/bin/env python
# -*- coding=utf-8 -*-
"""
局部公共函数库
"""
import pprint

def test():
    print(f"公共函数方法")


def get_data_from_webhook_json(res):
    """
    从wehbook反推给我们的数据中获取需要的信息并格式化输出
    :param res:
    :return:
    """
    push_branch_info = res.get("ref")
    push_branch = push_branch_info.split("/")[-1]
    commit_info = res.get("commits")[0].get("message")
    author = res.get("commits")[0].get("author")
    data = {
        "branch": push_branch,
        "commit": commit_info,
        "author": author,
    }
    pprint.pprint(data)
    return data