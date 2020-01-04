import pyautogui
import time
#prints the y position to be used as ypos in main.py. Put cursor slightly under the bookmarks (fullscreen) and copy that y position to ypos.
while True:
    time.sleep(2)
    print(pyautogui.position().y)