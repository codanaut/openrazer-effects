import openrazer.client
import colorsys
import random
import time
import sys

#####################################
#CONFIG COLORS & TIME BETWEEN CHANGES

#Color Options
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
white = [255,255,255]

#colors to be randomly chosen
#colors = [red,green,blue,white]
colors = [red,green,blue]
#colors = [red,blue,white]

#time in seconds between color changes
sleepTime = 1

#####################################

device_manager = openrazer.client.DeviceManager()
devices = device_manager.devices
print("Found {} Razer devices".format(len(device_manager.devices)))

for device in devices:
    if not device.fx.advanced:
        print("Skipping device " + device.name + " (" + device.serial + ")")
        devices.remove(device)
    print("Setting {} to rainbow rgb".format(device.name))


def customMatrix():
    try:
        for device in devices:
            
            #rows - there is a max of 6 rows starting at 0-5
            fRow = [0]
            topRows = [1,2]
            bottomRows = [3,4,5]

            #f key groups
            fGroup1 = [3,4,5,6]
            fGroup2 = [7,8,9,10]
            fGroup3 = [11,12,13,14]

            #cols left, middle, right
            leftCols = [0,1,2,3,4,5]
            middleCols = [6,7,8,9,10]
            rightCols = [11,12,13,14]

            #Control keys - ins,home,page up. starts at 15
            controlKeyCols = [15,16,17]
            controlMidRows =[1,2]

            # keypad
            keypadCols = [18,19,20,21]

            #esc key
            color = random.choice(colors)
            device.fx.advanced.matrix[0, 1] = color

            #F1-F4
            color = random.choice(colors)
            for i in fRow:
                for c in fGroup1:
                    device.fx.advanced.matrix[i, c] = color

            #F5 - F8
            color = random.choice(colors)
            for i in fRow:
                for c in fGroup2:
                    device.fx.advanced.matrix[i, c] = color

            #F9 - F12
            color = random.choice(colors)
            for i in fRow:
                for c in fGroup3:
                    device.fx.advanced.matrix[i, c] = color

            #left alphanumeric keys top & bottom
            color = random.choice(colors)
            for i in topRows:
                for c in leftCols:
                    device.fx.advanced.matrix[i, c] = color
            color = random.choice(colors)
            for i in bottomRows:
                for c in leftCols:
                    device.fx.advanced.matrix[i, c] = color

            #middle alphanumeric keys top & bottom
            color = random.choice(colors)
            for i in topRows:
                for c in middleCols:
                    device.fx.advanced.matrix[i, c] = color
            color = random.choice(colors)
            for i in bottomRows:
                for c in middleCols:
                    device.fx.advanced.matrix[i, c] = color
            
            #right alphanumeric keys top & bottom
            color = random.choice(colors)
            for i in topRows:
                for c in rightCols:
                    device.fx.advanced.matrix[i, c] = color
            color = random.choice(colors)
            for i in bottomRows:
                for c in rightCols:
                    device.fx.advanced.matrix[i, c] = color
            
            #control keys top & bottom
            color = random.choice(colors)
            for i in fRow:
                for c in controlKeyCols:
                    device.fx.advanced.matrix[i, c] = color
            color = random.choice(colors)
            for i in controlMidRows:
                for c in controlKeyCols:
                    device.fx.advanced.matrix[i, c] = color
            
            # Arrow Keys
            color = random.choice(colors)
            for i in bottomRows:
                for c in controlKeyCols:
                    device.fx.advanced.matrix[i, c] = color

            #keypad top & bottom
            color = random.choice(colors)
            for i in topRows:
                for c in keypadCols:
                    device.fx.advanced.matrix[i, c] = color
            color = random.choice(colors)
            for i in bottomRows:
                for c in keypadCols:
                    device.fx.advanced.matrix[i, c] = color
                    

            device.fx.advanced.draw()

    except:
        print("is device connected? Sleeping for 30 seconds, will try again!")
        time.sleep(30)
        pass



# define which function to run and how long to sleep between color changes
def run():
    while True:
        try:
            customMatrix()
            time.sleep(sleepTime)
        except KeyboardInterrupt:
            print(" You Press CTRL+C GOOD BYE")
            sys.exit(0)
            

run()