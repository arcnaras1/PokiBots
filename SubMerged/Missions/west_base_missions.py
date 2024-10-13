def configurre():
    wait(1)
    motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
    motor_2 = Motor(Port.E, Direction.CLOCKWISE)
    drive_base = DriveBase(motor, motor_2, 56, 130)
    motor_2_2 = Motor(Port.F, Direction.COUNTERCLOCKWISE)
    drive_base.use_gyro(True)
    drive_base.reset()
    drive_base.settings(straight_speed=300)
    drive_base.settings(straight_acceleration=400)
    drive_base.settings(turn_rate=200)
    drive_base.settings(turn_acceleration=750)

def reset(): 
    leftwheel.reset_angle(0)
    rightwheel.reset_angle(0)
    drive_base.reset()

def WEST1():
    configurre()
    drive_base.straight(250)
    drive_base.straight(-150)
    drive_base.turn(-11)
    drive_base.straight(255)
    drive_base.straight(-75)
    drive_base.turn(6)
    drive_base.straight(95)
    drive_base.straight(-400)

def WEST2():
    configurre()
    drive_base.straight(-140, Stop.BRAKE)
    turn_attachment(motor_22, 1500, -155)
    drive_base.straight(175, Stop.BRAKE)
    drive_base.turn(-75, Stop.COAST)
    wait(1)
    drive_base.straight(190, Stop.BRAKE)
    drive_base.turn(8, Stop.BRAKE)
    drive_base.straight(-220, Stop.BRAKE)

def WEST3():
    configurre()
    motor_2_2.reset_angle(0)
    drive_base.straight(-185, Stop.BRAKE)
    drive_base.turn(55, Stop.BRAKE)
    drive_base.straight(-140, Stop.BRAKE)
    drive_base.turn(-90, Stop.BRAKE)
    drive_base.straight(-325, Stop.BRAKE)
    drive_base.turn(-20, Stop.BRAKE)
    turn_attachment(motor_2_2, 1200, -130)
    turn_attachment(motor_2_2, 1200, 130)
    drive_base.straight(8, Stop.BRAKE)
    drive_base.turn(45, Stop.BRAKE)
    drive_base.straight(-40, Stop.BRAKE)
    drive_base.turn(40, Stop.BRAKE)
    drive_base.straight(-40, Stop.BRAKE)
    turn_attachment(motor_2_2, 1000, -130)
    turn_attachment(motor_2_2, 1000, 130)
    drive_base.turn(105)
    drive_base.straight(-150, Stop.BRAKE)
    drive_base.turn(270, Stop.BRAKE)
    drive_base.straight(145)
    drive_base.straight(-145)
    drive_base.turn(-65)
    drive_base.straight(415)
    drive_base.turn(-45)

def WEST4():
    configurre()
    drive_base.straight(-490, Stop.BRAKE)
    drive_base.turn(-70, Stop.BRAKE)
    drive_base.straight(-110, Stop.BRAKE)
    drive_base.straight(100, Stop.BRAKE)
    drive_base.turn(6, Stop.BRAKE)
    motor_22.run_angle(500, -135, Stop.BRAKE)
    drive_base.straight(-90)
    drive_base.turn(-5)
    motor_22.run_angle(1500, 130, Stop.BRAKE)

def WEST5():
    """"
    def hello():



    return "I have a life"
    configure()
    reset()

    attachment.run_angle(1000,370)
    drive_base.straight(313 , Stop.BRAKE)
    drive_base.turn(67, Stop.BRAKE)
    drive_base.straight(107, Stop.BRAKE)
    attachment.run_angle(1000,-90)
    attachment.run_angle(500,90)
    """
    drive_base.straight(-322)
    drive_base.turn(92)
    drive_base.straight (-100 )

    drive_base.turn(21)


    drive_base.settings(straight_speed=67)
    drive_base.straight(-133)
    drive_base.straight(143)  
    """
    ###FREZEEE LINEEE MISSION 6 ABOVE MISSON 7 BELOW
    drive_base.turn (153.9)
    attachment.run_angle (1000,-80.7)
    drive_base.straight(60)
    attachment.run_angle (300,20)
    attachment.run_angle (1000,-60)
    drive_base.straight (-100)
    # attachment.run_angle (1000,-25)
    # drive_base.settings(straight_speed=57)
    drive_base.turn (90)
    drive_base.straight (310)
    """

def WEST6():
    configurre()
    reset()
    attachment.run_angle(1000,20)


    drive_base.straight(295, Stop.BRAKE)
    drive_base.turn(107.7, Stop.BRAKE)
    drive_base.straight (-65)
    drive_base.turn (57.7, Stop.BRAKE)
    drive_base.straight(-56)
    ###FReeze####
    drive_base.straight(-400, Stop.BRAKE)
    drive_base.turn(27.7, Stop.BRAKE)
    drive_base.straight(367.7, Stop.BRAKE)

    drive_base.turn (-17)

    drive_base.straight (37)

    drive_base.straight (-50)




    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    drive_base.straight(-100  , Stop.BRAKE)
    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #### FREEZE ###
    attachment.run_angle(1000,-83)
    drive_base.curve(100,20, Stop.BRAKE)
    drive_base.turn (18)
    drive_base.straight(100)

    drive_base.turn (-20)
    drive_base.straight (25)
    drive_base.turn (20)
    drive_base.straight (100)
    drive_base.turn (-40)
    hub.light.on(Color.RED)
    """
    drive_base.straight (180)
    attachment.run_angle(1000,60)
    """

    