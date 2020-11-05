import mss
import cv2 as cv
import numpy as np
import pyautogui
import pynput
import time

def on_release(key):
    print('{0} irti'.format(key))
    if key == pynput.keyboard.Key.esc:
        return False
    if key == pynput.keyboard.Key.down:
        pyautogui.moveTo(960,910)
        save_keypress_and_image("Down",window_capture())
    if key == pynput.keyboard.Key.left:
        pyautogui.moveTo(280,540)
        save_keypress_and_image("Left", window_capture())
    if key == pynput.keyboard.Key.right:
        pyautogui.moveTo(1640,540)
        save_keypress_and_image("Right", window_capture())
    if key == pynput.keyboard.Key.up:
        pyautogui.moveTo(960,170)
        save_keypress_and_image("Up", window_capture())


def save_keypress_and_image(keypress,screenshot):
    path = "/home/lebaa/poeAI/{}/{}.jpg".format(keypress,time.time())
    print(path)
    cv.imwrite(path,screenshot)



listener = pynput.keyboard.Listener(on_release = on_release)
listener.start()

def window_capture():

    monitor = {"top": 0, "left": 1640, "width": 275, "height": 275}
    screenshot = mss.mss().grab(monitor)
    return np.array(screenshot)

while True:
    cv.imshow('ikkuna',window_capture())
    if cv.waitKey(1) == ord('q'):
        break

print("asd")
