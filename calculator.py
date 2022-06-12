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
        menu.Menu().basic_cal()
        Input = int(input("Enter Your Choice: "))
        if Input == 1: # code written in this is for addition 
            result = functions.basic_method().add() # usr define function module
            print("Result of Addition is:",result)
            time.sleep(7)
            os.system("cls")
        if Input == 2: # code written in this is for subtraction 
            result = functions.basic_method().subtract()
            print("Result of Subtraction is:",result)
            time.sleep(7)
            os.system("cls")
        if Input == 3: # code written in this is for multiplication 
            result = functions.basic_method().multiply()
            print("Result of Multiplication is:",result)
            time.sleep(7)
            os.system("cls")
        if Input == 4: # code written in this is for division 
            result = functions.basic_method().divide()
            print("Result of Division is:",result)
            time.sleep(7)
            os.system("cls")
calculator()
    

    
