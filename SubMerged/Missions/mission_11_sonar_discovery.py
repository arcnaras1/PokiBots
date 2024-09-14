from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

prime_hub = PrimeHub()
left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right = Motor(Port.E, Direction.CLOCKWISE)
attach = Motor(Port.A)
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
drive_base.turn(-16, Stop.BRAKE)
drive_base.straight(515, Stop.BRAKE)
drive_base.turn(-17, Stop.BRAKE)
#drive_base.straight(15, Stop.BRAKE)
attach.run_angle(100,-80)
drive_base.straight(35, Stop.BRAKE)
attach.run_angle(100,250)
drive_base.straight(-17, Stop.BRAKE)
attach.run_angle(100,800)