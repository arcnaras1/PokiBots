if __name__ == "__main__":
    import FullCodeTemplate
from BASEROBOT import *
def EAST1(br: BaseRobot):
    br.settings(straight_speed=200)
    br.settings(straight_acceleration=200)
    br.settings(turn_rate=150)
    br.settings(turn_acceleration=400)
    br.use_gyro(True)
    br.hub.imu.reset_heading(0)
    br.left_attachment.run_angle(400, -275)
    wait(1000)
    br.left_attachment.run_angle(400, 275)


def EAST6(br):
    br.settings(straight_speed=250)
    br.settings(straight_acceleration=500)
    br.settings(turn_rate=150)
    br.settings(turn_acceleration=400)
    br.use_gyro(True)
    br.hub.imu.reset_heading(0)
    
    br.front_attachment.run_angle(700,-905)
    br.straight (270, Stop.BRAKE)
    br.turn(-40, Stop.BRAKE)
    br.straight(270, Stop.BRAKE)
    br.straight(-150, Stop.BRAKE)
    br.turn(35, Stop.BRAKE)
    br.straight(375, Stop.BRAKE)
    br.turn (-85, Stop.BRAKE)
    br.straight(250, Stop.BRAKE)
    br.turn(54.78)
    br.straight(170)
    br.front_attachment.run_angle(700,1000)
    br.straight(50)
    br.front_attachment.run_angle(700,-470)
    wait(500)
    br.straight(-240)
    br.turn(-59.5)
    br.straight (350)
    br.straight (-200)
