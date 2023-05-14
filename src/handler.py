import json
import boto3

client = boto3.client('iot-data', region_name='us-west-2')

def lambda_handler(event, context):
    # print(event)
    try:
        id = event['id']
        digital_value = event['digital_value']
        print("Device ID: ", id)
        print("Device Digital Value: ", digital_value)
        
        # Publish the data to AWS IoT Core
        response = client.publish(
            topic='test/topic',
            qos=1,
            payload=json.dumps({'id': id, 'digital_value': digital_value})
        )
        
        print(response)
        
        return {
            'statusCode': 200,
            'body': json.dumps('Successful Post Request')
            
        }
    
    except KeyError as e:
        error_msg = f"Bad Request: Missing required key '{e.args[0]}'"
        return {
            'statusCode': 400,
            'body': json.dumps({'Error': error_msg})
        }
    except Exception as e:
        error_msg = f"Internal Server Error: {str(e)}"
        return {
            'statusCode': 500,
            'body': json.dumps({'error': error_msg})
        }
