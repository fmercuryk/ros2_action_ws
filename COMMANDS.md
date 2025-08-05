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

