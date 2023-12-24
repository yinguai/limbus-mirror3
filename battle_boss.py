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

boss = "./battle/boss.png"
to_battle = "./battle/to_battle.png"
battle_enter = "./battle/battle_enter.png"
win_rate = "./battle/win_rate.png"
start = "./battle/start.png"
confirm = "./battle/confirm.png"
ego = "./battle/ego.png"
select = "./battle/select.png"


try:
    boss_position = pyautogui.locateOnScreen(boss, confidence=0.5)
    if boss_position:
        target_x, target_y = pyautogui.center(boss_position)
        pyautogui.click(target_x, target_y)
        print("boss已点击")
        time.sleep(3)
except Exception:
    pass

#进入
try:
    battle_enter_position = pyautogui.locateOnScreen(battle_enter, confidence=0.45)
    if battle_enter_position:
        target_x, target_y = pyautogui.center(battle_enter_position)
        pyautogui.click(target_x, target_y)
        time.sleep(10)
        print("进入已点击")
except Exception:
    pass

#to battle
try:
    to_battle_position = pyautogui.locateOnScreen(to_battle, confidence=0.8)
    if to_battle_position:
        target_x, target_y = pyautogui.center(to_battle_position)
        pyautogui.click(target_x, target_y)
        to_battle_key=1
        time.sleep(10)
except Exception:
    pass

#自动p
win_rate_key = 0
start_key= 0
try:
    while not win_rate_key:
        win_rate = "./battle/win_rate.png"
        if click_image(win_rate):
            start_key = 1
            time.sleep(2)  # 点击成功后等待5秒

        if start_key == 1 and click_image(start):
            win_rate_key = 0
            start_key = 0
            time.sleep(45)  # 点击成功后等待15秒
except Exception:
    pass

#选择礼物
#选择ego礼物
try:
    ego_position = pyautogui.locateOnScreen(ego, confidence=0.6)
    if ego_position:
        target_x, target_y = pyautogui.center(ego_position)
        pyautogui.click(target_x, target_y)
        ego_key=1
        time.sleep(5)
except Exception:
    pass

try:
    select_position = pyautogui.locateOnScreen(select, confidence=0.6)
    if select_position:
        target_x, target_y = pyautogui.center(select_position)
        pyautogui.click(target_x, target_y)
        select_key=1
        time.sleep(5)
except Exception:
    pass


try:
    confirm_position = pyautogui.locateOnScreen(confirm, confidence=0.6)
    if confirm_position:
        target_x, target_y = pyautogui.center(confirm_position)
        pyautogui.click(target_x, target_y)
        confirm_key=1
        time.sleep(5)
except Exception:
    pass