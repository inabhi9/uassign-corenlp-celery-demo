# MongoDB config
#----------------------------------------------------
MONGO_DB = "test1"
MONGO_URI = "mongodb://localhost"
# output will be stored here, instead of log file
MONGO_OUTPUT_COLLECTION = "articles_ners"
# input from here, document should contain description field
MONGO_INPUT_COLLECTION = "articles"


# Stanford Core NLP config
#----------------------------------------------------
# download it from:
#    http://nlp.stanford.edu/software/stanford-corenlp-full-2013-11-12.zip
CORENLP_LIB_DIR = '/opt/stanford-corenlp-full-2013-11-12'


# Celery configuration
#----------------------------------------------------
# Redis for celery broker
REDIS_BROKER_HOST = 'localhost'
REDIS_BROKER_PORT = 6379
REDIS_BROKER_DB = 11
# no of worker, good to have no of cpu core +1
# although it would be great if tested and tuned
CELERYD_CONCURRENCY = 2
CELERY_RESULT_BACKEND = 'redis'
CELERY_TIMEZONE = 'Asia/Calcutta'
# SHOULD NOT TOUCH
CELERY_TASK_SERIALIZER = 'json'
BROKER_URL = "redis://%s:%s/%i" % (REDIS_BROKER_HOST, REDIS_BROKER_PORT, REDIS_BROKER_DB)
CELERY_ACCEPT_CONTENT = ['pickle', 'json']