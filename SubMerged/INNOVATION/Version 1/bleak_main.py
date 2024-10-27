import asyncio
import gspread_auth_backend as gs
from contextlib import suppress
from bleak import BleakScanner, BleakClient

PYBRICKS_COMMAND_EVENT_CHAR_UUID = "c5f50002-8280-46da-89f4-6d8051e4aeef"
HUB_NAME = "MAAHI"
drn = 1

async def main():
    main_task = asyncio.current_task()

    # Handle disconnection events
    def handle_disconnect(_):
        print("Hub was disconnected.")
        if not main_task.done():
            main_task.cancel()

    # Event to manage the ready signal
    ready_event = asyncio.Event()

    # Callback function for handling received data
    def handle_rx(_, data: bytearray):
        global drn
        if data[0] == 0x01:  # "write stdout" event (0x01)
            payload = data[1:].decode()
            cond = True
            try:
                int(payload)
            except:
                cond = False
            if payload == "rdy":
                ready_event.set()  # Set ready signal if payload is "rdy"
            elif cond:
                print("Received:", payload)
                gs.set_value(drn, payload)  # Save data to Google Sheets
                drn += 1

    # Scan for the hub by name
    device = await BleakScanner.find_device_by_name(HUB_NAME)
    if device is None:
        print(f"Could not find hub with name: {HUB_NAME}")
        return

    # Connect to the hub and begin notification
    async with BleakClient(device, handle_disconnect) as client:
        await client.start_notify(PYBRICKS_COMMAND_EVENT_CHAR_UUID, handle_rx)

        # Function to send commands to the hub
        async def send(data):
            await ready_event.wait()  # Wait until ready
            ready_event.clear()       # Reset ready signal
            await client.write_gatt_char(
                PYBRICKS_COMMAND_EVENT_CHAR_UUID, b"\x06" + data, response=True
            )

        # Inform user to start the program on the hub
        print("Start the program on the hub now with the button.")
        
        # Infinite loop to keep the connection alive and process incoming messages
        while True:
            await asyncio.sleep(1)  # Keep the loop running without blocking

# Run the main async program
if __name__ == "__main__":
    with suppress(asyncio.CancelledError):
        asyncio.run(main())
