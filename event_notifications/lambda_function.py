from run_queries import insert, delete, select, unsubscribe
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

 # All needed functionality (commented out in handler) now works in Lambda
def lambda_handler(event, context):
    logger.info(event)
    if ("operation" in event):
        op = event.get("operation")
        if (op == "insert"):
            insert(event.get("info"))
        elif (op == "delete"):
            delete()
        elif (op == "select"):
            select()
        else:
            logger.error("Invalid operation")
    elif ("queryStringParameters" in event):
        params = event.get("queryStringParameters")
        unsubscribe(params["url"], params["threshold"], params["email"])
        return {
            "statusCode" : 200,
            "headers" : {"Your-custom-header" : "custom-header-value"},
            "body" : json.dumps({"message" : "You have successfully unsubscribed from the event notifications!"})
        }
    else:
        logger.error("Invalid operation")
    
    return {
        "statusCode" : 200,
        "event" : json.dumps(event)
    }