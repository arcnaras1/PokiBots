from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, wait

class BaseRobot(DriveBase):
    def __init__(self, leftwheel: Port, rightwheel: Motor, left_attachment: Port, right_attachment: Port, wheel_diameter, axle_track):
        self.hub = PrimeHub()
        self.rightwheel = Motor(rightwheel)
        self.leftwheel = Motor(leftwheel, Direction.COUNTERCLOCKWISE)
        self.left_attachment = Motor(left_attachment)
        self.right_attachment = Motor(right_attachment)
        super().__init__(self.leftwheel, self.rightwheel, wheel_diameter, axle_track)   

    def turn_attachment(self, attach_motor, speed, degree, wait_time=1000):
      async def turn_attachment_coroutine(attach_motor, speed, degree):
         await multitask(attach_motor.run_angle(speed, degree, Stop.BRAKE), wait(wait_time), race=False)
      run_task(turn_attachment_coroutine(attach_motor, speed, degree))  
