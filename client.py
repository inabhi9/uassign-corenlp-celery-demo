"""
For collecting NERs, Stanford Core NLP is used using Python wrapper
(https://bitbucket.org/torotoki/corenlp-python.git)
To use this library, actual NLP library is needed and can be downloaded from
(http://nlp.stanford.edu/software/stanford-corenlp-full-2013-11-12.zip)

This module contains two functions,
1) sendToParser: which opens the db, iterate the document and send them to task queue
2) parseArticle: Which process the document and store the output. This function is asynchronous and
is callable by celery 
"""


import config
from celerytask import celery
from pymongo import MongoClient
from corenlp import StanfordCoreNLP
from datetime import datetime
import jsonrpclib
from simplejson import loads

# Mongo connection and db init
mongoClient = MongoClient(config.MONGO_URI)
db = getattr(mongoClient, config.MONGO_DB)
inputCol = getattr(db, config.MONGO_INPUT_COLLECTION)
outputCol = getattr(db, config.MONGO_OUTPUT_COLLECTION)


def sendToParser():
    """
    Will iterate through each document and send em to the task queue
    """
    mCur = inputCol.find()
    for doc in mCur:
        parseArticle.delay(str(doc.get('_id')), doc.get('description'))

@celery.task
def parseArticle(articalId, strText):
    """
    Process given text and collect NamedEntityResolution using Stanford Core NLP library
    
    :param mixed articalId: Article id to link output
    :param str strText: Text to be parsed
    
    :retval None  
    """
    
    startAt = datetime.now().strftime('%H:%M:%S:%f')    
    parsedObj = loads(coreNlp.parse(strText))
    
    ners = []
    for sentence in parsedObj.get('sentences'):
        for word in sentence.get('words'):
            w, d = word
            # collecting NERs
            if d.get('NamedEntityTag') == 'O': continue
            ners.append(w)
    endAt = datetime.now().strftime('%H:%M:%S:%f')
    # preparing output
    out = {'articleId': articalId,
           'startTime': startAt,
           'endTime': endAt,
           # 'threadId': 1,  
           'noNers': len(ners),
           'ner': ners}
    # saving to db
    outputCol.save(out)

if __name__ == '__main__':
    sendToParser()
    
if __name__ == 'client':
    coreNlp = jsonrpclib.Server("http://%s" % config.CORENLP_SERVER)
