if __name__ == "__main__":
    import FullCodeTemplate
from BASEROBOT import *

def EAST1(br: BaseRobot):   
    br.settings(straight_speed=200)
    br.settings(straight_acceleration=200)
    br.settings(turn_rate=150)
    br.settings(turn_acceleration=400)
    br.use_gyro(True)
    br.hub.imu.reset_heading(0)
    br.turn(-25, Stop.BRAKE)
    br.straight(800, Stop.BRAKE)
    br.turn(30, Stop.BRAKE)
    br.straight(-20, Stop.BRAKE)
    br.left_attachment.run_angle(3000, 6480)
    br.left_attachment.run_angle(3000, -2800)
    wait(1000)
    br.straight(-10, Stop.BRAKE)
    br.turn(-50, Stop.BRAKE)
    br.straight(-800, Stop.BRAKE)

    """
def EAST1(br: BaseRobot):   
    br.settings(straight_speed=200)
    br.settings(straight_acceleration=200)
    br.settings(turn_rate=150)
    br.settings(turn_acceleration=400)
    br.use_gyro(True)
    br.hub.imu.reset_heading(0)
    br.right_attachment.run_angle(600, -300)
    br.straight(-150, Stop.BRAKE)
    br.right_attachment.run_angle(600, 350, wait=False)
    wait(200)
    br.straight(50, Stop.BRAKE)
"""
def EAST2(br: BaseRobot):
   br.settings(straight_speed=300)
   br.settings(straight_acceleration=300)
   br.settings(turn_rate=200)
   br.settings(turn_acceleration=300)
   br.straight(-610, Stop.BRAKE)
   br.turn(-5, Stop.BRAKE)
   br.straight(-110, Stop.BRAKE)
   br.turn(44, Stop.BRAKE)
   br.settings(straight_acceleration=500)
   br.straight(-175, Stop.BRAKE)
   wait(2000)
   br.straight(100, Stop.BRAKE)
def EAST3(br: BaseRobot):
   br.settings(straight_speed=300)
   br.settings(straight_acceleration=300)
   br.settings(turn_rate=200)
   br.settings(turn_acceleration=100)
   br.turn(-30, Stop.BRAKE)
   br.straight(250, Stop.BRAKE)
   br.turn(45, Stop.BRAKE)
   br.straight(160, Stop.BRAKE)
   br.turn(33, Stop.BRAKE)
   br.settings(straight_acceleration=500)
   br.straight(200, Stop.BRAKE)
   goal = br.hub.imu.heading() + 90
   br.settings(straight_acceleration=600)
   br.settings(turn_acceleration=600)
   while not ((goal - 2) < br.hub.imu.heading() < (goal + 2)):
      br.drive(0, (goal - br.hub.imu.heading()) * 3)

def EAST4(br: BaseRobot):
    br.settings(straight_speed=350)
    br.settings(straight_acceleration=500)
    br.settings(turn_rate=150)
    br.settings(turn_acceleration=400)
    br.use_gyro(True)
    br.hub.imu.reset_heading(0)
    
    br.front_attachment.run_angle(700,-905)
    br.straight (270, Stop.BRAKE)
    br.turn(-40, Stop.BRAKE)
    br.straight(270, Stop.BRAKE)
    br.straight(-150, Stop.BRAKE)
    br.turn(35, Stop.BRAKE)
    br.straight(375, Stop.BRAKE)
    br.turn (-85, Stop.BRAKE)
    br.straight(250, Stop.BRAKE)
    br.turn(54.78)
    br.straight(170)
    br.front_attachment.run_angle(700,1000)
    br.straight(50)
    br.front_attachment.run_angle(700,-470)
    wait(500)
    br.straight(-240)
    br.turn(-59.5)
    br.straight (350)
    br.straight (-200)
