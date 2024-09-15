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
    drive_base.settings(straight_speed=350)
    drive_base.settings(straight_acceleration=200)
    drive_base.settings(turn_rate=100)
    drive_base.settings(turn_acceleration=100)
    
drive_base.straight(-400)
drive_base.turn(45)
drive_base.straight(-100)
drive_base.straight(100)
drive_base.turn(-45)
drive_base.straight(450)
# drive_base.straight(-400)
# drive_base.straight(300)
# drive_base.turn(10)
# drive_base.straight(-300)
# drive_base.straight(500)