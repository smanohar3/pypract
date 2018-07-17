#Splash Screen - Used to display before any start of the application - a game etc.
import os
import time

def splash_screen(seconds):
    print("\n")
    print("*********************")
    print("*                   *")
    print("*    SPLASH SCREEN  *")
    print("*    VERSION 1.0    *")
    print("*                   *")
    print("*********************")
    time.sleep(seconds)
    os.system('clear')

splash_screen(3)
username = input('Your Username: ')
print('Hey ' + username)
