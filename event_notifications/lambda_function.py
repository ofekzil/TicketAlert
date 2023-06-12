from run_queries import insert, delete, select, unsubscribe, unsubscribe_all
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
        response = {
            "statusCode" : 200,
            "headers" : {"Your-custom-header" : "custom-header-value"},
            "body" : ""
        }
        params = event.get("queryStringParameters")
        op = params.get("op")
        if (op == "this"):
            unsubscribe(params.get("eid"))
            response["body"] = json.dumps("You have successfully unsubscribed from this event's notifications!")
        elif (op == "all"):
            unsubscribe_all(params.get("eid"))
            response["body"] = json.dumps("You have successfully unsubscribed from ALL event notifications!")
        else:
            logger.error("Invalid operation")
        return response
    else:
        logger.error("Invalid operation")
    
    return {
        "statusCode" : 200,
        "event" : json.dumps(event)
    }