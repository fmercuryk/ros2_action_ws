import rclpy
from rclpy.node import Node
import rclpy.parameter

from rclpy.parameter_event_handler import ParameterEventHandler


class SampleNodeWithParameter(Node):
    def __init__(self):
        super().__init__("node_with_parameters")
        self.declare_parameter("an_int_param", 0)
        self.declare_parameter("another_double_param", 0.0)
        self.handler = ParameterEventHandler(
            self
        )  # used to monitor changes to parameters.used to monitor changes to parameters.

        self.callback_handle = self.handler.add_parameter_callback(
            parameter_name="an_int_param",
            node_name="node_with_parameters",
            callback=self.callback,
        )  # It is very important to save the handle that is returned by add_parameter_callback; otherwise, the callback will not be properly registered.

        self.callback_handle2 = self.handler.add_parameter_callback(
            parameter_name="a_double_param",
            node_name="parameter_blackboard",
            callback=self.callback,
        )

        self.event_callback_handle = self.handler.add_parameter_event_callback(
            callback=self.event_callback,
        )

    def callback(self, p: rclpy.parameter.Parameter) -> None:
        self.get_logger().info(
            f"Received and update to parameter: {p.name}: {rclpy.parameter.parameter_value_to_python(p.value)}"
        )

    """
    Note that the parameter_event is of type rcl_interfaces/msg/ParameterEvent.
    event callbacks can also be used to monitor when parameters are added or deleted.
    """

    def event_callback(self, parameter_event) -> None:
        self.get_logger().info(
            f"Received parameter event from node: {parameter_event.node}"
        )

        for p in parameter_event.changed_parameters:
            self.get_logger().info(
                f"Inside event: {p.name} changed to: {rclpy.parameter.parameter_value_to_python(p.value)}"
            )


def main():
    rclpy.init()
    node = SampleNodeWithParameter()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
