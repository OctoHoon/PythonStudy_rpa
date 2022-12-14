import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("HoonCoding", interval=1) # 글자마다 1초씩 간격 둠
# pyautogui.write("훈코딩") # Pyautogui는 영문 숫자만 처리해서 적용 안됨


pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"])
# t e s t  순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향이 1번 l, a  입력. 엔터 입력
# automate the boring stuff / chapter20 에서 필요한 키 찾을 수 있음

# 특수 문자
# shift 4 -> $
# pyautogui.keyDown("shift") # shift 키를 누른 상태에서
# pyautogui.press("4") # 숫자 4를 입력하고
# pyautogui.keyUp("shift") # shift 키를 뗀다

# 조합키 (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # press("a)
# pyautogui.keyUp("ctrl") # Ctrl + A

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# ctrl 누르고 > alt 누르고 > shift 누르고 > A 누르고 > A 떼고 > shift 떼고 > alt 떼고 > ctrl 떼고

# pyautogui.hotkey("ctrl", "a")

import pyperclip # pip install pyperclip
# pyperclip.copy("훈코딩") # "나도코딩" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl", "v") # 클립보드에 있는 내용을 붙여넣기. 한글임에도 불구하고 가능.

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("안녕안녕")

# 자동화 프로그램 종료
# win : ctrl + alt + del -> 화면 전환
# mac : cmd + shift + option + q
