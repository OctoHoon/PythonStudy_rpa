import pyautogui

# pyautogui.sleep(3) # 3초 대기
# print(pyautogui.position()) # File 버튼의 좌표 (1003, 12) 알아냄

#pyautogui.click(1003, 12, duration=1) # 1초 동안 좌표로 이동 후 마우스 클릭

# pyautogui.click()
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown() # 마우스 버튼 누른 상태
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp() # 마우스 버튼 뗀 상태

pyautogui.sleep(3)
# pyautogui.rightClick()
# pyautogui.middleClick()

#print(pyautogui.position()) # 메모장 타이틀 잡고 드래그 연습
#pyautogui.moveTo(746, 147)
#pyautogui.drag(100, 0) # 상대 좌표
#pyautogui.drag(100, 0, duration=0.25) # 너무 빠른 동작으로 drag 수행이 안 될 때는 duration을 주면 됨
#pyautogui.dragTo(1278, 800, duration=0.25)
pyautogui.scroll(-300) # 양수이면 위 방향으로 300만큼 스크롤.
# -300 : 아래 방향으로 300만큼 스크롤

