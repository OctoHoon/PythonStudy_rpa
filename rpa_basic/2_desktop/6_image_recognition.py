import pyautogui

# file_menu = pyautogui.locateOnScreen("file_menu.png") # 화면에서 이미지 위치 찾음
# print(file_menu) # 찾은 이미지 정보 반환
# pyautogui.click(file_menu)
# pyautogui.click(file_menu.left - 200, file_menu.top + 200) # 찾은 이미지의 상대좌표 이용해 클릭도 가능

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)
#
# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen) # 이미지 찾지 못 하면 None 출력


# 찾으려는 이미지가 화면에 여러개인 경우 모두 클릭하려면
# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# 하나만 클릭하게 됨
# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)


# 속도 개선
# 1. GrayScale 
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정 # region = (x, y, width, height)
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(982, 663, 100, 170))
# pyautogui.moveTo(trash_icon)

# pyautogui.mouseInfo()
# 982, 663/ 1052, 832

# 3. 정확도 조정 # opencv install 필요
# rub_btn = pyautogui.locateOnScreen("run_button.png", confidence=0.5)
# pyautogui.moveTo(rub_btn)

# 자동화 대상이 바로 보여지지 않는 경우

# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# # if file_menu_notepad:
# #     pyautogui.click(file_menu_notepad)
# # else:
# #     print("발견 실패")
# 
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")
# 
# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png", confidence=0.9)
#     end = time.time()
#     if end - start > timeout:
#         print("시간 종료")
#         sys.exit()
#
# pyautogui.click(file_menu_notepad)

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file, confidence=0.9)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()

my_click("file_menu_notepad.png", 10)