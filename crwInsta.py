# crawling Instagram Hashtag #김똥꾸
# -*- coding=utf-8 -*-
import selenium.webdriver as webdriver	

# 검색할 태그명
tag = '김똥꾸'

# 인스타그램 태그 페이지 URL	
url = 'https://www.instagram.com/explore/tags/김똥꾸/'

# 크롬창을 띄우지 않는 옵션을 넣는다	
options = webdriver.ChromeOptions()	
options.add_argument('headless')	
options.add_argument('disable-gpu')	
driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)	

# 암시적으로 최대 5초간 기다린다
driver.implicitly_wait(5)

# url에 접근한다
driver.get(url)

# 게시물 개수 정보를 가져온다
totalCount = driver.find_element_by_class_name('g47SY').text 

# 게시물 개수를 출력한다
print("totalCount :", totalCount)	

# 열어둔 webdriver를 종료
driver.quit()
