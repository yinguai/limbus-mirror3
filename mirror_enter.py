import pyautogui
import time

#识别主界面drive
drive_key=0
drive = "./main_web/drive.png"
try:
    drive_position = pyautogui.locateOnScreen(drive, confidence=0.7)

    if drive_position:
        target_x, target_y = pyautogui.center(drive_position)
        pyautogui.click(target_x, target_y)
        drive_key=1
        time.sleep(4)
except Exception:
    pass

#点击镜牢
try:
    mirror_key=0
    mirror = "./main_web/mirror.png"
    mirror_position = pyautogui.locateOnScreen(mirror, confidence=0.7)
    if drive_key and mirror_position:
        target_x, target_y = pyautogui.center(mirror_position)
        pyautogui.click(target_x, target_y)
        mirror_key=1
        time.sleep(2)
except Exception:
    pass


#进入
try:
    normal_key=0
    normal = "./main_web/normal.png"
    normal_position = pyautogui.locateOnScreen(normal, confidence=0.7)
    if normal_position:
        target_x, target_y = pyautogui.center(normal_position)
        pyautogui.click(target_x, target_y)
        normal_key=1
        time.sleep(2)
except Exception:
    pass

#进入
try:
    enter_key=0
    enter = "./main_web/enter.png"
    enter_position = pyautogui.locateOnScreen(enter, confidence=0.7)
    if enter_position:
        target_x, target_y = pyautogui.center(enter_position)
        pyautogui.click(target_x, target_y)
        enter_key=1
        time.sleep(2)
except Exception:
    pass

#初始选择
try:
    yellow_key=0
    yellow = "./main_web/yellow.png"
    yellow_position = pyautogui.locateOnScreen(yellow, confidence=0.7)
    if yellow_position:
        target_x, target_y = pyautogui.center(yellow_position)
        pyautogui.click(target_x, target_y)
        yellow_key=1
        time.sleep(2)
except Exception:
    pass

#初始ego
try:
    green_spirit_key=0
    green_spirit = "./main_web/green_spirit.png"
    green_spirit_position = pyautogui.locateOnScreen(green_spirit, confidence=0.7)
    if green_spirit_position:
        target_x, target_y = pyautogui.center(green_spirit_position)
        pyautogui.click(target_x, target_y)
        green_spirit_key=1
        time.sleep(2)
except Exception:
    pass

#选择
try:
    select1_key=0
    select1 = "./main_web/select1.png"
    select1_position = pyautogui.locateOnScreen(select1, confidence=0.7)
    if select1_position:
        target_x, target_y = pyautogui.center(select1_position)
        pyautogui.click(target_x, target_y)
        select1_key=1
        time.sleep(2)
except Exception:
    pass

#confirm
try:
    confirm_key=0
    confirm = "./main_web/confirm.png"
    confirm_position = pyautogui.locateOnScreen(confirm, confidence=0.7)
    if confirm_position:
        target_x, target_y = pyautogui.center(confirm_position)
        pyautogui.click(target_x, target_y)
        confirm_key=1
        time.sleep(2)
except Exception:
    pass

#confirm1
try:
    confirm1_key=0
    confirm1 = "./main_web/confirm1.png"
    confirm1_position = pyautogui.locateOnScreen(confirm1, confidence=0.7)
    if confirm1_position:
        target_x, target_y = pyautogui.center(confirm1_position)
        pyautogui.click(target_x, target_y)
        confirm1_key=1
        time.sleep(2)
except Exception:
    pass