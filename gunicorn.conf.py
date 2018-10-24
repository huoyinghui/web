# -*- coding:utf-8 -*-
import os
import multiprocessing
import getpass


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR_LOGS = '/tmp'
who = getpass.getuser()
if who == 'root':
    BASE_DIR_LOGS = '/var/www/app/logs'
# 绑定的ip与端口
bind = "0.0.0.0:8000"
# 核心数
workers = multiprocessing.cpu_count()
# 使用gevent模式，还可以使用sync 模式，默认的是sync模式
worker_class = 'gevent'
# 等待服务的客户的数量,超过这个数字将导致客户端在尝试连接时错误
backlog = 2048


# 发生错误时log的路径
errorlog = os.path.join(BASE_DIR_LOGS, 'gunicorn.error.log')
# 正常时的log路径
accesslog = os.path.join(BASE_DIR_LOGS, 'gunicorn.access.log')
# 日志等级
loglevel = 'debug'
# 进程名
proc_name = 'gunicorn_main'
timeout = 30
