# Window 다루기. 윈도우에서만 가능
import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창 정보 가져옴
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기 정보 (width, height)
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보
# pyautogui.click(fw.left + 20, fw.top + 20) # 창의 좌표 기준으로 마우스 클릭
#
#
# for w in pyautogui.getAllWindows():
#     print(w) # 모든 윈도우 가져오기

# for w in pyautogui.getWindowsWithTitle("제목 없음"): # 메모장이나 그림판으로 실습
#     print(w)
#
# w = pyautogui.getWindowsWithTitle("제목 없음")[0]
# print(w)
# if w.isActive == False: # 현재 활성화가 되지 않았다면
#     w.activate() # 활성화 (맨 앞으로 가져오기)
#
# if w.isMaximized == False: # 현재 최대화가 되지 않았다면
#     w.maximize() # 최대화
#
# if w.isMinimized == False: # 현재 최소화가 되지 않았다면
#     w.minimize() # 최소화
#
# pyautogui.sleep(1)
# w.restore() # 화면 원복
#
# w.close() # 윈도우 닫기