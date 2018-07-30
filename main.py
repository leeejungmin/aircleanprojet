#led적용하기 전

import sys
import os
# 쓰레딩을 위한 모듈
import threading
import time
from con_moteur import control
from data_API_Pou import findDustGrade, findLocation
# findWeather 나중에 추가해보도록 하자
#GPIO interrupt를 위한 모듈
import RPi.GPIO as GPIO


# global 변수 선언
# 위치정보 저장 초기값은 -1 로 설정
location = -1

'''
버튼 설정은 나중에 하자
def button_operate():
    while True:
        if not 'event' in locals():
            event = GPIO.add_event_detect(getButton(), GPIO.RISING, callback=control(dustGrade), bouncetime=200)
        else:
            time.sleep(100)
'''


'''

led 작업은 나중에 하도록

def LED_operate():
    # threading.Timer(주기, 콜백함수)로 4분마다 실행
    LEDTimer = threading.Timer(240,LED_operate)
    
    # 글로벌 변수 선언
    global location
    
    try:
        # location 설정은 한번만 한다.
        if (location == -1):
            # API값을 받기 전에는 보통으로 설정
            #setLED(1)
            # 위치가 없을시에는 부산의 미세먼지를 기준으로 LED 셋팅
            #setLED(findDustGrade('부산'))
            findDustGrade('부산')
            print("초기값 : 부산의 미세먼지를 기준으로 LED가 셋팅되었습니다.")
        # 아이피 기반으로 location 설정 어떻게 method 찾음 ????????????
            location = findLocation()
            print("현재 고래의 위치: " + location)
            # 위치를 받아올 경우 미세먼지를 다시 설정
            #setLED(findDustGrade(location))
            findDustGrade(location)
            print(location + "의 미세먼지를 기준으로 LED가 다시 셋팅되었습니다.")
    
        # location 설정이 되어있을 경우
        else:
            # 미세먼지를 기준으로 LED셋팅
            setLED(findDustGrade(location))
            print(location + "의 미세먼지를 기준으로 LED가 셋팅되었습니다.")
    except:
    pass
    #필요없을듯
    LEDTIMER.start()
'''



try:
    #모터를 쓰레드를 이용하여 동작
    #여기서 실시간으로 정보를 받아서 보여주나 ?? 아니면 dustdegree 설정해줘야??
    moteur_thread = threading.Thread(target=control)
    moteur_thread.start()

except:
    pass

