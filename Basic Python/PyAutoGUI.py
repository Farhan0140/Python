#   https://pypi.org/project/PyAutoGUI/
#   https://pyautogui.readthedocs.io/en/latest/


#   

import pyautogui
import time

time.sleep(4)

for i in range(1, 50):
    pyautogui.write('@')
    pyautogui.write('M')
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')




