#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer

from my_robot_interfaces.action import CountUntil

# from my_robot_interfaces.action import CountUntilGoal
# from my_robot_interfaces.action import CountUntilResult


class CountUntilServer(Node):
    def __init__(self):
        self._as = ActionServer(
            "/count_until",
            CountUntil,
            execute_cb=self.on_goal,
            auto_start=False,
        )
        self._as.start()

        self._counter = 0
        rclpy.loginfo("action server has been started")

    def on_goal(self, goal):
        rclpy.loginfo("a goal has been received")
        rclpy.loginfo(f"goal: {goal}")

        target_number = goal.target_number
        period = goal.period

        self._counter = 0
        rate = rclpy.Rate(1.0 / period)

        while self._counter < target_number:
            self._counter += 1
            rate.sleep()

        # result = CountUntilResult()
        # result.count = self._counter
        # self._as.set_succeeded(result)


def main():
    rclpy.init()
    node = CountUntilServer()
    node.get_logger().info("Count Until Server is running")

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down Count Until Server")
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
