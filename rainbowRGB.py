import colorsys
import random
import time
from openrazer.client import DeviceManager
from openrazer.client import constants as razer_constants
import sys

# Create a DeviceManager. This is used to get specific devices
device_manager = DeviceManager()
print("Found {} Razer devices".format(len(device_manager.devices)))

devices = device_manager.devices

for device in devices:
    if not device.fx.advanced:
        print("Skipping device " + device.name + " (" + device.serial + ")")
        devices.remove(device)
    print("Setting {} to rainbow rgb".format(device.name))

# Disable daemon effect syncing.
# Without this, the daemon will try to set the lighting effect to every device.
device_manager.sync_effects = False


# set color lists
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
colors = [red,green,blue]

# Set random colors for each zone of each device
def setColors():
    try:
        for device in devices:
            rows, cols = device.fx.advanced.rows, device.fx.advanced.cols

            for row in range(rows):
                for col in range(cols):
                    device.fx.advanced.matrix[row, col] = random.choice(colors)

            device.fx.advanced.draw()
    except:
        print("Are the devices connected?")
        pass

# define which function to run and how long to sleep between color changes
def run():
    while True:
        try:
            setColors()
            time.sleep(1)
        except KeyboardInterrupt:
            print(" You Press CTRL+C GOOD BYE")
            sys.exit(0)
            

run()