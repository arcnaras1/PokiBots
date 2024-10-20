from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, multitask
from BASEROBOT import *

# Set up all devices.
prime_hub = PrimeHub()
def turn_attachment(motor, speed, degree):
       print(motor.run_angle(speed, degree, Stop.BRAKE))
       multitask(await motor.run_angle(speed, degree, Stop.BRAKE), wait(1000), race=True)

def WEST1(br):




# The main program starts here.
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
   br.straight(25)
   br.straight(-45)




def WEST2(br):
   br.front_attachment.run_angle(1000,-20)
   br.straight(-310, Stop.BRAKE)
   br.turn(113.7, Stop.BRAKE)
   br.straight (75)
   br.turn (57.7, Stop.BRAKE)
   br.straight(56)
   ###FReeze####
   br.straight(400, Stop.BRAKE)
   br.turn(27.7, Stop.BRAKE)
   br.straight(-380.7, Stop.BRAKE)




   br.turn (-22.7)


   br.straight (-57)












   ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   br.straight(100  , Stop.BRAKE)
   ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


   #### FREEZE ###
   br.front_attachment.run_angle(1000,75)
   br.curve(100,20, Stop.BRAKE)
   br.turn (11)
   br.straight(-100)
   """
   br.turn (-20)


   br.straight (25)
   br.turn (25)
   """
   hub.light.on(Color.RED)
   br.straight (-70)
   """
   br.turn (-40)
   hub.light.on(Color.RED)


   br.straight (180)
   """
   br.front_attachment.run_angle(1000,-80)
   br.turn (120)
   br.straight (-300)




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


def WEST4(br):
   br.use_gyro(True)
   br.reset()
   br.settings(straight_speed=300)
   br.settings(straight_acceleration=400)
   br.settings(turn_rate=200)
   br.settings(turn_acceleration=750)


   br.straight(-490, Stop.BRAKE)
   br.turn(-70, Stop.BRAKE)
   br.straight(-115, Stop.BRAKE)
   br.straight(100, Stop.BRAKE)
   br.turn(4, Stop.BRAKE)
   turn_attachment(br.front_attachment, 500, 135)
   br.straight(-64)
   turn_attachment(br.front_attachment, 1500, -135)
   br.straight(-11, Stop.BRAKE)
   turn_attachment(br.front_attachment, 1500, 130)
   br.straight(65, Stop.BRAKE)
   br.turn(22, Stop.BRAKE)
   turn_attachment(br.front_attachment, 1500, -130)
   br.straight(-51)
   turn_attachment(br.front_attachment, 1500, 130)
   turn_attachment(br.front_attachment, 500, -135)
   br.straight(8, Stop.BRAKE)
   br.turn(45, Stop.BRAKE)
   br.straight(-30)
   br.turn(55, Stop.BRAKE)
   br.straight(-40)
   turn_attachment(br.front_attachment, 500, 135)
   turn_attachment(br.front_attachment, 500, -135)
   br.turn(95, Stop.BRAKE)
   br.straight(-495, Stop.BRAKE)
   br.turn(90)
   br.straight(-390, Stop.BRAKE)




def WEST5(br):
    br.use_gyro(True)
    br.reset()
    br.settings(straight_speed=300)
    br.settings(straight_acceleration=400)
    br.settings(turn_rate=200)
    br.settings(turn_acceleration=750)


    br.straight(-140, Stop.BRAKE)
    turn_attachment(br.front_attachment, 1500, 50)
    br.straight(175, Stop.BRAKE)
    br.turn(-75, Stop.COAST)
    while not any(prime_hub.buttons.pressed()):
        wait(1)
    br.straight(190, Stop.BRAKE)
    br.turn(8, Stop.BRAKE)
    br.straight(-220, Stop.BRAKE)




    #run_task(main())

