#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class CustomNode(Node):
    def __init__(self):
        super().__init__("custom_node")
        self.get_logger().info("Custom Node has been initialized")


def main(args=None):
    rclpy.init(args=args)
    node = CustomNode()
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
