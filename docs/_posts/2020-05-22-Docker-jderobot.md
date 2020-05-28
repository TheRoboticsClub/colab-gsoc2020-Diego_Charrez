---
title: "Dockerfile for Jderobot"
excerpt: ""

sidebar:
  nav: "docs"

toc: true
toc_label: "TOC installation"
toc_icon: "cog"


categories:
- GSoC
tags:
- Jderobot

author: Diego Charrez
pinned: false
---

# Objectives

- Build a Dockerfile to run my experiments.
- Follow good practices for Docker.
- Test Dockerfile.

## Docker

Docker is a platform for developers which make applications easy to share and deploy. Using Docker containers are self-sufficient and can be run in natively on Linux, Moreover, containers are lightweight compared with virtual machines since containers share the kernel of the host machine, unlike virtual machines that brings its own operating system [\[3\]](https://docs.docker.com/get-started/).

{% capture fig_img %}
![Foo]({{ "/assets/images/blogs/containers.png" | relative_url }})
{% endcapture %}

<figure>
  {{ fig_img | markdownify | remove: "<p>" | remove: "</p>" }}
  <figcaption>Figure from Docker Docs</figcaption>
</figure>

## Dockerfile

These are some parts of the Dockerfile that I will be using for now, it is going to be updated as the projects is developed. Some good practices that I followed from 
[\[2\]](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) [\[1\]](https://dev.to/azure/improve-your-dockerfile-best-practices-5ll) reducing the number of layers (represent docker instructions) by lowering the number of instructions that create layers like `RUN`, `COPY` and `ADD`. 

```docker
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
    source ~/.bashrc
```

Also Sorting multi-line arguments helps to easily manage your packages.

```docker
RUN apt-get update -y && apt-get -y upgrade && apt-get install -y --no-install-recommends \
        apt-utils \
        cmake \
        curl \
        firefox \
        git \
        icewm \
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
```

The full Dockerfile that I will be using can be found [here](https://github.com/TheRoboticsClub/colab-gsoc2020-Diego_Charrez/blob/master/containers/Dockerfile).


## Commands

### For building a Dockerfile

```bash
docker build -t example .
```

## References

[1] Dev Community, [Improve your Dockerfile, best practices](https://dev.to/azure/improve-your-dockerfile-best-practices-5ll)

[2] Docker Docs, [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

[3] Docker Docs, [Getting started](https://docs.docker.com/get-started/)
