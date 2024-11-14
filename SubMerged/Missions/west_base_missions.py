from BASEROBOT import *

# Collect corals and 1 Krill
def WEST1(br):
   #First Coral
   br.straight(350)
   br.turn(26)
   br.turn(-26)
   br.straight(-480)

# Mission 5,6
def WEST2(br):
    def WEST1(br: BaseRobot):
   br.settings(straight_speed=300)
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
   br.straight(322)
   br.turn(96)
   br.straight (100 )
   br.turn(16)
   br.settings(straight_speed=43)
   br.straight(140.7)
   br.turn (70)  
   br.hub.light.on(Color.MAGENTA)
   br.settings(straight_speed=600)
   br.straight (100)
   br.turn(93.5)
   br.straight (-500)
   br.turn(225.7)
   br.hub.light.on(Color.RED)
   br.settings(straight_speed=350)
   br.straight(-345, Stop.BRAKE)
   br.turn (-35.7)
   br.straight (-70)
   br.straight (125)
   br.turn (-120)
   br.straight (-200)
   br.turn (-85)
   br.straight (637.777)

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
   br.turn(31, Stop.BRAKE)
   br.straight(-27)
   br.turn(65, Stop.BRAKE)
   br.straight(-8)
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
