FROM amazonlinux:2018.03
RUN ulimit -n 1024 && yum -y update && yum -y install \
    python3.10 \
    python3.10-pip \
    python3.10-devel \
    zip \
    && yum clean all

RUN python3 -m pip install pip==22.1.2
RUN pip install virtualenv==20.14.1
