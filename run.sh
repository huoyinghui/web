# 使用配置文件
gunicorn -c gunicorn.conf.py web.wsgi:application -b 0.0.0.0:8080
