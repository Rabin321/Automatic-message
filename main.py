# automatically send a-z.
import pyautogui
import time
import string
for letter in string.ascii_lowercase:
    time.sleep(1)
    pyautogui.typewrite(letter)
    pyautogui.press('enter')
