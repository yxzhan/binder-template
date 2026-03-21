#!/bin/bash

source /opt/ros/jazzy/setup.bash

if ! pgrep -x "rosbridge" > /dev/null; then
    ros2 launch rosbridge_server rosbridge_websocket_launch.xml &
    echo "ROS Bridge started"
fi

echo "Dev container attached"
