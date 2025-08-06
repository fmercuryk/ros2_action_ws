#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.action import CountUntil
from rclpy.action import ActionClient
from rclpy.action.server import ServerGoalHandle


class CountUntilCount(Node):
    def __init__(self):
        super().__init__("count_until_count")
        self.get_logger().info("Custom Node has been initialized")
        self.action_client = ActionClient(
            node=self,
            action_type=CountUntil,
            action_name="count_until",
        )

    def send_goal(self, target_number, perood):
        pass
        # wait for the action server to be available
        self.action_client.wait_for_server()

        # create a goal
        goal = CountUntil.Goal()
        goal.target_number = target_number
        goal.period = perood

        # send the goal
        self.get_logger().info(
            f"Sending goal: target_number={target_number}, period={perood}"
        )
        self.action_client.send_goal_async(goal)


def main(args=None):
    rclpy.init(args=args)
    node = CountUntilCount()
    node.send_goal(10, 1.0)
    node.get_logger().info("Custom Node is running")

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down Custom Node")
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
