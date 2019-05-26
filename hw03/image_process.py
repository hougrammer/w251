from __future__ import print_function
import paho.mqtt.client as mqtt
import ibm_boto3
from ibm_botocore.client import Config
import json

auth_endpoint = 'https://iam.bluemix.net/oidc/token'
service_endpoint = 'https://s3-api.us-geo.objectstorage.softlayer.net'

with open('/credentials/credentials.json') as f:
    credentials = json.load(f)

resource = ibm_boto3.resource('s3',
                      ibm_api_key_id=credentials['apikey'],
                      ibm_service_instance_id=credentials['resource_instance_id'],
                      ibm_auth_endpoint=auth_endpoint,
                      config=Config(signature_version='oauth'),
                      endpoint_url=service_endpoint)

bucket_name = 'davidhou-bucket'
obj = resource.Object(bucket_name=bucket_name, key='download.jpeg').get()

i = [0]
def on_message(client, userdata, message):
    print('Storing image {} in object store'.format(i[0]))
    resource.Bucket(name='davidhou-bucket').put_object(Key='image' + str(i[0]), Body=message.payload)
    i[0] += 1

client = mqtt.Client()
client.connect('169.53.138.75')
client.subscribe('forwarder_out')
client.on_message = on_message
client.loop_forever()
