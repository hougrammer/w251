# Homework 3

## Face Detector
This runs on my TX2.  It publishes images to topic `detector_out`.
```
docker build -t face_detector -f Dockerfile.face .
docker run --name face_detector -e DISPLAY=$DISPLAY --rm --privileged -v /home/david/w251/hw03:/hw03 -v /tmp/.X11-unix:/tmp/.X11-unix --device /dev/video1 --network hw03 -it face_detector bash
mosquitto -d
python face_detect.py
```

## MQTT Message Forwarder
This also runs on my TX2.  I'm using QOS 0 for publishing messages because I don't really care if a few images of my face get dropped on the way to the internet.  I read messages from topic `detector_out` and publish them to `forwarder_out`.
```
docker build -t mqtt_broker -f Dockerfile.broker .
docker run --name broker --rm --network hw03 -it -v /home/david/w251/hw03:/hw03 mqtt_broker sh
mosquitto -d
python forwarder.py
```

## Image Saver
This runs on my VSI.  I read messages from topic `forwarder_out` and save them to object store.
```
docker build -t cos_saver
docker run --name saver --rm -v $HOME/w251/hw03:/hw03 -v $HOME/credentials:/credentials -it cos_saver sh
mosquitto -d
python image_process.py
```
Get images from http://s3-api.us-geo.objectstorage.softlayer.net/davidhou-bucket/image#.
The face detector sent 12 images but images 7-9 were dropped due to QOS.
