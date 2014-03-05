Docker setup for CoreNLP Celery demo
=====================


Docker is a lightweight linux container.
For installation instruction please follow this link: [Docker.io installation][1]  


----------


Setup Redis
---------

If you don't have a Redis server up and running, you can easily build Redis server image using `Docker-redis` file.
To build, run following command  

    sudo docker build -t nlp_demo/redis - < Docker-redis

on successful completion, execute image by running following command

    sudo docker run nlp_demo/redis
    
This will print the `ifconfig` ouput and start the redis-server. Please note down the IP address assigned to the container for `eth0` interface.

----------

Setup Celery-App
---------

Before building application server, you need to edit config.py (rename config.py.sample) as this file will be applied to application during the docker build.  
- This application will take articles document from the MongoDB and output in the same database. Edit the MongoDB parameters accordingly. (if you don't have a MongoDB server up and running, see the below section on how to build MongoDB server)  
- Change the Redis broker host to the IP noted earlier.
- As per default configuration, each celery process spawn two worker.

To build application server, run following command  

    sudo docker build -t nlp_demo/app .


This image will run two programs using supervisor, 1) CoreNLP server 2) Worker server. To start container with supervisor

    sudo docker run nlp_demo/app /usr/bin/supervisord

You can run as many container as you want by running above command again and again. This will demonstrate the distributed computing (ofcourse you must have that much system configuration).  
    
To enqueue the jobs, run this command

    sudo docker run nlp_demo/app python /opt/uassign-corenlp-celery-demo/client.py

This will enqueue the entire articles collection.  

To see the output, you can login to mongodb and find the collection named `articles_ners` or whatever you set in `config.py` file


----------

Setup MongoDB
---------

If you don't have a MongoDB server up and running, you can easily build it using `Docker-mongo` file.
To build, run following command  

    sudo docker build -t nlp_demo/mongodb - < Docker-mongo

on successful completion, execute the image by running following command

    sudo docker run nlp_demo/mongodb
    
This will print the `ifconfig` ouput and start the mongodb server. Please note down the IP address assigned to the container for `eth0` interface. This image comes with pre-loaded sample articles.

  [1]: http://docs.docker.io/en/latest/installation/