from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop, Color
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
# Set up all devices.
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
drive_base.curve(380, -45, Stop.BRAKE)
drive_base.straight(-20, Stop.BRAKE)
drive_base.turn(-45, Stop.BRAKE)
drive_base.curve(250, 65, Stop.BRAKE)
drive_base.turn(20, Stop.BRAKE)
drive_base.straight(-25, Stop.BRAKE)
attach.run_angle(500, -80)
drive_base.straight(-60, Stop.BRAKE)
