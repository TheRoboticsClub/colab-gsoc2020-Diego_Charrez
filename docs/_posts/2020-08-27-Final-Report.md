---
title: "Final Report"
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

## Summary

JdeRobot provides a set of tools for developing robotic applications, including previous work in autonomous driving robots that use algorithms like a classification neural networks or regression neural networks, Therefore one of the main goals of this project is to combine OpenAI Gym and Gazebo to use Reinforcement learning in the current Behavior Studio setup. This involved to migrate previous code to work with python3. 

During this project I extended the support of Jderobot's behavior studio to ROS-noetic, and upgraded previous gym gazebo library to work accordingly to the new version of python3 and ubuntu 20.04. Moreover, I adapted the current GUI to work with Reinforcement Learning algorithms.

## Contributions

One of my early contribution was to make a sort of template to run Q-learning algorithm with OpenAI gym environments, like cartpole and breakout. For this task I created and documented a docker container to ease the reproducibility of the experiments, the containers were tested using GPUs in a notebook which later was modularized in python scripts. 

![Breakout]({{ "/assets/images/blogs/8m_breakout_256.gif" | absolute_url }})

Behavior Studio at first had support for python 2.7, and the ROS-noetic which had support for python3 was released recently it presented a great opportunity to migrate the project to python3 and use ROS-noetic directly.

I completed the refactoring to extend the support for python3 and tested it with the behavior studio GUI as is shown in the following figurem which displays the behavior studio GUI within the docker container through the VNC viewer.

{% capture fig_img %}
![Foo]({{ "/assets/images/blogs/behavior_studio_gui.png" | relative_url }})
{% endcapture %}

<figure>
  {{ fig_img | markdownify | remove: "<p>" | remove: "</p>" }}
  <figcaption>Behavior Studio GUI displayed inside container through VNC</figcaption>
</figure>

When the project began the Gym-Gazebo library only worked for ubuntu 18.04 and ROS-melodic, hence more refactoring was done to migrate this library to Ubuntu Focal Fossa with ROS-noetic due that this library is a key part in order to enable the reinforcement learning experimentation within Behavior Studio.

![Turtlebot]({{ "/assets/images/blogs/Turtlebot.gif" | absolute_url }})

Since the project was growing in dependencies it was necessary to make this available for others to use through the [Jderobot's docker hub](https://hub.docker.com/r/jderobot/behavior-studio), multiple images were created and maintained as new changes were added to the project. I added the respective guides and tutorials to use the docker images and also I posted the user manual including the installation steps for the ROS-noetic behavior studio.

{% capture fig_img %}
![Foo]({{ "/assets/images/blogs/vnc-behavior-studio.png" | relative_url }})
{% endcapture %}

As Ubuntu 20.04 support gazebo 11, formula 1 plugins were migrated to support this new version, which were added to the CustomRobot repository. although later on was decided to try to mostly use official ROS-plugins.

After the migration of the gym-gazebo library, behavior studio and other dependencies was done, I had the path clear to implement the Reinforcement learning support in behavior studio considering that it only worked with Brains with deep learning or opencv.

<figure>
  {{ fig_img | markdownify | remove: "<p>" | remove: "</p>" }}
  <figcaption>Behavior Studio with Reinforcement Learning displayed inside container through VNC</figcaption>
</figure>

In the last weeks the Behavior Studio GUI supported RL brains, using q-learning in the formula 1 circuit, here is a video how the training looks like inside a container which allow to do training in headless remote servers, using different host opearting systems.

{% include video id="OHEb_6hXugs" provider="youtube" %}

It was also added more documentation about the how the brains work and how one could setup different training parameters from the launch file that the Behavior studio GUI consumes.


```yml
BrainPath: 'brains/f1rl/train.py'
Type: 'f1rl'
Parameters:
    action_set: 'simple'
    gazebo_positions_set: 'pista_simple'
    alpha: 0.2 
    gamma: 0.9
    epsilon: 0.99
    total_episodes: 20000
    epsilon_discount: 0.9986 
    env: 'camera'
```    

## Difficulties

Most difficulties happen because I was not related to some existing code or I was not sure which approach to take to solve a problem since there were many options.

Moreover there were other difficulties related to the project itself, like some unexpected crashes, and code compatibility. This project needs a set of requirements that ensure the correct functionality of the behavior studio tool to mitigate this I develop a set of containers that already include those requirements that also helps new users to easily begin using this tool.

## Improved skills

Working in this project helped me learn new skills, and reinforce previous concepts. This was a great opportunity to delve into new problems which gave the opportunity to grasp new technologies and tools like docker, ros-noetic, pyqt, and improve cmake skills.

Overall I also gained more experience reading code from other contributors, since this is essential to keep contributing this and other open source projects.

## Summary of contributions to Jderobot

### Jderobot base

- [Missing libraries in the README for source installation.](https://github.com/JdeRobot/base/issues/1398)
- [Upgrade to Ubuntu 20.04 Focal Fossa](https://github.com/JdeRobot/base/issues/1396)
- [Added missing libraries to README and corrected typos](https://github.com/JdeRobot/base/pull/1399)

### Jderobot custom robots

- [[Models] ROS Noetic Support for F1](https://github.com/JdeRobot/CustomRobots/issues/9)
- [Addressing Issue #9](https://github.com/JdeRobot/CustomRobots/pull/12)

### Jderobot Academy

- [Adding environment setup instructions for both base and assets](https://github.com/JdeRobot/RoboticsAcademy/pull/497)
- [Adding environment setup in the installation page](https://github.com/JdeRobot/RoboticsAcademy/pull/495)
- [Corrected some typos in the AutonomousCars guide](https://github.com/JdeRobot/RoboticsAcademy/pull/482)

### Jderobot Behavior Studio

- [No module named PyQt5.QtWidgets (python2.7)](https://github.com/JdeRobot/BehaviorStudio/issues/24)
- [Core dump when loading a brain which saved model cannot be found.](https://github.com/JdeRobot/BehaviorStudio/issues/54)
- [Update noetic installation guide to support python3.7](https://github.com/JdeRobot/BehaviorStudio/issues/58)
- [Gym Gazebo for noetic](https://github.com/JdeRobot/BehaviorStudio/issues/60)
- [[noetic-devel] Error message in logs while using gazebo and behavior studio in docker container](https://github.com/JdeRobot/BehaviorStudio/issues/64)
- [[noetic-devel] Add docker image with CUDA 11 in ubuntu 20.04](https://github.com/JdeRobot/BehaviorStudio/issues/65)
- [[Noetic-devel] Improve Dockerfiles documentation](https://github.com/JdeRobot/BehaviorStudio/issues/68)
- [[Noetic-devel] Setting hyperparameters from config.yml](https://github.com/JdeRobot/BehaviorStudio/issues/69)
- [[noetic-devel] update dqn code](https://github.com/JdeRobot/BehaviorStudio/issues/70)
- [[noetic-devel] Update Dockerfiles to use Jderobot's Behavior studio directly](https://github.com/JdeRobot/BehaviorStudio/issues/72)
- [Noetic devel](https://github.com/JdeRobot/BehaviorStudio/pull/53)
- [Upgrading brains to Python3](https://github.com/JdeRobot/BehaviorStudio/pull/55)
- [adding installation guide for noetic-devel branch](https://github.com/JdeRobot/BehaviorStudio/pull/57)
- [Adding virtualenv](https://github.com/JdeRobot/BehaviorStudio/pull/59)
- [Gym gazebo for noetic](https://github.com/JdeRobot/BehaviorStudio/pull/61)
- [Adding support for RL](https://github.com/JdeRobot/BehaviorStudio/pull/62)
- [Issue 64](https://github.com/JdeRobot/BehaviorStudio/pull/66)
- [New image with CUDA11 in ubuntu focal](https://github.com/JdeRobot/BehaviorStudio/pull/67)
- [minor changes for qlearn](https://github.com/JdeRobot/BehaviorStudio/pull/71)
- [Updating all dockerfiles with behavior studio repository](https://github.com/JdeRobot/BehaviorStudio/pull/73)
- [Issue 69](https://github.com/JdeRobot/BehaviorStudio/pull/74)
- [updating documentation for rl](https://github.com/JdeRobot/BehaviorStudio/pull/75)


## Further work

There is still a lot of work to be done and Behavior Studio is a new project that is very exciting, hence I will try my best to keep contributing regularly to Behavior Studio.

I would like to keep adding new Reinforcement Learning algorithms and add new environments to make the platform more diverse, currently only line following is working, so it would be interesting to have a obstacles in the environment those obstacles could be dynamic or static, and just like that there are many good direction for this project.

## Acknowledgment

Taking part in this GSOC was a wonderful experience and I want to particularly thank my mentors Sergio, David and the Behavior Studio team for their helpful advises, discussions and support. I learned lots new things and deepen my knowledge in robotics, thanks to the Jderobot for giving me this opportunity to learn more about the organization and letting me contribute to this project.

# References

* [1] Jderobot, [BehaviorStudio (BehaviorSuite)](https://github.com/JdeRobot/BehaviorStudio/tree/reboot)