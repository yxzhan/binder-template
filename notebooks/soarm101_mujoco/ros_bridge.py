"""ROS 2 bridge for SOARM101 Mujoco simulation.

Subscribes to /joint_states and exposes joint positions to the simulation.
"""

import threading
from typing import Dict, Optional

try:
    import rclpy
    import rclpy.executors
    from rclpy.node import Node
    from sensor_msgs.msg import JointState
    ROS2_AVAILABLE = True
except ImportError:
    ROS2_AVAILABLE = False
    print("[ROS Bridge] rclpy not available - ROS control disabled")


if ROS2_AVAILABLE:
    class JointStateBridge(Node):
        def __init__(self) -> None:
            super().__init__("soarm101_mujoco_bridge")
            self.joint_positions: Dict[str, float] = {}
            self._lock = threading.Lock()
            self._subscription = self.create_subscription(
                JointState,
                "/joint_states",
                self._joint_state_callback,
                10,
            )
            self.get_logger().info("SOARM101 Mujoco ROS Bridge started")
            self.get_logger().info("Listening to /joint_states for joint updates")

        def _joint_state_callback(self, msg: JointState) -> None:
            with self._lock:
                for name, pos in zip(msg.name, msg.position):
                    self.joint_positions[name] = pos

        def get_joint_positions(self) -> Dict[str, float]:
            with self._lock:
                return dict(self.joint_positions)


class RosBridge:
    def __init__(self) -> None:
        if not ROS2_AVAILABLE:
            raise RuntimeError("ROS 2 is not available")
        self._node: Optional[JointStateBridge] = None
        self._executor: Optional[rclpy.executors.SingleThreadedExecutor] = None
        self._spin_thread: Optional[threading.Thread] = None
        self._running = False

    def start(self) -> None:
        rclpy.init()
        self._node = JointStateBridge()
        self._executor = rclpy.executors.SingleThreadedExecutor()
        self._executor.add_node(self._node)
        self._running = True
        self._spin_thread = threading.Thread(target=self._spin, daemon=True)
        self._spin_thread.start()

    def _spin(self) -> None:
        while self._running and rclpy.ok():  # type: ignore[attr-defined]
            if self._executor is not None:
                self._executor.spin_once(timeout_sec=0.01)

    def get_joint_positions(self) -> Dict[str, float]:
        if self._node is None:
            return {}
        return self._node.get_joint_positions()

    def stop(self) -> None:
        self._running = False
        if self._spin_thread is not None:
            self._spin_thread.join(timeout_sec=1.0)
        if self._node is not None and self._executor is not None:
            self._executor.remove_node(self._node)
            self._node.destroy_node()
        rclpy.shutdown()  # type: ignore[attr-defined]
