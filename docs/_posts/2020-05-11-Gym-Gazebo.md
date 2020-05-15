---
title: "Gym and Gazebo at Behaviour Suite"
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

# Definitions

### OpenAI Gym

OpenAI Gym is a framework to test and developed reinforcement learning algorithms, it includes many environments like the Atari games.

![CarRacing]({{ "/assets/images/blogs/CarRacing-v0.gif" | absolute_url }})

### Gazebo

Is an open-source 3D robotics simulator.

### Behaviour Studio

Is a tool that will benchmark different algorithms for autonomous driving using Jderobot tools.

# Using Behaviour Studio, Gym and Gazebo

I used the [installation guide](https://github.com/RoboticsLabURJC/2019-tfm-ignacio-arranz/tree/master/gym-gazebo) from Ignacio Arranz's master thesis [repository](https://github.com/RoboticsLabURJC/2019-tfm-ignacio-arranz) 

### Installation

#### ROS Melodic and Gazebo 9.0 in Ubuntu 18.04

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-melodic-desktop-full
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

TODO

## References

[1] Greg Brockman, et al. ["OpenAI Gym"](https://gym.openai.com/) 2016.

[2] Andrew Howard, et al. ["Gazebo"](http://gazebosim.org/) 2002 at the University of Southern California.

[3] Jderobot, [BehaviorStudio (BehaviorSuite)](https://github.com/JdeRobot/BehaviorSuite)

[4] Nacho Arranz’s master thesis [repository](https://github.com/RoboticsLabURJC/2019-tfm-ignacio-arranz) 

[5] [Gym-gazebo](https://github.com/RoboticsLabURJC/2019-tfm-ignacio-arranz/blob/master/gym-gazebo/README.md)
