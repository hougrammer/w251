import paho.mqtt.client as mqtt

i = [0]
def on_message(client, userdata, message):
    print('Received message ' + str(i[0]))
    i[0] += 1

client = mqtt.Client()
client.connect('169.53.138.75')
client.subscribe('forwarder_out')
client.on_message = on_message
client.loop_forever()
