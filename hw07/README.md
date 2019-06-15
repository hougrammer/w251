Started with Dockerfile for face detection from hw03.
Add the following to install Tensorflow.

```
RUN apt install -y zlib1g-dev zip libjpeg8-dev libhdf5-dev 
RUN pip3 install -U numpy grpcio absl-py py-cpuinfo psutil portpicker grpcio six mock requests gast h5py astor termcolor Pillow

RUN pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v42 tensorflow-gpu
RUN pip3 install Pillow
```

Run with
```
python3 inference_usbCam_face.py 1
```
