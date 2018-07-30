import requests
from bs4 import BeautifulSoup
import json


# 요청 가능 시도 이름 (서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종)
def findDustGrade(station):
    # 요청을 보낼 url을 만들자
    url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName='
    # 나중에 station name을 변경할 수 있도록 밖으로 뺌
    stationName = station
    params = '&numOfRows=50&ServiceKey=utabAdXUUw%2FXTvd5HyygbTOlQCnLD7PIQEd0as%2FADJ6CrpAOziHUiC6gIE98SCOhLyvzzw3e80TjoK78vIBYIg%3D%3D&ver=1.3'
    # API 요청을 보냄
    r = requests.get(url + stationName + params)

    # Beautifulsoup를 이용해서 파싱
    soup = BeautifulSoup(r.text, 'xml')
    # 원하는 태그를 찾음 나는 미세먼지중에서 pm25를 기준으로 미세먼지 농도를 표시할것이다.
    pmGrade = soup.find_all('pm25Grade1h')

    # 내가 원하는 지역의 미세먼지 평균값을 계산
    sum = 0  # 모든 미세먼지 수치를 더하기 위한 인덱스
    index = 0  # 나누기 위한 인덱스
    for i in pmGrade:
        # 값이 있는 경우 더함
        if i.get_text().isdigit():
            sum = sum + int(i.get_text())
            index = index + 1

    # index가 0일 경우 계산할 수 없으니 예외 처리
    if index != 0:
        # 미세먼지 농도의 평균값을 계산
        avg = sum / index
        # 평균값을 반올림 하여 리턴
        return round(avg)
    else:
        # 값이 제대로 안나올경우 -1을 리턴
        return -1


# 아이피를 기반으로 위치정보를 리턴
def findLocation():
    try:
        # 아이피 기반으로 위치정보를 받아옴
        r = requests.get("https://geoip-db.com/json")

        # 위치에대한 다앙한 정보 리턴
        # data['city']에 도시에대한 정보가 영문으로 들어있음
        # city DB정보 - https://dev.maxmind.com/geoip/geoip2/geolite2/
        data = r.json()

        # 미세먼지 API가 제공해주는 지역
        # 서울, 부산, 대구, 인천, 광주, 대전,
        # 울산, 경기, 강원, 충북, 충남, 전북,
        # 전남, 경북, 경남, 제주, 세종
        if data['city'] == 'Seoul':
            return '서울'
        elif data['city'] == 'Busan':
            return '부산'
        elif data['city'] == 'Daegu':
            return '대구'
        elif data['city'] == 'Incheon':
            return '인천'
        elif data['city'] == 'Gwangju':
            return '광주'
        elif data['city'] == 'Daejeon':
            return '대전'
        elif data['city'] == 'Ulsan':
            return '울산'
        elif data['city'] == 'Gyeonggi-do':
            return '경기'
        elif data['city'] == 'Gangwon-do':
            return '강원'
        elif data['city'] == 'North Chungcheong':
            return '충북'
        elif data['city'] == 'Chungcheongnam-do':
            return '충남'
        elif data['city'] == 'Jeollabuk-do':
            return '전북'
        elif data['city'] == 'Jeollanam-do':
            return '전남'
        elif data['city'] == 'Gyeongsangbuk-do':
            return '경북'
        elif data['city'] == 'Gyeongsangnam-do':
            return '경남'
        elif data['city'] == 'Jeju-do':
            return '제주'
        else:
            return '서울'
    except:
        # API호출에 실패한 경우 -1 을리턴
        return -1


def findWeather(station):
    # 요청 보낼 url을 만듦
    url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?'
    # 만약 지역정보 파라미터가 들어가면 지역 날씨, 안들어가면 전국날씨가 리턴
    if station.find('서울') != -1 or station.find('경기도') != -1 or station.find('인천') != -1:
        params = 'stnId=109'
    elif station.find('강원도') != -1:
        params = 'stnId=105'
    elif station.find('충청북도') != -1:
        params = 'stnId=131'
    elif station.find('충청남도') != -1:
        params = 'stnId=133'
    elif station.find('경상북도') != -1:
        params = 'stnId=143'
    elif station.find('전라북도') != -1:
        params = 'stnId=146'
    elif station.find('전라남도') != -1:
        params = 'stnId=156'
    elif station.find('경상남도') != -1:
        params = 'stnId=159'
    elif station.find('제주도') != -1:
        params = 'stnId=184'
    # 만약 이곳에 없는면 전국날씨 보여줌
    else:
        params = 'stnId=108'

    # API요청을 보냄
    r = requests.get(url + params)

    # beautiful soup를 이용해서 파싱
    soup = BeautifulSoup(r.text, 'xml')
    # wf 태그에 있는 기상예보를 가져옮
    weather = soup.find('wf')

    # string에 있는 replace 함수를 사용하기 위해 데이터타입을 string으로 변환
    weather = weather.get_text()
    # <br />을 띄어쓰기로 바꿈
    weather = weather.replace('<br />', ' ')
    # 기상예보 정보를 마침표를 이용하여 분류
    weather = weather.split('.')
    # 기상예보정보를 첫번째 줄만 string으로 리턴
    return weather[0]


if __name__ == "__main__":
    print(findWeather('부산'))
    print(findDustGrade(findLocation()))

