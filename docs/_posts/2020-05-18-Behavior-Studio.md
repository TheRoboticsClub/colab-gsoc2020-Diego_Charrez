---
title: "Behavior Studio"
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

# Objetives

- Get more familiar with Behavior Studio.
- Write concepts related to Behavior Studio.
- Install Behavior Studio.
- Try some examples from Behavior Studio

Behavior Studio is a set of tools written in python that uses the JdeRobot toolkit for comparing different autonomous driving networks [\[1\]](https://github.com/JdeRobot/BehaviorStudio/tree/reboot).

## Jderobot Base

The Jderobot Base repository maintains the open source code implementation of the Jderobot toolkit that contains many tools and libraries to bring hardware abstraction, develop computer vision and many more. [\[2\]](https://github.com/JdeRobot/base).

## Jderobot Assets

This Jderobot Assets provides all the necessary worlds and models needed by the examples and exercises from Jderobot toolkit [\[3\]](https://github.com/JdeRobot/assets).

## Installation 

Behavior Studio uses the Jderobot's base and assets which can be installed following this [instructions](https://github.com/JdeRobot/base#getting-environment-ready).

### ROS and Gazebo

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-melodic-desktop-full

```

### Jderobot base and assets

```bash
sudo sh -c 'echo "deb [arch=amd64] http://wiki.jderobot.org/apt `lsb_release -cs` main" > /etc/apt/sources.list.d/jderobot.list'
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 24E521A4
sudo apt update
sudo apt install jderobot
sudo apt install jderobot-assets
sudo apt install ros-melodic-jderobot-assets
echo "source /opt/jderobot/share/jderobot/gazebo/gazebo-setup.sh" >> ~/.bashrc
echo "source /opt/jderobot/share/jderobot/gazebo/assets-setup.sh" >> ~/.bashrc
echo "source /opt/jderobot/setup.bash" >> ~/.bashrc 
source ~/.bashrc
```

### Behavior Studio

```bash
pip install virtualenv
virtualenv -p python3 bstudio_env
source bstudio_env/bin/activate
git clone -b reboot https://github.com/JdeRobot/BehaviorStudio
cd BehaviorStudio
pip install -r requirements.txt
```

### Problems encountered

The `logger.py` could not import colors.

```bash 
$ python driver.py
Traceback (most recent call last):
  File "driver.py", line 22, in <module>
    from pilot import Pilot
  File "/root/BehaviorStudio/behavior_suite/pilot.py", line 22, in <module>
    from utils.logger import logger
  File "/root/BehaviorStudio/behavior_suite/utils/logger.py", line 5, in <module>
    from colors import Colors
ModuleNotFoundError: No module named 'colors'
```

Adding `utils.` in the import of colors fixed the problem for me.

```python
from colors import Colors
from utils.colors import Colors
```


## Examples

In progress ...

## References

[1] Jderobot, [BehaviorStudio (BehaviorSuite)](https://github.com/JdeRobot/BehaviorStudio/tree/reboot)

[2] Jderobot, [Base](https://github.com/JdeRobot/base)

[3] Jderobot, [Assets](https://github.com/JdeRobot/assets)
