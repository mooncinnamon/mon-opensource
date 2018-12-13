# 영화의 리뷰 모두 저장

from urllib.request import urlopen
from bs4 import BeautifulSoup
import time; # 수행 시간 측정을 위해

# 웹 크롤링 직전 시간 출력
local_time = time.asctime(time.localtime(time.time()))
print(local_time)

# 리뷰 개수 구하기
url = 'https://movie.daum.net/moviedb/grade?movieId=95306&type=netizen&page=1'
webpage = urlopen(url)
source = BeautifulSoup(webpage, 'html5lib')
review = source.find('span', {'class': 'txt_menu'})
# 페이지당 리뷰가 10개 있으므로 총 리뷰 개수를 10으로 나누어 페이지 개수를 구함
t = review.get_text().strip().replace('(', '').replace(')', '').replace(',', '')
page_no = int(int(t)/10) + 1

# 전체 리뷰를 리스트에 저장
review_list = []
for n in range(10):
	url = 'https://movie.daum.net/moviedb/grade?movieId=95306&type=netizen&page={}'.format(n + 1)
	webpage = urlopen(url)
	source = BeautifulSoup(webpage, 'html5lib')
	reviews = source.find_all('p', {'class': 'desc_review'})
	for review in reviews:
		review_list.append(review.get_text().strip().replace('\n', '').replace('\t', '').replace('\r', ''))

# 전체 리뷰 정보를 파일에 저장
file = open('mon-test', 'w', encoding = 'utf-8')	
for review in review_list:
	file.write(review + '\n')

# 웹 크롤링 후 시간 출력
local_time = time.asctime(time.localtime(time.time()))
print(local_time)

file.close()
