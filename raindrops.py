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
black = [0,0,0]
grey = [15,15,15]

# set color of effects
color = blue
backgroundColor = grey

def step1():
    try:
        for device in devices:
            rows, cols = device.fx.advanced.rows, device.fx.advanced.cols

            for row in range(rows):
                for col in range(cols):
                    device.fx.advanced.matrix[row, col] = backgroundColor

            device.fx.advanced.draw()

    except:
        print("is device connected? Sleeping for 30 seconds, will try again!")
        time.sleep(30)
        pass

def step2():
    try:
        for device in devices:
            rows, cols = device.fx.advanced.rows, device.fx.advanced.cols


            def ranRow():
                rRow = random.randint(0,5)
                #print(rRow)
                return rRow
            
            def ranCol():
                rCol = random.randint(1,21)
                #print(rCol)
                return rCol
            
            try:
                for i in range(10):
                    device.fx.advanced.matrix[ranRow(), ranCol()] = color
                
            except:
                pass

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
            time.sleep(0)
            step2()
            time.sleep(1)
        except KeyboardInterrupt:
            print(" You Press CTRL+C GOOD BYE")
            sys.exit(0)
            

run()