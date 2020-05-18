---
title: "Gym and Gazebo"
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

## OpenAI Gym

OpenAI Gym is a framework to test and developed reinforcement learning algorithms, it includes many environments like the Atari games [\[1\]](https://gym.openai.com/).

![CarRacing]({{ "/assets/images/blogs/CarRacing-v0.gif" | absolute_url }})

## Gazebo

Is an open-source 3D robotics simulator, and it is integrated with ROS [\[2\]](http://gazebosim.org/) .

## Behaviour Studio

Is a tool that will benchmark different algorithms for autonomous driving using Jderobot tools [\[3\]](https://github.com/JdeRobot/BehaviorSuite).

# Using Behaviour Studio, Gym and Gazebo

I used the [installation guide](https://github.com/RoboticsLabURJC/2019-tfm-ignacio-arranz/tree/master/gym-gazebo) from Ignacio Arranz's master thesis [repository](https://github.com/RoboticsLabURJC/2019-tfm-ignacio-arranz). I only pasted here the installation commands, there are more for display and running environments in the Ignacio's  repository I mentioned before [\[5\]](https://github.com/RoboticsLabURJC/2019-tfm-ignacio-arranz/blob/master/gym-gazebo/README.md).

## Installation

### ROS Melodic and Gazebo 9.0 in Ubuntu 18.04
[ROS wiki](http://wiki.ros.org/melodic/Installation/Ubuntu)
```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-melodic-desktop-full
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
### Gym-Gazebo

```bash
git clone https://github.com/RoboticsLabURJC/2019-tfm-ignacio-arranz
cd 2019-tfm-ignacio-arranz/gym-gazebo
pip3 install -r requirements.txt
pip3 install -e .
```

Adding more packages needed

```bash
sudo apt-get install                     \
python-pip python3-vcstool python3-pyqt4 \
pyqt5-dev-tools                          \
libbluetooth-dev libspnav-dev            \
pyqt4-dev-tools libcwiid-dev             \
cmake gcc g++ qt4-qmake libqt4-dev       \
libusb-dev libftdi-dev                   \
python3-defusedxml python3-vcstool       \
ros-melodic-octomap-msgs                 \
ros-melodic-joy                          \
ros-melodic-geodesy                      \
ros-melodic-octomap-ros                  \
ros-melodic-control-toolbox              \
ros-melodic-pluginlib	                 \
ros-melodic-trajectory-msgs              \
ros-melodic-control-msgs                 \
ros-melodic-std-srvs 	                 \
ros-melodic-nodelet                      \
ros-melodic-urdf                         \
ros-melodic-rviz                         \
ros-melodic-kdl-conversions              \
ros-melodic-eigen-conversions            \
ros-melodic-tf2-sensor-msgs              \
ros-melodic-pcl-ros                      \
ros-melodic-navigation                   \
ros-melodic-sophus                       \
python-rviz
```

### Problems encountered

#### Python

I got this error, because my tf2_ros was working with python2

```bash
ImportError: dynamic module does not define module export function (PyInit__tf2)
```

I tried many possible solutions like these.

[Attempted solution](https://answers.ros.org/question/326226/importerror-dynamic-module-does-not-define-module-export-function-pyinit__tf2/)

Then reading other solutions I found out that my problem might have been caused because I was using conda, so I did a clean docker installation and it worked!.


#### Environment variables

Loading the environment variables returned this message

```bash
bash formula1_setup.bash
cp: cannot stat '../assets/urdf/kobuki_nn_urdf/urdf/': No such file or directory                       
cp: cannot stat '../assets/meshes/lidar_lite_v2_withRay.dae': No such file or directory
```

I found the missing files in the [gym-gazebo repo](https://github.com/erlerobot/gym-gazebo/tree/master/gym_gazebo/envs/assets) from erlerobot, so I copied to the Ignacio's repo and the bash ran correctly now.

```bash
git clone https://github.com/erlerobot/gym-gazebo
cp -r gym-gazebo/gym_gazebo/envs/assets/meshes/ 2019-tfm-ignacio-arranz/gym-gazebo/gym-gazebo/envs/assets/
cp -r gym-gazebo/gym_gazebo/envs/assets/urdf/ 2019-tfm-ignacio-arranz/gym-gazebo/gym-gazebo/envs/assets/
```



### Running
```bash
cd gym_gazebo/envs/installation
bash setup_melodic.bash
bash turtlebot_setup.bash
```

```bash
cd agents/turtlebot
python3 circuit2_turtlebot_lidar_qlearn.py
```

![Turtlebot]({{ "/assets/images/blogs/Turtlebot.gif" | absolute_url }})

## References

[1] Greg Brockman, et al. ["OpenAI Gym"](https://gym.openai.com/) 2016.

[2] Andrew Howard, et al. ["Gazebo"](http://gazebosim.org/) 2002 at the University of Southern California.

[3] Jderobot, [BehaviorStudio (BehaviorSuite)](https://github.com/JdeRobot/BehaviorSuite)

[4] Nacho Arranz’s master thesis [repository](https://github.com/RoboticsLabURJC/2019-tfm-ignacio-arranz) 

[5] [Gym-gazebo](https://github.com/RoboticsLabURJC/2019-tfm-ignacio-arranz/blob/master/gym-gazebo/README.md)

