FROM hyhlinux/env_django

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000 8000
#CMD ["gunicorn", "main:aioapp", "-c", "gunicorn.conf.py", "-k", "aiohttp.worker.GunicornWebWorker"]
CMD ["gunicorn", "web.wsgi:application", "-c", "gunicorn.conf.py"]
