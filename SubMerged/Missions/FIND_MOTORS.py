from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, wait
def find_ports():
    PORTS = [Port.A, Port.B, Port.C, Port.D, Port.E, Port.F]
    inps = ["LW", "RW", "LA", "RA", "LC", "RC"]
    ExpandedInp = ["Left Wheel", "Right Wheel", "Left Attachment", "Right Attachment", "Left Color Sensor", "Right Color Sensor"]
    vals = []
    for port in PORTS:
        print("Trying", port)
        worked = False
        try:
            m = Motor(port)
            m.run_angle(1500, 500, Stop.BRAKE)
            answer = ""
            while (not (answer:= input("Which of these motors ran?") or answer == "NW") in inps[:4]):
                pass
            vals.append((str(port), answer))
            worked = not worked
        except KeyboardInterrupt:
            vals.append((str(port), "NW"))
            continue
        except Exception as e:
            print(f"Not a motor: {e}")
        if not worked:
            try:
                c = ColorSensor(port)
                for _ in range(20):
                    c.lights.off()
                    wait(200)
                    c.lights.on(100)
                    wait(200)
                answer = ""
                while (not (answer:= input("Which of these color sensors ran?")) in inps[4:] or answer == "NW"):
                    pass
                vals.append((str(port), answer))
                c.lights.off()
            except Exception as e:
                print(f"Hmph: {e}")
    print("*********************************")
    for port, value in vals:
        if value == "NW":
            print(f"{port}: Not Working")
            continue
        print(f"{port}: {ExpandedInp[inps.index(value)]}")
    return vals

find_ports()
