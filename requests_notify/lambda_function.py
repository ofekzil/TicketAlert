from run_queries import insert, delete, select, hello
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    res = hello()
    logger.info("Got the result, %s", res)