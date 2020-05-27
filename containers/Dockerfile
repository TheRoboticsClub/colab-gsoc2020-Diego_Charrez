FROM nvidia/cudagl:10.1-devel-ubuntu18.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && apt-get -y upgrade && apt-get install -y --no-install-recommends apt-utils \
    wget curl git vim sudo firefox && \
    apt-get autoclean && apt-get autoremove

RUN apt-get update && apt-get install -y xvfb x11vnc python-opengl icewm cmake tmux python3-pip
RUN pip3 install jupyterlab virtualenv

# ROS melodic
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
RUN apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
RUN apt update
RUN apt install -y --no-install-recommends ros-melodic-desktop-full

# Jderobot base and assets
RUN sh -c 'echo "deb [arch=amd64] http://wiki.jderobot.org/apt `lsb_release -cs` main" > /etc/apt/sources.list.d/jderobot.list'
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 24E521A4
RUN apt update
RUN apt install -y --no-install-recommends jderobot
RUN apt install -y --no-install-recommends jderobot-assets
RUN apt install -y --no-install-recommends ros-melodic-jderobot-assets
RUN echo "source /opt/jderobot/share/jderobot/gazebo/gazebo-setup.sh" >> ~/.bashrc
RUN echo "source /opt/jderobot/share/jderobot/gazebo/assets-setup.sh" >> ~/.bashrc
RUN echo "source /opt/jderobot/setup.bash" >> ~/.bashrc 
RUN source ~/.bashrc

COPY start.sh /root/
RUN chmod +x /root/start.sh

# Add user ubuntu with no password, add to sudo group
RUN adduser --disabled-password --gecos '' ubuntu
RUN adduser ubuntu sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ubuntu
WORKDIR /home/ubuntu/
RUN chmod a+rwx /home/ubuntu/

USER root

RUN echo 'alias jl="DISPLAY=:0 jupyter lab --no-browser --ip 0.0.0.0 --port 8888 --allow-root &"' >> /root/.bashrc && \
    echo 'alias tb="tensorboard --logdir runs --bind_all &"' >> /root/.bashrc

WORKDIR /root
CMD ["bash"]
