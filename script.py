from attr import s
import pyautogui
import keyboard
import sys

while True:
    if keyboard.is_pressed("u"):
        while True:
            if keyboard.is_pressed("n"):
                break
            else:
                pyautogui.press("Q")
    if keyboard.is_pressed("j"):
        sys.exit()