from BASEROBOT import *

# Collect corals and 1 Krill
def WEST1(br):
   #First Coral
   br.straight(350)
   br.turn(26)
   br.turn(-26)
   br.straight(-480)

# Mission 5,shRK DROPPOFF
def WEST2(br):
    br.settings(straight_speed=400)
   #br.settings(straight_acceleration=400)
   br.settings(straight_acceleration=700)
   br.settings(turn_rate=110)
   br.settings(turn_acceleration=400)
   br.use_gyro(True)
   br.hub.imu.reset_heading(0)
   """
   br.straight(280)
   br.turn (40)
   br.straight (118)
   """
   br.straight (-570)
   br.turn(-85.77)
   br.straight (-40)
   br.straight (78.77)
   br.turn (-90)
   br.straight (-450)
   br.turn (253)
   br.settings(straight_speed=300)
   br.straight(157)
   br.turn(96)
   br.straight (100)
   br.turn(22.77)
   br.settings(straight_speed=43)
   br.straight(120.7)
   br.turn (70)  
   br.settings(straight_speed=130)
   br.straight (100)
   br.turn(90)
   br.straight (300)

   # Missions 1, 2, 3, 4
def WEST3(br):
   attachment_motor = br.front_attachment

   br.use_gyro(True)
   br.settings(straight_speed=300)
   br.settings(straight_acceleration=400)
   br.settings(turn_rate=200)
   br.settings(turn_acceleration=750)
   br.reset()

   ############# Mission 1 #############
   br.straight(-477)
   br.turn(-70, Stop.BRAKE)
   br.straight(-132, Stop.BRAKE)
   br.straight(100, Stop.BRAKE)
   
   
   ############# Mission 4 #############
   
   br.turn_attachment(attachment_motor, 200, 135)
   br.straight(-55)
   br.turn_attachment(attachment_motor, 1500, -135)
   
   ############# Mission 2 #############
   br.straight(-8, Stop.BRAKE)
   br.straight(40, Stop.BRAKE)
   br.turn(15.78, Stop.BRAKE)
   br.turn_attachment(attachment_motor, 1500, -130)
   br.straight(-50)
   br.turn_attachment(attachment_motor, 1500, 130)
   br.turn_attachment(attachment_motor, 500, -135)
   br.straight(8, Stop.BRAKE)
   
   ############# Mission 3 #############
   br.turn(28, Stop.BRAKE)
   br.straight(-28)
   br.turn(64, Stop.BRAKE)
   br.straight(-11)
   br.turn_attachment(attachment_motor, 500, 135)
   br.turn_attachment(attachment_motor, 500, -135)
   
   
   ############# Return to Base #############
   br.turn(108, Stop.BRAKE)
   br.straight(-562, Stop.BRAKE)

# Mission 1 part 2
def WEST4(br):
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

# Put Coral back on the Map
def WEST5(br):
   br.settings(straight_speed = 20)
   br.straight(180, Stop.BRAKE)
   br.settings(straight_speed = 100)
   br.straight(-220, Stop.BRAKE)
