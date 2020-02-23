import openrazer.client
import colorsys
import random
import time
import sys

device_manager = openrazer.client.DeviceManager()
devices = device_manager.devices

for device in devices:
    if not device.fx.advanced:
        print("Skipping device " + device.name + " (" + device.serial + ")")
        devices.remove(device)
    print("Setting {} to stripes effect".format(device.name))

#Color Options
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
white = [255,255,255]

def step1():
    try:
        for device in devices:
            rows, cols = device.fx.advanced.rows, device.fx.advanced.cols

            even = [0,2,4]
            odd = [1,3,5]
            for i in even:
                for col in range(cols):
                    device.fx.advanced.matrix[i, col] = green
            for i in odd:
                for col in range(cols):
                    device.fx.advanced.matrix[i, col] = blue
            
            device.fx.advanced.draw()

    except:
        print("is device connected? Sleeping for 30 seconds, will try again!")
        time.sleep(30)
        pass

def step2():
    try:
        for device in devices:
            rows, cols = device.fx.advanced.rows, device.fx.advanced.cols

            even = [0,2,4]
            odd = [1,3,5]

            for i in even:
                for col in range(cols):
                    device.fx.advanced.matrix[i, col] = blue
            for i in odd:
                for col in range(cols):
                    device.fx.advanced.matrix[i, col] = green
            
            device.fx.advanced.draw()


    except:
        print("is device connected? Sleeping for 30 seconds, will try again!")
        time.sleep(30)
        pass

# define which function to run and how long to sleep between color changes
def run():
    while True:
        try:
            step1()
            time.sleep(1)
            step2()
            time.sleep(1)
        except KeyboardInterrupt:
            print(" You Press CTRL+C GOOD BYE")
            sys.exit(0)
            

run()