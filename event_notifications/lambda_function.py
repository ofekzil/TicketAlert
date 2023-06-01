from run_queries import insert, delete, select
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

 # All needed functionality (commented out in handler) now works in Lambda
def lambda_handler(event, context):
    logger.info(event)
    
    op = event.get("operation")
    if (op == "insert"):
        insert(event.get("info"))
    elif (op == "delete"):
        delete()
    elif (op == "select"):
        select()
    else:
        logger.error("Invalid operstion")
    
    return {
        "statusCode" : 200,
        "event" : json.dumps(event)
    }