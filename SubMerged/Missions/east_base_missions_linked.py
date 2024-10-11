from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
motor_1 = Motor(Port.E, Direction.COUNTERCLOCKWISE)
motor_2 = Motor(Port.B, Direction.CLOCKWISE)
motor = Motor(Port.F, Direction.CLOCKWISE)
drive_base = DriveBase(motor_1, motor_2, 56, 130)
drive_base.use_gyro(True)
def my_task():
    drive_base.settings(straight_speed=170)
    drive_base.settings(straight_acceleration=150)
    drive_base.settings(turn_rate=300)
    drive_base.settings(turn_acceleration=300)
"""
drive_base.turn(-12)
drive_base.straight(-310)
drive_base.turn(25)
drive_base.straight(-70)
drive_base.turn(30)
drive_base.straight(-100)

drive_base.straight(110)
drive_base.turn(15)
drive_base.straight(25)
drive_base.turn(60)
drive_base.straight(30)
drive_base.turn(25)
drive_base.straight(-50)
drive_base.turn(80)
# drive_base.straight(100)
"""
drive_base.settings(turn_acceleration=200)
drive_base.turn(-20, Stop.BRAKE)
drive_base.straight(-225, Stop.BRAKE)
drive_base.straight(100, Stop.BRAKE)
drive_base.turn(25, Stop.BRAKE)
drive_base.settings(straight_acceleration=250)
drive_base.straight(-310, Stop.BRAKE)
drive_base.turn(46, Stop.BRAKE)
drive_base.straight(-60, Stop.BRAKE)
drive_base.straight(100, Stop.BRAKE)
