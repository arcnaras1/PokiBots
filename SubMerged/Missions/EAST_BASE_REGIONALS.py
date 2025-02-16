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
