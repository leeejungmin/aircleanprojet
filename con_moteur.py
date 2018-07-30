import RPi.GPIO as IO
import time
import data_API_Pou


pwmPin = 19
dirPin = 13

dustGrade=data_API_Pou.findWeather('부산')

#초기화를 해야 하나?
'''
def initGPIO():
    IO.setwarnings(False)
    IO.setmode(IO.BCM)
    IO.setup(pwmPin, IO.OUT)
    IO.setup(dirPin,IO.OUT)



    p = IO.PWM(pwmPin, 100)
    p.start(0)
'''

#점점 증가하다가 감소
'''
while 1:
    IO.output(dirPin, True)
    for x in range (100):
        p.ChangeDutyCycle(x)
        time.sleep(0.1)
    time.sleep(0.5)
    for x in range (100, 0, -1):
        p.ChangeDutyCycle(x)
        time.sleep(0.1)
    time.sleep(0.5)
    IO.output(dirPin, False)
    for x in range (100):
        p.ChangeDutyCycle(x)
        time.sleep(0.1)
    time.sleep(0.5)
    for x in range (100, 0, -1):
        p.ChangeDutyCycle(x)
        time.sleep(0.1)
'''
#농도 받으면 모터 속도 조절함수
def control(dustGrade):
    IO.setwarnings(False)
    IO.setmode(IO.BCM)
    IO.setup(pwmPin, IO.OUT)
    IO.setup(dirPin, IO.OUT)

    p = IO.PWM(pwmPin, 100)
    p.start(0)
    IO.output(dirPin, True)
    if dustGrade == 0: # 20속도 정함
        p.ChangeDutyCycle(20)
        time.sleep(0.1)
    elif dustGrade == 1: # 40
        p.ChangeDutyCycle(40)
        time.sleep(0.1)
    elif dustGrade == 2: # 75
        p.ChangeDutyCycle(75)
        time.sleep(0.1)
    elif dustGrade == 3: # 100
        p.ChangeDutyCycle(100)
        time.sleep(0.1)
    else :
        pass
'''
def getButton():
    return button
'''


def printTest(self):
    print("thread Test")
if __name__ == "__main__":
    try:

        control(dustGrade)


    except KeyboardInterrupt:

        control(dustGrade).cleanup()
    control(dustGrade).cleanup()

