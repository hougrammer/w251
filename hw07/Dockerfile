FROM w251/cuda:dev-tx2-4.2_b158

ARG URL=http://169.44.201.108:7002/jetpacks/4.2

RUN apt-get update && apt install -y \
    git \
    pkg-config \
    wget \
    build-essential \
    cmake \
    unzip \
    python3-pip \
    vim \
    inetutils-ping \
    mosquitto \
    mosquitto-clients

WORKDIR /tmp

RUN curl $URL/libopencv_3.3.1-2-g31ccdfe11_arm64.deb -so libopencv_3.3.1-2-g31ccdfe11_arm64.deb
RUN curl $URL/libopencv-dev_3.3.1-2-g31ccdfe11_arm64.deb -so libopencv-dev_3.3.1-2-g31ccdfe11_arm64.deb
RUN curl $URL/libopencv-python_3.3.1-2-g31ccdfe11_arm64.deb -so libopencv-python_3.3.1-2-g31ccdfe11_arm64.deb

RUN apt install -y  libtbb-dev libavcodec-dev libavformat-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgtk2.0-dev
RUN apt install -y libswscale-dev libv4l-dev
RUN dpkg -i *.deb

RUN apt install -y libcanberra-gtk-module libcanberra-gtk3-module libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev 

RUN python3 -m pip install --upgrade pip
RUN pip3 install paho-mqtt

# HW 07
RUN apt install -y zlib1g-dev zip libjpeg8-dev libhdf5-dev
RUN pip3 install -U numpy grpcio absl-py py-cpuinfo psutil portpicker grpcio six mock requests gast h5py astor termcolor Pillow

RUN pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v42 tensorflow-gpu

RUN rm -f /tmp/*.deb
WORKDIR /root

