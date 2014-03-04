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

Before building application server, you need to edit config.py as this file will be applied to application during the docker build.  
- This application will take articles document from the MongoDB and output in the same database. Edit the MongoDB parameters accordingly. (if you dont have a MongoDB server up and running, see the below section on how to build MongoDB server)  
- Change the Redis broker host to the IP noted earlier.
- As per default configuration, each celery process spawn two worker.

To build, run following command  

    sudo docker build -t nlp_demo/app .

on successful completion, execute image by running following command

    sudo docker run nlp_demo/app
    
You can run as many container as you want by running above command again and again. This will demonstrate the distributed computing.

----------

Setup MongoDB
---------

If you don't have a MongoDB server up and running, you can easily build it using `Docker-mongo` file.
To build, run following command  

    sudo docker build -t nlp_demo/mongodb - < Docker-mongo

on successful completion, execute image by running following command

    sudo docker run nlp_demo/mongodb
    
This will print the `ifconfig` ouput and start the mongodb server. Please note down the IP address assigned to the container for `eth0` interface.  
Please load the sample articles in the database. To do so, follow these instruction on the host machine

    wget https://bitbucket.org/inabhi9/uassign-corenlp-celery-demo/downloads/article_dump.json.tar.bz2
    bzip2 -d article_dump.json.tar.bz2
    tar -xvf article_dump.json.tar
    mongoimport -h IP_ASSIGNED_TO_MONGO_CONTAINER -d nlp_demo -c articles article_dump.json

  [1]: http://docs.docker.io/en/latest/installation/