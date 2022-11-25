import ssl
from selenium import webdriver

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('../res/rootca.crt')


browser = webdriver.Chrome(r"C:\Users\Admin\PycharmProjects\pythonProject2\chromedriver.exe")

browser.get("http://naver.com") # 자동화로 크롬 실행
elem = browser.find_element_by_link_text("카페")
elem.get_attribute("href")