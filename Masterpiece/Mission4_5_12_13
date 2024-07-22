from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

# Set up all devices.
prime_hub = PrimeHub()
left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right = Motor(Port.E, Direction.CLOCKWISE)
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
drive_base.straight(675, Stop.NONE)
drive_base.turn(40, Stop.BRAKE)
drive_base.straight(150, Stop.BRAKE)
drive_base.turn(60, Stop.BRAKE)
drive_base.straight(600, Stop.BRAKE)
drive_base.turn(-90, Stop.BRAKE)
drive_base.straight(200, Stop.BRAKE)
drive_base.straight(-200, Stop.BRAKE)
drive_base.turn(45, Stop.BRAKE)
drive_base.straight(300, Stop.BRAKE)
drive_base.straight(-200, Stop.BRAKE)
drive_base.turn(45, Stop.BRAKE)
drive_base.straight(550, Stop.BRAKE)
drive_base.turn(80, Stop.BRAKE)
drive_base.straight(400, Stop.BRAKE)
drive_base.turn(130, Stop.BRAKE)
drive_base.straight(400, Stop.BRAKE)
drive_base.straight(-500, Stop.BRAKE)
