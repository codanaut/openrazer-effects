import openrazer.client
import colorsys
import argparse

parser = argparse.ArgumentParser()
   
parser.add_argument('lvl', nargs='*')

args = parser.parse_args()

if args.lvl:
    lvl = float(args.lvl[0])
else:
    lvl = 100

device_manager = openrazer.client.DeviceManager()

for device in device_manager.devices:
    print("{}:".format(device.name))
    print("   type: {}".format(device.type))
    print("   serial: {}".format(device.serial))
    print("   firmware version: {}".format(device.firmware_version))
    print("   driver version: {}".format(device.driver_version))
    print()

    device_manager.sync_effects = False

for device in device_manager.devices:
        
    #print info & set brightness
    print("Setting {} brightness".format(device.name))
    device.brightness = lvl
