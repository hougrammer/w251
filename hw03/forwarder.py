import paho.mqtt.client as mqtt

i = [0]
def on_message(client, userdata, message):
    print('Publishing message ' + str(i[0]))
    i[0] += 1
    pub.publish('forwarder_out', message.payload)
    


sub = mqtt.Client()
sub.connect('face_detector')
sub.subscribe('detector_out')

pub = mqtt.Client()
pub.connect('169.53.138.75')

sub.on_message = on_message
sub.loop_forever()
