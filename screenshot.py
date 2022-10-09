import pyautogui


# pip install pyautogui
#pip install Pillow --upgrade
import pyautogui #importeer deze package

myScreenshot = pyautogui.screenshot() # variable voor het uitvoeren van deze functie.
myScreenshot.save(r'screenshot.png') #hij voert de functie uit en slaat het op
exit() #verlaat python