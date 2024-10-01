from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
motor_1 = Motor(Port.E, Direction.COUNTERCLOCKWISE)
motor_2 = Motor(Port.B, Direction.CLOCKWISE)
motor = Motor(Port.A, Direction.CLOCKWISE)
drive_base = DriveBase(motor_1, motor_2, 56, 130)
drive_base.use_gyro(True)
def my_task():
    drive_base.settings(straight_speed=200)
    drive_base.settings(straight_acceleration=150)
    drive_base.settings(turn_rate=400)
    drive_base.settings(turn_acceleration=400)
drive_base.turn(-12)
drive_base.straight(-310)
drive_base.turn(35)
drive_base.straight(-70)
drive_base.turn(25)
drive_base.straight(-100)
