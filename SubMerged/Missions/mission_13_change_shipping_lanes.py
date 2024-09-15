from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

prime_hub = PrimeHub()
motor = Motor(Port.A, Direction.CLOCKWISE)
motor_1 = Motor(Port.E, Direction.COUNTERCLOCKWISE)
motor_2 = Motor(Port.B, Direction.CLOCKWISE)
drive_base = DriveBase(motor_1, motor_2, 56, 130)
drive_base.use_gyro(True)
def my_task():
    drive_base.settings(straight_speed=350)
    drive_base.settings(straight_acceleration=200)
    drive_base.settings(turn_rate=100)
    drive_base.settings(turn_acceleration=150)

drive_base.straight(-305, Stop.BRAKE)
drive_base.curve(8.75, 25, Stop.BRAKE)
# drive_base.straight(-17, Stop.BRAKE)
motor.run_angle(100,-95, Stop.BRAKE)
drive_base.settings(turn_rate=50)
drive_base.turn(25, Stop.BRAKE)
motor.run_angle(100,80, Stop.BRAKE)
motor.run_angle(100, -20)
drive_base.straight(100)
drive_base.turn(70)
drive_base.straight(-300)








