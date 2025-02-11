import sys
sys.path.insert(0,'/opt')
import json
from baseDAO import BaseDAO
import os



def queueWatcherHandler(event, context):
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
    
    if 'Records' not in event:
        raise Exception('Evento com formato errado: não possui Records')
    pedidosDAO= BaseDAO('pedidos-pizzaria')
    for record in event['Records']:
        print('processing record:')
        print(record)
        record_body = json.loads(record['body'])
        
        file_name = record_body['s3']['object']['key']
        folder,filename=file_name.split('/')
        id_pedido,customer_name = filename.split('-')
        dynamo_item={}
        dynamo_item['pedido']=id_pedido
        dynamo_item['datetime']='' #TODO: descobrir o campo datetime
        dynamo_item['cliente']=customer_name
        dynamo_item['status']=folder
        
        pedidosDAO.put_item(dynamo_item)
        
            
        
        
    
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    # """
