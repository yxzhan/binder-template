# ROS 2 Bridge (rosbridge_suite)

rosbridge provides a WebSocket interface to ROS 2, allowing non-ROS programs (web browsers, Python scripts, etc.) to publish/subscribe to topics, call services, and interact with the ROS graph via a JSON API over WebSocket.

- **WebSocket port:** `9090`
- **Protocol:** [rosbridge v2.0](https://github.com/RobotWebTools/rosbridge_suite/blob/ros2/ROSBRIDGE_PROTOCOL.md)

---

## Installation

The base image (`intel4coro/jupyter-ros2:jazzy-py3.12`) does not include rosbridge by default. Two steps are required: installing the ROS apt package and installing its Python dependencies into the conda environment.

### 1. Install the apt package

```bash
sudo apt-get update
sudo apt-get install -y ros-jazzy-rosbridge-suite
```

This installs `rosbridge_suite` v2.4+ along with `rosapi` and `rosbridge_server`.

### 2. Install Python dependencies

The conda Python environment used in this image is separate from the system Python, so rosbridge's Python dependencies must be installed via pip:

```bash
pip install pymongo cbor2 ujson tornado
```

| Package   | Purpose                                      |
|-----------|----------------------------------------------|
| `pymongo` | Provides the `bson` module for binary data   |
| `cbor2`   | CBOR encoding support for outgoing messages  |
| `ujson`   | Fast JSON serialisation                      |
| `tornado` | Async WebSocket server framework             |

### Permanent installation (Dockerfile)

To bake rosbridge into the Docker image, add the following to `binder/Dockerfile` and the pip packages to `requirements.txt`:

**`binder/Dockerfile`**
```dockerfile
RUN apt-get update && apt-get install -y ros-jazzy-rosbridge-suite
```

**`requirements.txt`**
```
pymongo
cbor2
ujson
tornado
```

---

## Starting the server

Source the ROS 2 environment and launch the WebSocket server:

```bash
source /opt/ros/jazzy/setup.bash
ros2 launch rosbridge_server rosbridge_websocket_launch.xml
```

Expected output:

```
[INFO] [rosbridge_websocket]: Rosbridge WebSocket server started on port 9090
```

### Run in the background

```bash
source /opt/ros/jazzy/setup.bash
ros2 launch rosbridge_server rosbridge_websocket_launch.xml &
```

### Run with a custom port

```bash
ros2 launch rosbridge_server rosbridge_websocket_launch.xml port:=9091
```

### Stop the server

```bash
pkill -f rosbridge_websocket
```

---

## Connecting to the server

Once running, connect to `ws://localhost:9090` from any WebSocket client.

**Example using `roslibjs` in the browser:**

```javascript
const ros = new ROSLIB.Ros({ url: 'ws://localhost:9090' });
ros.on('connection', () => console.log('Connected to rosbridge'));
```

**Example using `roslibpy` in Python:**

```python
import roslibpy

client = roslibpy.Ros(host='localhost', port=9090)
client.run()
print('Connected:', client.is_connected)
```

---

## Verify the server is running

Check that port 9090 is bound:

```bash
ss -tlnp | grep 9090
```

Check that the ROS node is active:

```bash
source /opt/ros/jazzy/setup.bash
ros2 node list | grep rosbridge
```
