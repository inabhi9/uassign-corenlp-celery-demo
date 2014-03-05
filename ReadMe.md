CoreNLP-Celery demo
---------------

As per your requirements, I've created a prototype project which iterate through the tasks and send them to the task queue. Output is stored in mongodb itself as for distributing system, storing in file at local system doesn't make sense

For distributed task queue, I used Celery with gevent multiprocessing library. Celery taskes care of running queued task, generating events and failure.


### Installation
For ubuntu 13.10, but should work on 12.04+

* pull repository
* Install pip: sudo apt-get install python-pip
* Install redis:
    * sudo apt-add-repository ppa:rwky/redis
    * sudo apt-get update
    * sudo apt-get install redis-server
* Install mongodb:
        
         sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
        
        echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list

        sudo apt-get update
        
        sudo apt-get install mongodb-10gen
        
* pip install -r requirements.txt
* Download NLP lib
    
    http://nlp.stanford.edu/software/stanford-corenlp-full-2013-11-12.zip


### Running on local machine

* Copy docker-builder/config.py.sample to parent directory as config.py and make necessary changes to it
* For task worker
    You can run task worker on any no of machine. You need to setup only application requirements

        celery -A celerytask worker -P gevent

* To enqueue the task:

        python client.py

* You must have coreNLP server up and running. You can run it by

        python /usr/local/lib/python2.7/dist-packages/corenlp/corenlp.py -H 0.0.0.0 -p 3456 -S /opt/stanford-corenlp-full-2013-11-12/