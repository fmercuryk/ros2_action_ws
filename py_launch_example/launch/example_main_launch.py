from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    colors = {"background_r": "200"}

    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PathJoinSubstitution(
                    [
                        FindPackageShare("py_launch_example"),
                        "launch",
                        "example_substitutions_launch.py",
                    ]
                ),
                launch_arguments={
                    "turtlesim_ns": "turtlesim2",
                    "use_provided_red": "True",
                    "new_background_r": colors["background_r"],
                }.items(),
            )
        ]
    )
