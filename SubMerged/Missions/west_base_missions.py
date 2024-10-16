from BASEROBOT import *


async def turn_attachment(attach_motor, speed, degree):
    await wait(1)
    await multitask(attach_motor.run_angle(speed, degree, Stop.BRAKE), wait(1000), race=True)

def WEST1(br: BaseRobot):
    br.use_gyro(True)
    br.reset()
    br.settings(straight_speed=300)
    br.settings(straight_acceleration=400)
    br.settings(turn_rate=200)
    br.settings(turn_acceleration=750)

    br.straight(250)
    br.straight(-150)
    br.turn(-11)
    br.straight(255)
    br.straight(-75)
    br.turn(6)
    br.straight(95)
    br.straight(-400)

def WEST2(br: BaseRobot):
    br.use_gyro(True)
    br.reset()
    br.settings(straight_speed=300)
    br.settings(straight_acceleration=400)
    br.settings(turn_rate=200)
    br.settings(turn_acceleration=750)
    br.straight(-140, Stop.BRAKE)
    turn_attachment(br.front_attachment, 1500, -155)
    br.straight(175, Stop.BRAKE)
    br.turn(-75, Stop.COAST)
    wait(1)
    br.straight(190, Stop.BRAKE)
    br.turn(8, Stop.BRAKE)
    br.straight(-220, Stop.BRAKE)

def WEST3(br: BaseRobot):
    br.use_gyro(True)
    br.reset()
    br.settings(straight_speed=300)
    br.settings(straight_acceleration=400)
    br.settings(turn_rate=200)
    br.settings(turn_acceleration=750)
    br.front_attachment.reset_angle(0)
    br.straight(-185, Stop.BRAKE)
    br.turn(55, Stop.BRAKE)
    br.straight(-140, Stop.BRAKE)
    br.turn(-90, Stop.BRAKE)
    br.straight(-325, Stop.BRAKE)
    br.turn(-20, Stop.BRAKE)
    turn_attachment(br.front_attachment, 1200, -130)
    turn_attachment(br.front_attachment, 1200, 130)
    br.straight(8, Stop.BRAKE)
    br.turn(45, Stop.BRAKE)
    br.straight(-40, Stop.BRAKE)
    br.turn(40, Stop.BRAKE)
    br.straight(-40, Stop.BRAKE)
    turn_attachment(br.front_attachment, 1000, -130)
    turn_attachment(br.front_attachment, 1000, 130)
    br.turn(105)
    br.straight(-150, Stop.BRAKE)
    br.turn(270, Stop.BRAKE)
    br.straight(145)
    br.straight(-145)
    br.turn(-65)
    br.straight(415)
    br.turn(-45)

def WEST4(br: BaseRobot):
    br.use_gyro(True)
    br.reset()
    br.settings(straight_speed=300)
    br.settings(straight_acceleration=400)
    br.settings(turn_rate=200)
    br.settings(turn_acceleration=750)
    br.straight(-490, Stop.BRAKE)
    br.turn(-70, Stop.BRAKE)
    br.straight(-110, Stop.BRAKE)
    br.straight(100, Stop.BRAKE)
    br.turn(6, Stop.BRAKE)
    motor_22.run_angle(500, -135, Stop.BRAKE)
    br.straight(-90)
    br.turn(-5)
    motor_22.run_angle(1500, 130, Stop.BRAKE)

def WEST5(br: BaseRobot):
    br.use_gyro(True)
    br.reset()
    br.settings(straight_speed=300)
    br.settings(straight_acceleration=400)
    br.settings(turn_rate=200)
    br.settings(turn_acceleration=750)
    """"
    def hello():



    return "I have a life"
    configure()
    reset()

    attachment.run_angle(1000,370)
    br.straight(313 , Stop.BRAKE)
    br.turn(67, Stop.BRAKE)
    br.straight(107, Stop.BRAKE)
    attachment.run_angle(1000,-90)
    attachment.run_angle(500,90)
    """
    br.straight(-322)
    br.turn(92)
    br.straight (-100 )

    br.turn(21)


    br.settings(straight_speed=67)
    br.straight(-133)
    br.straight(143)  
    """
    ###FREZEEE LINEEE MISSION 6 ABOVE MISSON 7 BELOW
    br.turn (153.9)
    attachment.run_angle (1000,-80.7)
    br.straight(60)
    attachment.run_angle (300,20)
    attachment.run_angle (1000,-60)
    br.straight (-100)
    # attachment.run_angle (1000,-25)
    # br.settings(straight_speed=57)
    br.turn (90)
    br.straight (310)
    """

def WEST6(br: BaseRobot):
    br.use_gyro(True)
    br.reset()
    br.settings(straight_speed=300)
    br.settings(straight_acceleration=400)
    br.settings(turn_rate=200)
    br.settings(turn_acceleration=750)
    br.reset()
    br.front_attachment.run_angle(1000,20)


    br.straight(295, Stop.BRAKE)
    br.turn(107.7, Stop.BRAKE)
    br.straight (-65)
    br.turn (57.7, Stop.BRAKE)
    br.straight(-56)
    ###FReeze####
    br.straight(-400, Stop.BRAKE)
    br.turn(27.7, Stop.BRAKE)
    br.straight(367.7, Stop.BRAKE)

    br.turn (-17)

    br.straight (37)

    br.straight (-50)




    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    br.straight(-100  , Stop.BRAKE)
    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #### FREEZE ###
    attachment.run_angle(1000,-83)
    br.curve(100,20, Stop.BRAKE)
    br.turn (18)
    br.straight(100)

    br.turn (-20)
    br.straight (25)
    br.turn (20)
    br.straight (100)
    br.turn (-40)
    br.hub.light.on(Color.RED)
    """
    br.straight (180)
    attachment.run_angle(1000,60)
    """

    