FROM python

MAINTAINER Yuze Ma <yuze.bob.ma@gmail.com>

ENV SRC_PATH /usr/src/

RUN mkdir -p $SRC_PATH

WORKDIR $SRC_PATH
COPY . $SRC_PATH

RUN pip install -r requirements.txt

# CMD ["bin/bash"]

