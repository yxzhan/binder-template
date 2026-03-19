#!/bin/bash

# Launch the ROS2
source ${ROS_PATH}/setup.bash

# Add other startup programs here


# The following should be at the end of the entrypoint. Don't modify it!!!
exec "$@"