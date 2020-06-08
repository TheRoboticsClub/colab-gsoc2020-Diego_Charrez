FROM nvidia/cuda:10.1-cudnn7-devel

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && apt-get -y upgrade && apt-get install -y --no-install-recommends \
        apt-utils \
        cmake \
        curl \
        firefox \
        git \
        icewm \
	libssl-dev \
        python-opengl \
        python3-setuptools \
        python3-pip \
        sudo \ 
        tmux \
        vim \
        wget \
        xvfb \
        x11vnc && \
    pip3 install jupyterlab virtualenv && \
    apt-get autoclean && \
    apt-get autoremove

# ROS melodic
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' && \
    apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654 && \
    apt update && apt install -y --no-install-recommends \
        ros-melodic-desktop-full

# Jderobot base and assets
RUN sh -c 'echo "deb [arch=amd64] http://wiki.jderobot.org/apt `lsb_release -cs` main" > /etc/apt/sources.list.d/jderobot.list' && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv 24E521A4 && \
    apt update && apt install -y --no-install-recommends \
        jderobot \
        jderobot-assets \
        ros-melodic-jderobot-assets && \
    echo "source /opt/jderobot/share/jderobot/gazebo/gazebo-setup.sh" >> ~/.bashrc && \
    echo "source /opt/jderobot/share/jderobot/gazebo/assets-setup.sh" >> ~/.bashrc && \
    echo "source /opt/jderobot/setup.bash" >> ~/.bashrc && \
    /bin/bash -c "source ~/.bashrc"

# Add user ubuntu with no password
RUN adduser --disabled-password --gecos '' ubuntu && \
    adduser ubuntu sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ubuntu
WORKDIR /home/ubuntu/
RUN chmod a+rwx /home/ubuntu/

USER root
COPY start.sh /root/
RUN chmod +x /root/start.sh && \
    echo 'alias jl="DISPLAY=:0 jupyter lab --no-browser --ip 0.0.0.0 --port 8888 --allow-root &"' >> /root/.bashrc && \
    echo 'alias tb="tensorboard --logdir runs --bind_all &"' >> /root/.bashrc

WORKDIR /root
CMD ["bash"]
