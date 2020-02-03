# Obstacle_avoidance_randomwalk
GAZEBO simulation of a differential drive robot which performs obstacle avoidance and randomly navigates in a closed environment

## Prerequisites
The following software packages need to be installed before preceeding with this demo. The setup is installed on Ubuntu 18.04 and ROS-Melodic

Initialize a catkin workspace
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```

## Running the code
Download the repository and build it.
```
cd ~/catkin_ws
catkin_make
source devel/setup.bash
cd src/
git clone https://github.com/kartiksonu/Obstacle_avoidance_randomwalk.git 
cd ..
catkin_make
```
## Running the simulation
To simulate in Gazebo:

```
cd ~/catkin_ws
roslaunch mybot_gazebo mybot_world.launch
```
In a new terminal

```
cd ~/catkin_ws/src/mybot_ws/src/scripts
chmod +x random_walk.py
python random_walk.py

```
Now you should be able to see the robot moving inside the simulator.

Press ctrl+c to quit the simulation.

## Observing topics in ROS
To view the topics that are being published use
```
rostopic list
```
To print the messages published on a topic
```
rostopic echo /TOPIC_NAME
```
