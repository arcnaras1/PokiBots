
from BASEROBOT import *
def EAST1(br: BaseRobot):
    br.settings(straight_speed=200)
    br.settings(straight_acceleration=200)
    br.settings(turn_rate=150)
    br.settings(turn_acceleration=400)
    br.use_gyro(True)
    # """
    # br.turn(-12)
    # br.straight(-310)
    # br.turn(25)
    # br.straight(-70)
    # br.turn(30)
    # br.straight(-100)

    # br.straight(110)
    # br.turn(15)
    # br.straight(25)
    # br.turn(60)
    # br.straight(30)
    # br.turn(25)
    # br.straight(-50)
    # br.turn(80)
    # # br.straight(100)
    # """
    # br.settings(turn_acceleration=200)
    # br.turn(-22, Stop.BRAKE)
    # br.straight(235, Stop.BRAKE)
    # br.straight(-100, Stop.BRAKE)
    # br.turn(20, Stop.BRAKE)
    # br.settings(straight_acceleration=250)
    # br.straight(310, Stop.BRAKE)
    # br.turn(35, Stop.BRAKE)
    # br.straight(70, Stop.BRAKE)
    # br.straight(-140, Stop.BRAKE)
    # br.turn(92, Stop.BRAKE)
    br.straight(70, Stop.BRAKE)
    br.turn(-28, Stop.BRAKE)
    br.straight(180, Stop.BRAKE)
    br.straight(-170, Stop.BRAKE)
    br.turn(192, Stop.BRAKE)
    br.straight(-390, Stop.BRAKE)
    br.turn(-4, Stop.BRAKE)
    br.front_attachment.run_angle(100,-85)
    br.straight(75, Stop.BRAKE)
    br.turn(-20, Stop.BRAKE)
    br.straight(-100, Stop.BRAKE)
    br.front_attachment.run_angle(100, 85)
    br.straight(500)
def EAST2(br: BaseRobot):
    br.settings(straight_speed=400)
    #br.settings(straight_acceleration=400)
    br.settings(straight_acceleration=800)
    br.settings(turn_rate=110)
    br.settings(turn_acceleration=400)
    br.hub.imu.reset_heading(0)
    br.use_gyro(True)
    #br.straight (-800, Stop.BRAKE)
    br.turn(3)
    br.straight(-740, Stop.NONE)
    x = 900
    while x > 100:
        br.drive(x, 0)
        x-= 200
    br.brake()
    br.front_attachment.run_angle(100,-85)
    br.settings(straight_acceleration=650)
    br.straight (123, Stop.BRAKE)
    br.front_attachment.run_angle(100,85, Stop.BRAKE)
    br.straight (100, Stop.BRAKE)
    while not -88 > br.hub.imu.heading() > -92:
        br.drive(0, turn_rate=-300)
    br.brake()
    br.straight (-150, Stop.BRAKE)
    br.turn(90, Stop.BRAKE)
    br.straight (-800, Stop.BRAKE)

def EAST3(br: BaseRobot):
    br.straight(280, Stop.BRAKE)
    br.curve(8.25, 17, Stop.BRAKE)
    br.straight(10)
    # br.straight(-17, Stop.BRAKE)
    br.back_attachment.run_angle(1000,815, Stop.BRAKE)
    br.settings(turn_acceleration=200)
    br.turn(27, Stop.BRAKE)
    br.back_attachment.run_angle(1000,-815, Stop.BRAKE)
    br.straight(-60, Stop.BRAKE)
    br.turn(-55, Stop.BRAKE)
    br.straight(300)
    br.back_attachment.run_angle(1000,150, Stop.BRAKE)
    br.turn(-10, Stop.BRAKE)
    br.straight(30, Stop.BRAKE)
    br.turn_attachment(br.back_attachment, 1000, 950, wait_time=1500)
    br.back_attachment.run_angle(1000, -800)
    br.straight(-410, Stop.BRAKE)
    br.turn(27, Stop.BRAKE)
    br.straight(-300, Stop.BRAKE)
def EAST4(br: BaseRobot):
    br.straight(400)
    br.turn(45)
    br.straight(100)
    br.straight(-100)
    br.turn(-45)
    br.straight(-450)
def EAST5(br: BaseRobot):
    br.settings(straight_speed=350)
    br.settings(straight_acceleration=200)
    br.settings(turn_rate=100)
    br.settings(turn_acceleration=150)

    br.straight(437, Stop.BRAKE)
    br.settings(turn_rate=80)
    br.turn(46, Stop.BRAKE)
    br.straight(100, Stop.BRAKE)

    br.straight(-100, Stop.BRAKE)
    br.straight(100, Stop.BRAKE)
    br.straight(-200, Stop.BRAKE)
    br.turn(-160, Stop.BRAKE)
    br.straight(-200)
def EAST6(br:BaseRobot):
    br.straight(460)
    br.straight(-300)
    br.turn(-20)
    br.straight(-150)
def EAST7(br:BaseRobot):
    br.straight(-500)
    br.straight(100)
    br.turn(-30)
    br.straight(-800)
