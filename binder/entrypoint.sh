#!/bin/bash

# Launch the ROS2
source ${ROS_PATH}/setup.bash

# Add other startup programs here
ros2 launch rosbridge_server rosbridge_websocket_launch.xml &

# The following should be at the end of the entrypoint. Don't modify it!!!
exec "$@"