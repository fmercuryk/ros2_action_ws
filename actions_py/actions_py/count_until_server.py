#!/usr/bin/env python3

import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
from my_robot_interfaces.action import CountUntil


class CountUntilServer(Node):
    def __init__(self):
        super().__init__("count_until_server")
        self.count_until_server_ = ActionServer(
            node=self,
            action_type=CountUntil,
            action_name="count_until",
            execute_callback=self.execute_callback,
        )
        self.get_logger().info("Count Until Server has been initialized")

    def execute_callback(self, goal_handle: ServerGoalHandle):
        # get request from goal
        target_number = goal_handle.request.target_number
        period = goal_handle.request.period

        # execute the action
        self.get_logger().info(f"executing the goal")
        counter = 0
        for i in range(target_number):
            counter += 1
            self.get_logger().info(f"Count: {counter}")
            time.sleep(period)

        # set the result
        goal_handle.succeed()

        # create the result message
        result = CountUntil.Result()
        result.reached_number = counter

        return result

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
