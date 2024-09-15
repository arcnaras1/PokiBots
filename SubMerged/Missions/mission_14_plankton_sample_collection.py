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
    drive_base.settings(turn_acceleration=150)
drive_base.straight(200, Stop.BRAKE)
drive_base.turn(-30, Stop.BRAKE)
drive_base.straight(175, Stop.BRAKE)
drive_base.turn(45, Stop.BRAKE)
drive_base.straight(150, Stop.BRAKE)
drive_base.turn(60, Stop.BRAKE)
drive_base.straight(30)
# drive_base.straight(20, Stop.BRAKE)
motor.run_angle(500,100, Stop.BRAKE)
drive_base.straight(-30, Stop.BRAKE)
drive_base.turn(45, Stop.BRAKE)
drive_base.straight(550, Stop.BRAKE)


