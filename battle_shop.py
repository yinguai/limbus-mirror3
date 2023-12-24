import time
from PIL import ImageGrab
import pyautogui
import os

#定义点击函数
def click_image(image_path, confidence=0.55, timeout=60):
    start_time = time.time()
    position = None

    while time.time() - start_time < timeout:
        position = pyautogui.locateOnScreen(image_path, confidence=confidence)
        
        if position:
            target_x, target_y = pyautogui.center(position)
            pyautogui.click(target_x, target_y)
            return True  # 点击成功返回True
        
        time.sleep(0.5)  # 每隔1秒检查一次
        
    return False  # 超时返回False

shop = "./shop/shop.png"
enter = "./shop/enter.png"
skip = "./shop/skip.png"
choose2 = "./shop/choose2.png"
heal = "./shop/heal.png"
conti = "./shop/conti.png"
leave = "./shop/leave.png"
confirm = "./shop/confirm.png"

#点击商店
try:
    shop_position = pyautogui.locateOnScreen(shop, confidence=0.45)
    if shop_position:
        target_x, target_y = pyautogui.center(shop_position)
        pyautogui.click(target_x, target_y)
        shop_key=1
        time.sleep(3)
except Exception:
    pass

#点击进入
try:
    enter_position = pyautogui.locateOnScreen(enter, confidence=0.45)
    if enter_position:
        target_x, target_y = pyautogui.center(enter_position)
        pyautogui.click(target_x, target_y)
        enter_key=1
        time.sleep(3)
except Exception:
    pass

#点击跳过
try:
    skip_position = pyautogui.locateOnScreen(skip, confidence=0.6)
    if skip_position:
        target_x, target_y = pyautogui.center(skip_position)
        pyautogui.click(target_x, target_y)
        skip_key=1
        time.sleep(3)
except Exception:
    pass

#点击跳过
try:
    skip_position = pyautogui.locateOnScreen(skip, confidence=0.6)
    if skip_position:
        target_x, target_y = pyautogui.center(skip_position)
        pyautogui.click(target_x, target_y)
        skip_key=1
        time.sleep(3)
except Exception:
    pass

#加血
try:
    heal_position = pyautogui.locateOnScreen(heal, confidence=0.45)
    if heal_position:
        target_x, target_y = pyautogui.center(heal_position)
        pyautogui.click(target_x, target_y)
        heal_key=1
        time.sleep(3)
except Exception:
    pass

#choose2
try:
    choose2_position = pyautogui.locateOnScreen(choose2, confidence=0.45)
    if choose2_position:
        target_x, target_y = pyautogui.center(choose2_position)
        pyautogui.click(target_x, target_y)
        choose2_key=1
        time.sleep(3)
except Exception:
    pass

#点击跳过
try:
    skip_position = pyautogui.locateOnScreen(skip, confidence=0.6)
    if skip_position:
        target_x, target_y = pyautogui.center(skip_position)
        pyautogui.click(target_x, target_y)
        skip_key=1
        time.sleep(3)
except Exception:
    pass

#点击跳过
try:
    skip_position = pyautogui.locateOnScreen(skip, confidence=0.6)
    if skip_position:
        target_x, target_y = pyautogui.center(skip_position)
        pyautogui.click(target_x, target_y)
        skip_key=1
        time.sleep(3)
except Exception:
    pass

#continue
try:
    conti_position = pyautogui.locateOnScreen(conti, confidence=0.45)
    if conti_position:
        target_x, target_y = pyautogui.center(conti_position)
        pyautogui.click(target_x, target_y)
        conti_key=1
        time.sleep(3)
except Exception:
    pass

#离开
try:
    leave_position = pyautogui.locateOnScreen(leave, confidence=0.45)
    if leave_position:
        target_x, target_y = pyautogui.center(leave_position)
        pyautogui.click(target_x, target_y)
        leave_key=1
        time.sleep(3)
except Exception:
    pass

#confirm
try:
    confirm_position = pyautogui.locateOnScreen(confirm, confidence=0.45)
    if confirm_position:
        target_x, target_y = pyautogui.center(confirm_position)
        pyautogui.click(target_x, target_y)
        confirm_key=1
        time.sleep(3)
except Exception:
    pass