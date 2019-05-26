# Homework 3

## Running Face Detector
```
docker run --name face_detector -e DISPLAY=$DISPLAY --rm --privileged -v /home/david/w251/hw03:/hw03 -v /tmp/.X11-unix:/tmp/.X11-unix --device /dev/video1 --network hw03 -it face_detector bash
```

## Running MQTT Broker
```
docker run --name broker --rm --network hw03 -it -v /home/david/w251/hw03:/hw03 mqtt_broker
mosquitto -d
```
### Subscribing
```
mosquitto_sub -t hw03 -h <host>
```
### Publishing
```
mosquitto_pub -t hw03 -m <message>
```
