FROM nvidia/cudagl:10.1-devel-ubuntu18.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && apt-get -y upgrade && apt-get install -y --no-install-recommends apt-utils \
    wget curl git vim sudo firefox && \
    apt-get autoclean && apt-get autoremove

RUN apt-get update && apt-get install -y xvfb x11vnc python-opengl icewm cmake tmux

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
