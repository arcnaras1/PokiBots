from pybricks.hubs import PrimeHub
from pybricks.parameters import Port, Color, Button
from pybricks.tools import wait

# Standard MicroPython modules
from usys import stdin, stdout
from uselect import poll

hub = PrimeHub()
# Optional: Register stdin for polling. This allows
# you to wait for incoming data without blocking.
keyboard = poll()
keyboard.register(stdin)
cur_value = 1
while True:

    # Let the remote program know we are ready for a command.
    if Button.RIGHT in hub.buttons.pressed():
        cur_value += 1
        hub.display.number(cur_value)
        wait(250)
        
    if Button.LEFT in hub.buttons.pressed():
        cur_value -= 1
        hub.display.number(cur_value)
        wait(250)
        
    if Button.BLUETOOTH in hub.buttons.pressed():
        stdout.buffer.write(b'rdy')
        exec(f"stdout.buffer.write(b'{cur_value}')")
        while Button.BLUETOOTH in hub.buttons.pressed():
            pass
