import pyautogui
# 스크린 샷 찍기

# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 1016,557 64,182,224 #40B6E0 -> 임의로 색깔 있는 버튼 찍음

pixel = pyautogui.pixel(1016, 557)
print(pixel) # RGB 값 가져옴

print(pyautogui.pixelMatchesColor(1016, 557, ((64, 182, 224))))
print(pyautogui.pixelMatchesColor(1016, 557, pixel))
print(pyautogui.pixelMatchesColor(1016, 557, ((64, 182, 222))))