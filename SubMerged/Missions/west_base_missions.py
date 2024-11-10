from BASEROBOT import *

# Set up all devices.
def WEST0(br: BaseRobot):
   br.settings(straight_speed=200)
   br.settings(straight_acceleration=400)
   br.settings(turn_rate=110)
   br.settings(turn_acceleration=400)
   br.use_gyro(True)
   
   br.straight(322)
   br.turn(92)
   br.straight (100 )
   br.turn(23)
   br.settings(straight_speed=60)
   br.straight(95)
   br.straight(-143)   
   
   br.settings(straight_speed=60)
   br.straight(95)
   br.straight(-143) 
# Collect corals and 1 Krill
def WEST1(br):
   #First Coral
   br.straight(350)
   br.straight(-370)

# Mission 5
def WEST2(br):
    br.settings(straight_speed=150)
    br.settings(straight_acceleration=500)
    br.settings(turn_rate=50)
    br.settings(turn_acceleration=400)
    br.use_gyro(True)
    br.straight(310+325, Stop.BRAKE)
    br.turn(-65, Stop.BRAKE)
    br.straight(237.7, Stop.BRAKE)
    br.turn (-94)
    br.straight (220)
    """
    br.straight(177)
    br.turn(-90.7)
    br.straight(-237.7, Stop.BRAKE)
    br.turn(-90, Stop.BRAKE)
    br.straight(320+310, Stop.BRAKE)
    """
# Mission 6
def WEST3(br):




   br.straight(-322)
   br.turn(92)
   br.straight (-100 )


   br.turn(21)




   br.settings(straight_speed=67)
   br.straight(-133)
   br.straight(143) 


   ###FREZEEE LINEEE MISSION 6 ABOVE MISSON 7 BELOW
   br.turn (153.9)
   br.front_attachment.run_angle (1000,-80.7)
   br.straight(60)
   br.front_attachment.run_angle (300,20)
   br.front_attachment.run_angle (1000,-60)
   br.straight (-100)
   #br.front_attachment.run_angle (1000,-25)
   # br.settings(straight_speed=57)
   br.turn (90)
   br.straight (310)
         
# Missions 1, 2, 3, 4
def WEST4(br):
attachment_motor = br.front_attachment

   br.use_gyro(True)
   br.settings(straight_speed=300)
   br.settings(straight_acceleration=400)
   br.settings(turn_rate=200)
   br.settings(turn_acceleration=750)
   br.reset()

   ############# Mission 1 #############
   br.straight(-490, Stop.BRAKE)
   br.turn(-70, Stop.BRAKE)
   br.straight(-125, Stop.BRAKE)
   br.straight(100, Stop.BRAKE)
   
   
   ############# Mission 4 #############
   br.turn(5, Stop.BRAKE)
   br.turn_attachment(attachment_motor, 200, 135)
   br.straight(-50)
   br.turn_attachment(attachment_motor, 1500, -135)
   
   ############# Mission 2 #############
   br.straight(-8, Stop.BRAKE)
   br.straight(40, Stop.BRAKE)
   br.turn(16, Stop.BRAKE)
   br.turn_attachment(attachment_motor, 1500, -130)
   br.straight(-40)
   br.turn_attachment(attachment_motor, 1500, 130)
   br.turn_attachment(attachment_motor, 500, -135)
   br.straight(8, Stop.BRAKE)
   
   ############# Mission 3 #############
   br.turn(31, Stop.BRAKE)
   br.straight(-30)
   br.turn(67, Stop.BRAKE)
   br.turn_attachment(attachment_motor, 500, 135)
   br.turn_attachment(attachment_motor, 500, -135)
   
   
   ############# Return to Base #############
   br.turn(105, Stop.BRAKE)
   br.straight(-560, Stop.BRAKE)
   

# Mission 1 part 2
def WEST5(br):
   attachment_motor = br.front_attachment
   br.use_gyro(True)
   br.settings(straight_speed=300)
   br.settings(straight_acceleration=400)
   br.settings(turn_rate=200)
   br.settings(turn_acceleration=750)
   br.reset()
   ####MAIN CODE####
   br.straight(-100)
   br.turn_attachment(attachment_motor, 200, -200)
   br.straight(-200)

def WEST6(br):
   br.straight(180, Stop.BRAKE)
   br.straight(-220, Stop.BRAKE)
