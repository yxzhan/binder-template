# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Binder template for running robotics research Jupyter Notebooks on Binderhub. Built on a ROS 2 (Jazzy) + Python 3.12 Docker image (`intel4coro/jupyter-ros2:jazzy-py3.12`) with JupyterLab and code-server (VS Code in browser).

## Build & Run

```bash
# Build and run locally (from repo root)
docker compose -f ./binder/docker-compose.yml up --build

# Stop and remove container
docker compose -f ./binder/docker-compose.yml down

# Install Python dependencies (inside container)
pip install -r requirements.txt
```

Access JupyterLab at http://localhost:8888/ after starting.

## Architecture

- **`binder/`** — Docker environment: `Dockerfile` (base image + AI coding tools + dependencies), `docker-compose.yml` (local dev), `entrypoint.sh` (sources ROS 2 setup, runs at container start)
- **`notebooks/`** — Jupyter notebooks and Python utilities. `utils.py` provides `display_desktop()` for embedding a remote desktop viewer in JupyterLab via Sidecar widget
- **`requirements.txt`** — Python deps installed at Docker build time (ipywidgets, sidecar, matplotlib)

All development runs inside the Docker container. The entrypoint sources `${ROS_PATH}/setup.bash` for ROS 2 availability. New apt packages go in the Dockerfile; new Python packages go in `requirements.txt` (then rebuild the image).

## Code Style

- PEP 8, 4-space indentation, 100-char line limit
- Type hints on function signatures
- Google/NumPy-style docstrings
- Import order: stdlib, third-party, local (separated by blank lines)
- Naming: `snake_case` (functions/variables), `PascalCase` (classes), `UPPER_SNAKE_CASE` (constants)

## No Test Framework

No test framework is currently configured. If adding tests, use pytest.
