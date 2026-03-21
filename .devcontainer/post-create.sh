#!/bin/bash
set -e

source /opt/ros/jazzy/setup.bash

if [ -f "/home/repo/requirements.txt" ]; then
    pip install -r /home/repo/requirements.txt
fi

echo "ROS 2 environment configured"
