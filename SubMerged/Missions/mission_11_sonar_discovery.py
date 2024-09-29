from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

prime_hub = PrimeHub()
left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right = Motor(Port.E, Direction.CLOCKWISE)
attach = Motor(Port.F)
drive_base = DriveBase(left, right, 56, 130)
def configure():
    drive_base.settings(straight_speed=175)
    drive_base.settings(straight_acceleration=150)
    drive_base.settings(turn_rate=400)
    drive_base.settings(turn_acceleration=400)
    drive_base.use_gyro(True)
    drive_base.reset()

# The main program starts here.
configure()

drive_base.straight(-460, Stop.BRAKE)
drive_base.turn(-23, Stop.BRAKE)
drive_base.straight(-51, Stop.BRAKE)
attach.run_angle(100,74)
drive_base.straight(50, Stop.BRAKE)
drive_base.turn(-12, Stop.BRAKE)
drive_base.straight(-60, Stop.BRAKE)
drive_base.turn(12, Stop.BRAKE)
drive_base.settings(turn_rate=200)
attach.run_angle(100,-74)
"""
drive_base.straight(-430, Stop.BRAKE)
drive_base.turn(-19, Stop.BRAKE)
drive_base.straight(-55, Stop.BRAKE)
attach.run_angle(100,84)
drive_base.straight(50, Stop.BRAKE)
drive_base.turn(-12, Stop.BRAKE)
drive_base.straight(-60, Stop.BRAKE)
drive_base.turn(12, Stop.BRAKE)
attach.run_angle(100,-84)
"""