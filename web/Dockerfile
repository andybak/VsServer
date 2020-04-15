# Python3
# postgresql-cliente
# dependencias de geodjango, como GDAL
FROM makinacorpus/geodjango:bionic-3.6

RUN apt-get update -qq && apt-get install -y -qq libspatialindex-dev
RUN apt-get clean && apt-get update && apt-get install -y locales
RUN export LC_ALL=en_US.UTF-8
RUN export LANG=en_US.UTF-8
RUN locale-gen en_US.UTF-8

RUN mkdir -p /data/web

WORKDIR /data/web

RUN mkdir -p ./gisdrf/statics/admin

COPY requirements.txt /data/web/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /data/web/