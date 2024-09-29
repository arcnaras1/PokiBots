from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, multitask, run_task
# Set up all devices.
prime_hub = PrimeHub()
left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right = Motor(Port.E, Direction.CLOCKWISE)
attach = Motor(Port.A)
drive_base = DriveBase(left, right, 56, 130)

async def timeout_motor(motor: Motor, speed, degrees, stop_type):
    await multitask(motor.run_angle(speed, degrees, stop_type), wait(2000), race=True)

def configure():
    drive_base.settings(straight_speed=350)
    drive_base.settings(straight_acceleration=150)
    drive_base.settings(turn_rate=700)
    drive_base.settings(turn_acceleration=400)
    drive_base.use_gyro(True)
    drive_base.reset()
motor_timeout = lambda motor, speed, degrees, stoptype: run_task(timeout_motor(motor, speed, degrees, stoptype))
# The main program starts here.
configure()
# drive_base.turn(-30, Stop.BRAKE)
drive_base.curve(640, -55, Stop.BRAKE)
drive_base.straight(90, Stop.BRAKE)
drive_base.turn(10, Stop.BRAKE)
drive_base.straight(-15, Stop.BRAKE)
motor_timeout(attach, 500, 250, Stop.BRAKE)
wait(1000)
wait(1000)
#motor_timeout(attach, 300, -120, Stop.BRAKE)
drive_base.straight(15, Stop.BRAKE)
drive_base.turn(-5, Stop.BRAKE)
drive_base.straight(-90, Stop.BRAKE)
#drive_base.curve(-640, 55, Stop.BRAKE)
#drive_base.straight(75, Stop.BRAKE)
"""
timeout_motor(attach300,-20, Stop.BRAKE)
drive_base.straight(15, Stop.BRAKE)
drive_base.turn(10,Stop.BRAKE)
drive_base.straight(-30, Stop.BRAKE)
#drive_base.turn(-30,Stop.BRAKE)
timeout_motor(attach400,-150, Stop.BRAKE)
drive_base.straight(20, Stop.BRAKE)
drive_base.straight(-100, Stop.BRAKE)
"""