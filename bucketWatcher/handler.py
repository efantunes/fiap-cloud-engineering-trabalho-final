import sys
sys.path.insert(0,'/opt')
import json
from sqsHandler import SqsHandler
import os



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
    
    if 'ready_queue_url' not in os.environ:
        raise Exception('Variavel de ambiente nao setada: ready_queue_url')
    print(f"URL da fila de pronto: {os.environ['ready_queue_url']}")
    if 'preparation_queue_url' not in os.environ:
        raise Exception('Variavel de ambiente nao setada: preparation_queue_url')
    print(f"URL da fila de preparacao: {os.environ['preparation_queue_url']}") 
    
    if 'Records' not in event:
        raise Exception('Evento com formato errado: não possui Records')
    
    sqs_client_ready = SqsHandler(os.environ['ready_queue_url'])
    sqs_client_preparation = SqsHandler(os.environ['preparation_queue_url'])
    for record in event['Records']:
        print('processing record:')
        print(record)
        if 's3' not in record:
            print(Exception('Evento com formato errado: não possui Records.s3'))
            continue
        if 'object' not in record['s3']:
            print(Exception('Evento com formato errado: não possui Records.s3.object'))
            continue
        if 'key' not in record['s3']['object']:
            print(Exception('Evento com formato errado: não possui Records.s3.object.key'))
            continue
        
        file_name = record['s3']['object']['key']
        folder,filename=file_name.split('/')
        if folder == 'em-preparacao':
            sqs_client_preparation.send(json.dumps(record))
        elif folder=='pronto':
            sqs_client_ready.send(json.dumps(record))
        else:
            print(f"Pulando arquivo: Pasta nao reconhecida: {folder}")
            
        
        
    
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    # """
