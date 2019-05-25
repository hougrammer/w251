import paho.mqtt.client as mqtt    #import client library
import time

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected ok")
def on_publish(client,userdata,result):   #create function for callback
    print("data published")

client = mqtt.Client('python1')             #create new instance 
client.on_connect = on_connect  #bind call back function
client.connect('broker1')               #connect to broker
client.loop_start()  #Start loop 
time.sleep(2) # Wait for connection setup to complete
client.publish('hw03', 'test')
client.loop_stop()    #Stop loop 
