FROM jupyter/datascience-notebook

MAINTAINER Yuze Ma <yuze.bob.ma@gmail.com>

ENV SRC_PATH /home/jovyan/work

# RUN mkdir -p $SRC_PATH

WORKDIR $SRC_PATH
COPY . $SRC_PATH

RUN pip install -r requirements.txt

# CMD ["bin/bash"]

