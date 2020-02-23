import subprocess
import time
import os
import signal
import sys

runningPID = ''

def checkProcess():
    if runningPID == '':
        pass
    else:
        killProcess()

def killProcess():
    id = runningPID
    #print(id)
    os.killpg(id, signal.SIGTERM)
    print("killing last effect")

def brightnessLVL(brightlvl):
    lvl = str(brightlvl)
    p = subprocess.Popen(['python3 set-brightness.py {}'.format(lvl)],stdout=subprocess.PIPE,shell=True, start_new_session=True)
    #global runningPID
    #runningPID = p.pid    

def sectionsRandom():
    p = subprocess.Popen(['python3 sections-randomRGB.py'],stdout=subprocess.PIPE,shell=True, start_new_session=True)
    global runningPID
    runningPID = p.pid


def stripes():
    p = subprocess.Popen(['python3 stripes.py'],stdout=subprocess.PIPE,shell=True, start_new_session=True)
    global runningPID
    runningPID = p.pid

def rainbowRGB():
    p = subprocess.Popen(['python3 rainbowRGB.py'],stdout=subprocess.PIPE,shell=True, start_new_session=True)
    global runningPID
    runningPID = p.pid

def menu():
    print(" ")
    print("RAZER EFFECT SETTER")
    print(" ")
    print("1: sections random rgb")
    print("2: stripes")
    print("3: rainbow rgb")
    print("-")
    print("b: Brightness")
    print("k: Kill Any Running Effects")
    print(" ")
    
def brightnessMenu():
    print("Enter Value between 0-100")
    print("to set brightness")
    blvl = input("Brightness: ")
    brightnessLVL(blvl)


def run():
    os.system('cls' if os.name == 'nt' else 'clear')
    option = ''
    menu()
    while option != 'q':

        option = input("Select option to run or 'q' and zero to exit: ")

        if option == str(1):
            os.system('cls' if os.name == 'nt' else 'clear')
            checkProcess()
            print("starting sections random rgb")
            sectionsRandom()
            menu()
        
        elif option == str(2):
            os.system('cls' if os.name == 'nt' else 'clear')
            checkProcess()
            print("starting Stipes effect")
            stripes()
            menu()
        
        elif option == str(3):
            os.system('cls' if os.name == 'nt' else 'clear')
            checkProcess()
            print("starting Rainbow RGB effect")
            rainbowRGB()
            menu()

        elif option == "b":
            os.system('cls' if os.name == 'nt' else 'clear')
            test = 10
            brightnessMenu()
            menu()

        elif option == "k":
            os.system('cls' if os.name == 'nt' else 'clear')
            killProcess()
            menu()
        
        elif option == "q":
            print(" ")
            print("EXITING and SHUTTING DOWN EFFECTS")
            checkProcess()
            sys.exit(0)
        elif option == str(0):
            print(" ")
            print("EXITING and SHUTTING DOWN EFFECTS")
            checkProcess()
            sys.exit(0)
        
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Please Enter Valid Option")
            print(" ")
            menu()
run()