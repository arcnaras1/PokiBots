from BASEROBOT import *
from east_base_missions_linked import EAST1, EAST2, EAST3, EAST4, EAST5, EAST6
from west_base_missions import WEST0, WEST1
br = BaseRobot(Port.E, Port.C, Port.A, Port.D, 56, 81)
RunOrder = [WEST0, WEST1, EAST1, EAST2, EAST3, EAST4, EAST5, EAST6]
#RunOrder = [lambda: br.hub.light.on(Color.BROWN), lambda: br.hub.light.on(Color.RED),lambda: br.hub.light.on(Color.GREEN)]
mission_counter = 1
while True:
    if Button.RIGHT in br.hub.buttons.pressed():
        mission_counter += 1
        mission_counter = ((mission_counter - 1) % len(RunOrder)) + 1
        wait(250)
        
    if Button.LEFT in br.hub.buttons.pressed():
        mission_counter -= 1
        mission_counter = ((mission_counter - 1) % len(RunOrder)) + 1
        wait(250)
    
    if Button.BLUETOOTH in br.hub.buttons.pressed():
        br.use_gyro(True)
        RunOrder[mission_counter - 1](br)
        br.stop()
    br.hub.display.number(mission_counter)
"""
for k, mission_run in enumerate(RunOrder):
    br.hub.display.number(k+1)
    while not Button.RIGHT in prime_br.hub.buttons.pressed():
        pass
    mission_run()
"""
