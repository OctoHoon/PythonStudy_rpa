# 1. 그림판 실행 (단축키: win + r, 입력값 : mspaint) 및 최대화
#
# 2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력
# - 입력 글자: "참 잘했어요"
#
# 3. 5초 대기 후 그림판 종료
# 이 때, 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함

import pyautogui
import pyperclip

pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")

pyautogui.sleep(3)

w = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]

if w.isMaximized == False:
    w.maximize()

# pyautogui.mouseInfo()
fw = pyautogui.getActiveWindow()
pyautogui.click(fw.left + 340, fw.top + 75) # 이미지 찾는 방법으로도 가능
pyautogui.click(fw.left + 340, fw.top + 340) # 이미지 찾고, 그것의 상대좌표를 이용하는 방법도 가능

pyperclip.copy("참 잘했어요")
pyautogui.hotkey("ctrl", "v")

pyautogui.sleep(5)
w.close()
pyautogui.sleep(0.5)
pyautogui.press("n")
