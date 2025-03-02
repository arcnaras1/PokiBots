if __name__ == "__main__":
    import FullCodeTemplate
from BASEROBOT import *

#East Base Collection / Clear the Way
def EAST1(br: BaseRobot):
    br.settings(straight_speed=650)
    br.settings(straight_acceleration=600)
    br.settings(turn_rate=350)
    br.settings(turn_acceleration=500)
    br.use_gyro(True)

    
    br.straight (390)
    br.turn(36)
    br.straight(170)
    br.turn(-27)
    br.straight(120)
    br.turn (54)
    br.straight (130)
    br.turn (-50)
    br.straight(-1000)

#Sonar
def EAST2(br: BaseRobot):   
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
    br.left_attachment.run_angle(3000, 4800)
    br.left_attachment.run_angle(3000, -2800)
    br.straight(-10, Stop.BRAKE)
    br.turn(-50, Stop.BRAKE)
    br.settings(straight_speed=400)
    br.settings(straight_acceleration=400)
    br.straight(-800, Stop.BRAKE)

# feed the whale
def EAST3(br: BaseRobot):

   br.settings(straight_speed=150)
   br.settings(straight_acceleration=250)
   br.settings(turn_rate=200)
   br.settings(turn_acceleration=300)
   br.hub.imu.reset_heading(0)
   br.turn(-20, Stop.BRAKE)
   br.straight(-570, Stop.BRAKE)
   br.settings(straight_speed=500)
   br.settings(straight_acceleration=300)
   #br.turn(-5, Stop.BRAKE)
   br.hub.imu.reset_heading(0)
   br.turn(52, Stop.BRAKE)
   current = 0
   while sorted([51, (current := br.hub.imu.heading()), 53])[1] != current:
     br.drive(0, (54 - current) * -3)
   #earlier = br.hub.imu.heading()
   print("Start of delay?")
   br.stop()
   br.settings(straight_acceleration=400, straight_speed = 500)
   br.straight(-370, Stop.BRAKE)
   wait(2000)
   br.straight(100, Stop.BRAKE)

# Change Shipping Lanes 
def EAST4(br: BaseRobot):
   br.settings(straight_speed=300)
   br.settings(straight_acceleration=300)
   br.settings(turn_rate=200)
   br.settings(turn_acceleration=100)
   br.straight(495, Stop.BRAKE)
   br.turn(35, Stop.BRAKE)
   br.straight(30, Stop.BRAKE)
   br.right_attachment.run_angle(500, 300)
   br.settings(turn_rate=400)
   br.settings(turn_acceleration=300)
   br.turn(30, Stop.NONE)
   br.settings(turn_rate=75)
   br.turn(15,Stop.BRAKE, wait=False)
   br.straight(-10)
   br.right_attachment.run_angle(500, -300)
   br.straight(-30, Stop.BRAKE)
   br.turn(75,Stop.BRAKE)
   br.straight(300, Stop.BRAKE)
   #while not ((goal - 2) < br.hub.imu.heading() < (goal + 2)):
    #  br.drive(0, (goal - br.hub.imu.heading()) * 3)

#Prapti Combo
def EAST5(br):
    br.settings(straight_speed=350)  # ORIGINAL WAS 250
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
    # br.hub.imu.reset_heading(0)
    

    # br.straight(250, Stop.BRAKE)
    # current = 0
    # while (-1 < (current := br.hub.imu.heading()) < 1):
    #     br.drive(0, current * -3)

    # br.hub.imu.reset_heading(0)
    br.turn(51.78)
    # while (53.2 < (current := br.hub.imu.heading()) < 56.1):
    #     br.drive(0, (current - 54.78) * -3)
    br.straight(170)
    br.front_attachment.run_angle(700,1000)
    br.straight(50)
    br.front_attachment.run_angle(700,-470)
    wait(500)
    br.straight(-240)
    br.turn(-59.5)
    br.straight (350)
    br.straight (-200)
