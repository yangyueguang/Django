FROM python:3.7
MAINTAINER xuechao <xuechao@datagrand.com>
ENV TZ=Asia/Beijing
ADD apps /apps
ADD setup.py /setup.py

#install requires
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --upgrade pip
RUN pip install -r /apps/requirs.txt -i https://pypi.douban.com/simple/

WORKDIR /apps
# 加密py
#RUN c && rm /flask/setup.py

EXPOSE 5001
CMD sh runserver.sh

#ENTRYPOINT celery -A tasks worker --loglevel=info
#CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--workers", "3", "app:app"]
#数据迁移
#CMD sh migrate.sh