# -*- coding:utf-8 -*-
import logging
from django.core.mail import send_mail
from smtplib import SMTPException

logger = logging.getLogger('app')


def send():
    try:
        ret = send_mail(
            'Subject here', 'Here is the message.',
            'django_hyh@163.com', ['2285020853@qq.com', 'django_hyh@163.com', 'hyhlinux@163.com'],
            fail_silently=False)
    except SMTPException as e:
        logging.error(e)
        return "{}".format(e)
    except Exception as e:
        logging.error(e)
        return "{}".format(e)
    return ret
