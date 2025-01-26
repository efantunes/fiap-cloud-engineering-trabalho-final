import sys
sys.path.insert(0,'/opt')
import json
from sqsHandler import SqsHandler



def bucketWatcherHandler(event, context):
    # body = {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "input": event
    # }

    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(body)
    # }

    # return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    # """
    print(event)
    print(context)
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    # """
