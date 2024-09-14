from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
# Set up all devices.
prime_hub = PrimeHub()
left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right = Motor(Port.E, Direction.CLOCKWISE)
attach = Motor(Port.F)
drive_base = DriveBase(left, right, 56, 130)
def configure():
    drive_base.settings(straight_speed=350)
    drive_base.settings(straight_acceleration=500)
    drive_base.settings(turn_rate=700)
    drive_base.settings(turn_acceleration=400)
    drive_base.use_gyro(True)
    drive_base.reset()

# The main program starts here.
configure()
#"""
drive_base.straight(-580, Stop.BRAKE)
attach.run_angle(100, 85)
drive_base.straight(93, Stop.BRAKE)
drive_base.straight(15, Stop.BRAKE)
attach.run_angle(100, -85 )
drive_base.straight(93, Stop.BRAKE)
#drive_base.straight(50, Stop.BRAKE)
#attach.run_angle(2000, -120)
#"""
#drive_base.turn(-90, Stop.BRAKE)