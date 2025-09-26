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


*************************
2025/09/19
https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Creating-an-Action.html

jerry@Latitude3520:~/Code/ros/ros2_action_ws/src$ ros2 pkg create --license Apache-2.0 custom_action_interfaces
going to create a new package
package name: custom_action_interfaces
destination directory: /home/jerry/Code/ros/ros2_action_ws/src
package format: 3
version: 0.0.0
description: TODO: Package description
maintainer: ['jerry <fmercury@naver.com>']
licenses: ['Apache-2.0']
build type: ament_cmake
dependencies: []
creating folder ./custom_action_interfaces
creating ./custom_action_interfaces/package.xml
creating source and include folder
creating folder ./custom_action_interfaces/src
creating folder ./custom_action_interfaces/include/custom_action_interfaces
creating ./custom_action_interfaces/CMakeLists.txt
jerry@Latitude3520:~/Code/ros/ros2_action_ws/src$

jerry@Latitude3520:~/Code/ros/ros2_action_ws$ colcon build
Starting >>> my_robot_interfaces
Starting >>> custom_action_interfaces
Starting >>> my_robot_tut
Finished <<< my_robot_interfaces [0.44s]                                                                             
Starting >>> actions_py
Finished <<< my_robot_tut [1.17s]                                                                                  
Finished <<< actions_py [1.12s]                                                              
Finished <<< custom_action_interfaces [5.13s]                    

Summary: 4 packages finished [5.27s]
jerry@Latitude3520:~/Code/ros/ros2_action_ws$ source install/setup.bash
jerry@Latitude3520:~/Code/ros/ros2_action_ws$ ros2 interface show custom_action_interfaces/action/Fibonacci
# Goal
int32 order
---
# Result
int32[] sequence
---
# Feedback
int32 partial_sequence
jerry@Latitude3520:~/Code/ros/ros2_action_ws$ 

https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Writing-an-Action-Server-Client/Cpp.html
https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Writing-an-Action-Server-Client/Py.html


**************************
https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Writing-a-Composable-Node.html
Writing a Composable Node (C++)


**************************
https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Monitoring-For-Parameter-Changes-Python.html
Monitoring for parameter changes (Python)

1.
ros2 pkg create --build-type ament_python --license Apache-2.0 python_parameter_event_handler --dependencies rclpy

2.
rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y

3.
colcon build --packages-select python_parameter_event_handler

jerry@Latitude3520:~/Code/ros/ros2_action_ws$ rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y
/usr/bin/rosdep:6: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import load_entry_point
ERROR: the following packages/stacks could not have their rosdep keys resolved
to system dependencies:
my_robot_tut: Cannot locate rosdep definition for [roscpp]
jerry@Latitude3520:~/Code/ros/ros2_action_ws$ colcon build --packages-select python_parameter_event_handler
Starting >>> python_parameter_event_handler
Finished <<< python_parameter_event_handler [1.08s]          

Summary: 1 package finished [1.22s]
jerry@Latitude3520:~/Code/ros/ros2_action_ws$ . install/setup.bash

4.
. install/setup.bash

5.
ros2 run python_parameter_event_handler node_with_parameters

***************************
https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Launch/Creating-Launch-Files.html

1.
cd launch

2.
ros2 launch turtlesim_mimic_launch.py

3.
ros2 topic pub -r 1 /turtlesim1/turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: -1.8}}"

4.
ros2 run rqt_graph rqt_graph


***************************
https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Launch/Launch-system.html

1.
ros2 pkg create --build-type ament_python --license Apache-2.0 py_launch_example

2.
jerry@Latitude3520:~/Code/ros/ros2_action_ws$ colcon build --packages-select py_launch_example
Starting >>> py_launch_example
Finished <<< py_launch_example [1.07s]          

Summary: 1 package finished [1.21s]
jerry@Latitude3520:~/Code/ros/ros2_action_ws$ 

3.
ros2 launch py_launch_example my_script_launch.py

***************************
https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Launch/Using-Substitutions.html

1.
ros2 launch py_launch_example example_main_launch.py

2.
ros2 launch py_launch_example example_substitutions_launch.py --show-args

jerry@Latitude3520:~/Code/ros/ros2_action_ws$ ros2 launch py_launch_example example_substitutions_launch.py --show-args
Arguments (pass arguments as '<name>:=<value>'):

    'turtlesim_ns':
        no description given
        (default: 'turtlesim1')

    'use_provided_red':
        no description given
        (default: 'False')

    'new_background_r':
        no description given
        (default: '200')
jerry@Latitude3520:~/Code/ros/ros2_action_ws$

ros2 launch launch_tutorial example_substitutions_launch.py turtlesim_ns:='turtlesim3' use_provided_red:='True' new_background_r:=200


***************************
https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Launch/Using-Event-Handlers.html

