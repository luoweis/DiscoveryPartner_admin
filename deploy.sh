#!/bin/bash
virtualenv -p `which python3.6` venv
echo "start pip install requirements.txt"
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
flask run -h 0.0.0.0 -p 8080
