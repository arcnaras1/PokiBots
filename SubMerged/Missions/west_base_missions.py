from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import multitask, run_task, wait


# Set up all devices.
prime_hub = PrimeHub()

# Collect corals and 1 Krill
def WEST1(br):
   br.straight(230)
   br.straight(-300)
   while not any(prime_hub.buttons.pressed()):
       wait(1)
   br.straight(320)
   br.straight(-330)
   while not any(prime_hub.buttons.pressed()):
       wait(1)
   br.straight(400)
   br.straight(-400)
   while not any(prime_hub.buttons.pressed()):
       wait(1)
   br.straight(70)
   br.straight(-75)

# Mission 5
def WEST2(br):
   leftwheel.reset_angle(0)
   rightwheel.reset_angle(0)
   br.front_attachment.run_angle(1000,-20)




   br.straight(310, Stop.BRAKE)
   br.turn(113.7, Stop.BRAKE)
   br.straight (-75)
   br.turn (57.7, Stop.BRAKE)
   br.straight(-56)
   ###FReeze####
   br.straight(-400, Stop.BRAKE)
   br.turn(27.7, Stop.BRAKE)
   br.straight(380.7, Stop.BRAKE)




   br.turn (-22.7)


   br.straight (57)












   ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   br.straight(-100  , Stop.BRAKE)
   ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


   #### FREEZE ###
   br.front_attachment.run_angle(1000,75)
   br.curve(100,20, Stop.BRAKE)
   br.turn (11)
   br.straight(100)
   """
   br.turn (-20)


   br.straight (25)
   br.turn (25)
   """
   hub.light.on(Color.RED)
   br.straight (70)
   """
   br.turn (-40)
   hub.light.on(Color.RED)


   br.straight (180)
   """
   br.front_attachment.run_angle(1000,-80)
   br.turn (120)
   br.straight (300)

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
   br.turn(1.50, Stop.BRAKE)
   br.turn_attachment(attachment_motor, 500, 135)
   br.straight(-58)
   br.turn_attachment(attachment_motor, 1500, -135)
   wait(100)
   
   ############# Mission 2 #############
   br.straight(-8, Stop.BRAKE)
   br.turn_attachment(attachment_motor, 1500, 80)
   br.straight(60, Stop.BRAKE)
   br.turn(19, Stop.BRAKE)
   br.turn_attachment(attachment_motor, 1500, -130)
   br.straight(-43)
   br.turn_attachment(attachment_motor, 1500, 130)
   br.turn_attachment(attachment_motor, 500, -135)
   br.straight(8, Stop.BRAKE)
   wait(100)
   
   ############# Mission 3 #############
   br.turn(33, Stop.BRAKE)
   br.straight(-30)
   br.turn(65.25, Stop.BRAKE)
   br.straight(-38)
   br.turn_attachment(attachment_motor, 500, 135)
   br.turn_attachment(attachment_motor, 500, -135)
   wait(100)
   
   ############# Return to Base #############
   br.turn(110, Stop.BRAKE)
   br.straight(-520, Stop.BRAKE)

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