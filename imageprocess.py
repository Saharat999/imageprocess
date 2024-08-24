import cv2
import numpy as np
import pyautogui
import time

template = cv2.imread('รูปภาพ', 0)
template_height, template_width = template.shape[:2]

if template is None:
    print("Failed to load template image.")
    exit()

threshold = 0.6 

while True:
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    if len(loc[0]) > 0:
        print("Detected")
        for pt in zip(*loc[::-1]):
            print(f"Object found at: {pt}")
    else:
        print("Not Detected")
    time.sleep(1)
