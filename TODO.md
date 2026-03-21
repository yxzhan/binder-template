# SOARM101 Mujoco Simulation - TODO

## 1. Fix Mujoco Demo Issues
- [ ] Mujoco viewer sometimes can't be killed (process lingers)
- [ ] Pick and place scene: object positions don't match physical setup
- [ ] Mechanical arm self-collision needs to be resolved

## 2. Test Bambot Calibration
- [ ] After switching URDF, verify calibration works on physical robot
- [ ] Compare joint angles between Mujoco simulation and real hardware

## 3. Fix Bambot Export Build
- [ ] Resolve `bambot/website` build/export failure

## 4. Implement Joint States Broadcast
- [ ] Main arm (非夹爪) publishes `/joint_states` for state monitoring

## 5. Design Three Modes
- [ ] **Real Data Collection**: Record demonstrations from physical robot
- [ ] **Sim Data Collection**: Record demonstrations from Mujoco simulation
- [ ] **Policy Control**: Deploy trained policy to control physical robot

## 6. Implement Camera Feature
- [ ] Integrate camera feed into JupyterLab/Mujoco viewer
- [ ] Support real-time visual feedback during teleoperation
