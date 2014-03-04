# Taking Ubuntu 12.04 as base image for the deployment
FROM ubuntu:12.04

# Update apt source list
RUN apt-get -y update

# Installing required system components
RUN apt-get -y install python-dev gcc python-pip git wget unzip python-software-properties nano
RUN add-apt-repository -y ppa:webupd8team/java && apt-get -y update
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections
RUN apt-get install oracle-java7-installer -y

# Changing up working directory to /opt
# to fetching apps and corenlp
WORKDIR /opt

# Pulling source and required libs
RUN git clone https://inabhi9@bitbucket.org/inabhi9/uassign-corenlp-celery-demo.git
RUN wget http://nlp.stanford.edu/software/stanford-corenlp-full-2013-11-12.zip && unzip stanford-corenlp-full-2013-11-12.zip && rm -fr stanford-corenlp-full-2013-11-12.zip

# Installing application specific components
WORKDIR /opt/uassign-corenlp-celery-demo
RUN pip install -r requirements.txt

ADD ../config.py /opt/uassign-corenlp-celery-demo/
CMD ifconfig