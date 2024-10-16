from BASEROBOT import *
from east_base_missions_linked import EAST2
from west_base_missions import WEST1, WEST2, WEST3, WEST4, WEST5, WEST6

br = BaseRobot(Port.B, Port.E, Port.F, Port.A, 56, 130)
RunOrder = [WEST1,WEST2,WEST3,WEST4,WEST5,WEST6, EAST2]
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
        RunOrder[mission_counter - 1](br)
    br.hub.display.number(mission_counter)
"""
for k, mission_run in enumerate(RunOrder):
    br.hub.display.number(k+1)
    while not Button.RIGHT in prime_br.hub.buttons.pressed():
        pass
    mission_run()
"""