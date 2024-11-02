from BASEROBOT import *

# Mission 6
def WEST1(br: BaseRobot):
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
   
   br.straight (143)
   br.straight (-95)
   br.settings(straight_speed=130)
   br.turn(-23)
   br.straight(-100)
   br.turn (-92)
   br.straight (-322)

# Collect corals and 1 Krill
def WEST2(br):
   #First Coral
   br.straight(350)
   br.turn(26)
   br.turn(26)
   br.straight(-480)
  
# Mission 5
def WEST3(br):
    br.settings(straight_speed=250)
    br.settings(straight_acceleration=500)
    br.settings(turn_rate=150)
    br.settings(turn_acceleration=400)
    br.use_gyro(True)
    br.reset()
    
    br.straight(-310-320, Stop.BRAKE)
    br.turn(90, Stop.BRAKE)
    br.straight(237.7, Stop.BRAKE)
    br.turn (90.7)
    br.straight (-177)

    br.straight(177)
    br.turn(-90.7)
    br.straight(-237.7, Stop.BRAKE)
    br.turn(-90, Stop.BRAKE)
    br.straight(320+310, Stop.BRAKE)
         
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
   br.straight(-118, Stop.BRAKE)
   br.straight(100, Stop.BRAKE)
   wait(100)
   
   ############# Mission 4 #############
   br.turn(2.7, Stop.BRAKE)
   br.turn_attachment(attachment_motor, 200, 135)
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
   br.turn(31, Stop.BRAKE)
   br.straight(-30)
   br.turn(59.75, Stop.BRAKE)
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
   br.straight(190, Stop.BRAKE)
   br.turn(8, Stop.BRAKE)
   br.straight(-220, Stop.BRAKE)
