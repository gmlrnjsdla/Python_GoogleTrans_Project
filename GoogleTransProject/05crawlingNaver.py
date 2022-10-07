import requests
from bs4 import BeautifulSoup

area1 = input('날씨를 알고싶은 지역을 입력하세요 :')
weather_html = requests.get('https://search.naver.com/search.naver?query={}날씨'.format(area1))

weather_soup = BeautifulSoup(weather_html.text, 'html.parser')

# 오늘 현재 온도
today_temper = weather_soup.find('div', {'class':'temperature_text'}).text
today_temper = today_temper[6:11]
print(today_temper)

# 어제와의 날씨 비교
yesterday_weather = weather_soup.find('p', {'class':'summary'}).text
yesterday_weather = yesterday_weather[:13]
print(yesterday_weather)

# 오늘 날씨(ex:맑음)
today_weather = weather_soup.find('span', {'class':'weather before_slash'}).text
print(today_weather)

# 검색된 지역 이름
area = weather_soup.find('h2', {'class':'title'}).text
print(area)

# 체감 온도
sense_temper = weather_soup.select('dl.summary_list>dd')
sense_temper = sense_temper[0].text
print(sense_temper)

# 미세먼지 정보
dust_info = weather_soup.select('ul.today_chart_list>li')
dust1 = dust_info[0].find('span', {'class':'txt'}).text
print(dust1)

# 초미세먼지 정보
dust2 = dust_info[1].find('span', {'class':'txt'}).text
print(dust2)
# dust_info[2] : 자외선 정보, dust_info[3] : 일몰시간

