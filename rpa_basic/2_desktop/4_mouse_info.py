import pyautogui

pyautogui.FAILSAFE = False # 마우스 이동 못 해도 동작 멈추지 않음
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
# pyautogui.mouseInfo()
# x, y , R, G, B, RGB 문자
# 1005,13 58,62,108, 3A3E6C

# 마우스 포인터를 모니터 4 귀퉁이에 두면 동작 멈춤
for i in range(10):
    pyautogui.move(100, 100)