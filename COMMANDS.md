https://www.youtube.com/watch?v=X7YSnDbKMWo

colcon build --packages-select my_robot_interfaces
source install/setup.bash

ros2 interface show my_robot_interfaces/action/CountUntil
jerry@Latitude3520:~/Code/ros/ros2_action_ws$ ros2 interface show my_robot_interfaces/action/CountUntil
# Goal
int64 target_number
float64 period
---
# Result
int64 reached_number
---
# Feedback
int64 current_number

jerry@Latitude3520:~/Code/ros/ros2_action_ws/src$ ros2 pkg create actions_py --build-type ament_python --dependencies rclpy my_robot_interfaces

jerry@Latitude3520:~/Code/ros/ros2_action_ws/src/actions_py/actions_py$ touch count_until_server.py

jerry@Latitude3520:~/Code/ros/ros2_action_ws/src$ colcon build --packages-select actions_py --symlink-install
Starting >>> actions_py
Finished <<< actions_py [1.29s]          

Summary: 1 package finished [1.45s]
jerry@Latitude3520:~/Code/ros/ros2_action_ws/src$ 


*********************
2025/09/16

jerry@Latitude3520:~/Code/ros/ros2_action_ws/src$ ros2 pkg create my_robot_tut --build-type ament_python --dependencies rclpy roscpp std_msgs
jerry@Latitude3520:~/Code/ros/ros2_action_ws$ colcon build
Starting >>> my_robot_interfaces
Starting >>> my_robot_tut
Finished <<< my_robot_tut [1.17s]                                          
Finished <<< my_robot_interfaces [3.95s]                    
Starting >>> actions_py
Finished <<< actions_py [1.47s]          

Summary: 3 packages finished [5.56s]
jerry@Latitude3520:~/Code/ros/ros2_action_ws$

jerry@Latitude3520:~/Code/ros/ros2_action_ws/src/my_robot_tut$ mkdir scripts
jerry@Latitude3520:~/Code/ros/ros2_action_ws/src/my_robot_tut$ cd scripts/
jerry@Latitude3520:~/Code/ros/ros2_action_ws/src/my_robot_tut/scripts$ touch count_until_server.py
jerry@Latitude3520:~/Code/ros/ros2_action_ws/src/my_robot_tut/scripts$ chmod +x count_until_server.py


