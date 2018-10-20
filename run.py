#!/usr/bin/env python
# -*- coding=utf-8 -*-
from app import app, socketio
print(app.url_map)


if __name__ == "__main__":
    socketio.run(app)