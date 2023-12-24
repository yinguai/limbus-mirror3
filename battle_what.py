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

what = "./what/what.png"
battle_enter = "./what/battle_enter.png"
skip = "./what/skip.png"
select = "./what/select.png"
proceed = "./what/proceed.png"
very_high = "./what/very_high.png"
high = "./what/high.png"
commence = "./what/commence.png"
continu = "./what/continue.png"
confirm = "./what/confirm.png"

try:
    what_position = pyautogui.locateOnScreen(what, confidence=0.45)
    if what_position:
        target_x, target_y = pyautogui.center(what_position)
        pyautogui.click(target_x, target_y)
        what_key=1
        print("？已经点击")
        time.sleep(3)
except Exception:
    pass

try:
    battle_enter_position = pyautogui.locateOnScreen(battle_enter, confidence=0.6)
    if battle_enter_position:
        target_x, target_y = pyautogui.center(battle_enter_position)
        pyautogui.click(target_x, target_y)
        battle_enter_key=1
        time.sleep(5)
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

#点击选择
try:
    select_position = pyautogui.locateOnScreen(select, confidence=0.4)
    if select_position:
        target_x, target_y = pyautogui.center(select_position)
        pyautogui.click(target_x, target_y)
        select_key=1
        time.sleep(3)
except Exception:
    pass

#点击跳过
try:
    skip_position = pyautogui.locateOnScreen(skip, confidence=0.4)
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

#点击选择
try:
    select_position = pyautogui.locateOnScreen(select, confidence=0.4)
    if select_position:
        target_x, target_y = pyautogui.center(select_position)
        pyautogui.click(target_x, target_y)
        select_key=1
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

#点击proceed
try:
    proceed_position = pyautogui.locateOnScreen(proceed, confidence=0.6)
    if proceed_position:
        target_x, target_y = pyautogui.center(proceed_position)
        pyautogui.click(target_x, target_y)
        proceed_key=1
        time.sleep(3)
except Exception:
    pass

#点击跳过
try:
    skip_position = pyautogui.locateOnScreen(skip, confidence=0.4)
    if skip_position:
        target_x, target_y = pyautogui.center(skip_position)
        pyautogui.click(target_x, target_y)
        skip_key=1
        time.sleep(3)
except Exception:
    pass

#选择high
try:
    high_position = pyautogui.locateOnScreen(high, confidence=0.4)
    if high_position:
        target_x, target_y = pyautogui.center(high_position)
        pyautogui.click(target_x, target_y)
        high_key=1
        time.sleep(3)
except Exception:
    pass

#选择veryhigh
try:
    very_high_position = pyautogui.locateOnScreen(very_high, confidence=0.9)
    if very_high_position:
        target_x, target_y = pyautogui.center(very_high_position)
        pyautogui.click(target_x, target_y)
        very_high_key=1
        time.sleep(3)
except Exception:
    pass

#选择commence
try:
    commence_position = pyautogui.locateOnScreen(commence, confidence=0.4)
    if commence_position:
        target_x, target_y = pyautogui.center(commence_position)
        pyautogui.click(target_x, target_y)
        commence_key=1
        time.sleep(10)
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

#点击continue
try:
    continu_position = pyautogui.locateOnScreen(continu, confidence=0.6)
    if continu_position:
        target_x, target_y = pyautogui.center(continu_position)
        pyautogui.click(target_x, target_y)
        continu_key=1
        time.sleep(3)
except Exception:
    pass

#点击confirm
try:
    confirm_position = pyautogui.locateOnScreen(confirm, confidence=0.6)
    if confirm_position:
        target_x, target_y = pyautogui.center(confirm_position)
        pyautogui.click(target_x, target_y)
        confirm_key=1
        time.sleep(3)
except Exception:
    pass