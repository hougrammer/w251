import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print('Publishing message...')
    client.connect(169.53.138.75)
    client.publish('forwarder_out', message.payload)
    print('First 64 characters of message: {}'.format(message.payload[:64]))
    client.connect('face_detector')


client = mqtt.Client()
client.connect('face_detector')
client.subscribe('detector_out')
client.on_message = on_message
client.loop_forever()
