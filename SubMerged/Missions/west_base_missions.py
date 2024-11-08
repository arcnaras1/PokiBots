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
   br.straight(-115, Stop.BRAKE)
   br.straight(100, Stop.BRAKE)
   wait(100)
   
   ############# Mission 4 #############
   br.turn(2.5, Stop.BRAKE)
   br.turn_attachment(attachment_motor, 500, 135)
   br.straight(-55)
   br.turn_attachment(attachment_motor, 1500, -135)
   wait(100)
   
   ############# Mission 2 #############
   br.straight(-8, Stop.BRAKE)
   br.turn_attachment(attachment_motor, 1500, 80)
   br.straight(53, Stop.BRAKE)
   br.turn(19, Stop.BRAKE)
   br.turn_attachment(attachment_motor, 1500, -130)
   br.straight(-43)
   br.turn_attachment(attachment_motor, 1500, 130)
   br.turn_attachment(attachment_motor, 500, -135)
   br.straight(8, Stop.BRAKE)
   wait(100)
   
   ############# Mission 3 #############
   br.turn(30, Stop.BRAKE)
   br.straight(-30)
   br.turn(60, Stop.BRAKE)
   br.straight(-38)
   br.turn_attachment(attachment_motor, 500, 135)
   br.turn_attachment(attachment_motor, 500, -135)
   wait(100)
   
   ############# Return to Base #############
   br.turn(110, Stop.BRAKE)
   br.straight(-520, Stop.BRAKE)
    ############Return Seaweed#########
   

# Mission 1 part 2
def WEST5(br):
   attachment_motor = br.front_attachment
   br.use_gyro(True)
   br.reset()
   br.settings(straight_speed=300)
   br.settings(straight_acceleration=400)
   br.settings(turn_rate=200)
   br.settings(turn_acceleration=750)

   br.straight(-140, Stop.BRAKE)
   br.turn_attachment(attachment_motor, 1500, 155)
   br.straight(175, Stop.BRAKE)
   br.turn(-75, Stop.COAST)
   while not any(prime_hub.buttons.pressed()):
      wait(1)
   br.straight(190, Stop.BRAKE)
   br.turn(8, Stop.BRAKE)
   br.straight(-220, Stop.BRAKE)

def WEST6(br):
   br.straight(-322)
   br.turn(92)
   br.straight (-100 )

   br.turn(21)


   br.settings(straight_speed=67)
   br.straight(-133)
   br.straight(143)