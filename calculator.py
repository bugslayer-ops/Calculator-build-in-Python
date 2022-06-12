import functions
import menu
import time
import os

print("[Note]:- Enter Your Name before using further this tool..!") # print the note to usr
usr_name = input("Enter Your Name: ") # Enter the name of user...!
time.sleep(4) # set time delay 
os.system("cls") 


def calculator():
    print("Wellcome to Calculator..!")
    menu.Menu().main_menu()
    Input = int(input("Enter Your Choice: ")) # usr input the options mentioned above 
    if Input == 1: # usr input "1"
        os.system("cls") # clear screen 
        print("Note:- You Selected Basic Calculations..!") # usr selected Basic Calculations
        
calculator()
    

    