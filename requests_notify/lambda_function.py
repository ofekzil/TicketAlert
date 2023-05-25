from run_queries import insert, delete, select
import logging
import os
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

 # All needed functionality (commented out in handler) now works in Lambda
 # TODO: Work out currency conversions in event model (DB, class, notification)
 # TODO: set up triggers for events and ensure some id is passed in each one to differentiate between which function to call
def lambda_handler(event, context):
   
    # e = {'performerAndCity':'Alice Cooper Detroit', 
    #     'eventDate':'5 21 2023',
    #     'eventUrl':"https://www.stubhub.ca/alice-cooper-detroit-tickets-5-21-2023/event/132569874/",
    #     'threshold':95,
    #     'email':os.environ.get("RECEIVER")}
    # insert(e)
    # select()
    # delete()
    return {
        "statusCode" : 200
    }