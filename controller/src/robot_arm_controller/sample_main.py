from robot_arm_controller.control.arm_kinematics import ArmParameters
from robot_arm_controller.controller import ArmController, Settings
from robot_arm_controller.utils.prints import disable_console,console

import time

EPSILON = 0.01


    # Arm parameters
arm_params: ArmParameters = ArmParameters()
arm_params.a2x = 0
arm_params.a2z = 172.48

arm_params.a3z = 173.5

arm_params.a4z = 0
arm_params.a4x = 126.2

arm_params.a5x = 64.1
arm_params.a6x = 169

controller = ArmController(arm_parameters=arm_params)
controller.start(websocket_server=False)


start_time = time.time()
while not controller.is_ready:
    time.sleep(0.1)
    if time.time() - start_time > 3:
        raise TimeoutError("Controller took too long to start")

controller.set_setting_joints(Settings.STEPS_PER_REV_MOTOR_AXIS, 400)
controller.home()
