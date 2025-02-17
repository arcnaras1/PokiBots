if __name__ == "__main__":
   import FullCodeTemplate

from BASEROBOT import *
# Collect corals and 1 Krill
def WEST0(br):
   br.use_gyro(True)
   br.settings(straight_speed=200)
   br.straight(-310, Stop.BRAKE)
   br.curve(-205, -80, Stop.BRAKE)
   #br.settings(straight_speed=250)
   br.straight(-210, Stop.BRAKE)
   br.straight(227, Stop.BRAKE)
   br.turn(-80, Stop.BRAKE)
   br.straight(600, Stop.BRAKE)
def WEST1(br):
   br.use_gyro(True)
   br.hub.imu.reset_heading(0)
   br.settings(straight_speed=100)
   br.straight(250)
   br.straight(-250)
   while not (-1 < br.hub.imu.heading() < 1):
      br.drive(0, br.hub.imu.heading() * -3)
   br.straight(520)
# def WEST1(br):
#    #First Coral
#    br.straight(350)
#    br.turn(26)
#    br.turn(-26)
#    br.straight(-480)

# # Mission 5,shRK DROPPOFF
# def WEST2(br):
#     br.settings(straight_speed=250)
#     br.settings(straight_acceleration=500)
#     br.settings(turn_rate=150)
#     br.settings(turn_acceleration=400)
#     br.use_gyro(True)
#     br.reset()

#     br.straight(-310-320, Stop.BRAKE)
#     br.turn(90, Stop.BRAKE)
#     br.straight(237.7, Stop.BRAKE)
#     br.turn (90.7)
#     br.straight (-177)

#     br.straight(177)
#     br.turn(-90.7)
#     br.straight(-237.7, Stop.BRAKE)
#     br.turn(-90, Stop.BRAKE)
#     br.straight(320+310, Stop.BRAKE)

#    # Missions 1, 2, 3, 4
# def WEST3(br):
#    attachment_motor = br.front_attachment

#    br.use_gyro(True)
#    br.settings(straight_speed=300)
#    br.settings(straight_acceleration=400)
#    br.settings(turn_rate=200)
#    br.settings(turn_acceleration=750)
#    br.reset()

#    ############# Mission 1 #############
#    br.straight(-477, Stop.BRAKE)
#    br.turn(-70, Stop.BRAKE)
#    br.straight(-132, Stop.BRAKE)
#    br.straight(100, Stop.BRAKE)
   
   
#    ############# Mission 4 #############
   
#    br.turn_attachment(attachment_motor, 200, 135)
#    br.straight(-55, Stop.BRAKE)
#    br.turn_attachment(attachment_motor, 1500, -135)
   
#    ############# Mission 2 #############
#    br.straight(-8, Stop.BRAKE)
#    br.straight(40, Stop.BRAKE)
#    br.turn(19, Stop.BRAKE)
#    br.turn_attachment(attachment_motor, 1800, -130)
#    br.straight(-50, Stop.BRAKE)
#    br.turn_attachment(attachment_motor, 1500, 130)
#    br.turn_attachment(attachment_motor, 500, -135)
#    br.straight(8, Stop.BRAKE)
   
#    ############# Mission 3 #############
#    br.turn(27, Stop.BRAKE)
#    br.straight(-28, Stop.BRAKE)
#    br.turn(61, Stop.BRAKE)
#    br.straight(-13, Stop.BRAKE)
#    br.turn_attachment(attachment_motor, 500, 135)
#    br.turn_attachment(attachment_motor, 500, -135)
   
   
#    ############# Return to Base #############
#    br.turn(106, Stop.BRAKE)
#    br.straight(-562, Stop.BRAKE)


# # Mission 1 part 2
# def WEST4(br):
#    attachment_motor = br.front_attachment
#    br.use_gyro(True)
#    br.settings(straight_speed=300)
#    br.settings(straight_acceleration=400)
#    br.settings(turn_rate=200)
#    br.settings(turn_acceleration=750)
#    br.reset()
#    ####MAIN CODE####
#    br.straight(-100)
#    br.turn_attachment(attachment_motor, 200, -200)
#    br.straight(-200)

# # Put Coral back on the Map
# def WEST5(br):
#    br.settings(straight_speed = 20)
#    br.straight(40, Stop.BRAKE)
#    br.settings(straight_speed = 100)
#    br.straight(-100, Stop.BRAKE)