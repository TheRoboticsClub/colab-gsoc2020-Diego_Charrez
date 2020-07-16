---
permalink: /install/

title: "Installation and use"

sidebar:
  nav: "docs"
---

Installing gym gazebo for ubuntu 20.04.

# Requisites

- Ubuntu 20.04 (Focal Fossa)
- ROS Noetic
- Gazebo 11

# Install dependencies

```bash
apt-get install \
python3-vcstool python3-pyqt5 python3-skimage \
pyqt5-dev-tools libcwiid-dev python3-rviz \
libbluetooth-dev libspnav-dev \
cmake gcc g++ qt5-qmake \
libusb-dev libftdi-dev libsdl-dev \
python3-defusedxml libsdl-image1.2-dev \
ros-noetic-octomap-msgs        \
ros-noetic-geodesy             \
ros-noetic-octomap-ros         \
ros-noetic-control-toolbox     \
ros-noetic-pluginlib	       \
ros-noetic-trajectory-msgs     \
ros-noetic-control-msgs	       \
ros-noetic-std-srvs 	       \
ros-noetic-nodelet	       \
ros-noetic-urdf		       \
ros-noetic-rviz		       \
ros-noetic-kdl-conversions     \
ros-noetic-eigen-conversions   \
ros-noetic-tf2-sensor-msgs     \
ros-noetic-pcl-ros \
ros-noetic-navigation 
```

```bash
git clone https://github.com/strasdat/Sophus
cd Sophus && mkdir build && cd build
cmake ../ && make && make install
```

# Install Gym-Gazebo

```bash
virtualenv -p python3.7 gazebo-gym
source gazebo-gym/bin/activate
git clone https://github.com/RoboticsLabURJC/2019-tfm-ignacio-arranz
cd 2019-tfm-ignacio-arranz/gym-gazebo
pip install -r requirements.txt
pip install -e .
```

# Usage

```bash
cd gym_gazebo/envs/installation
bash setup_noetic.bash
bash 
```