from gpiozero import DistanceSensor,LED
import RPi.GPIO as GPIO
import time,os

# 超声波传感器 BRM
dis = DistanceSensor(19,26,max_distance=2)
# 警报灯 BRM
alert = LED(13)
# rgb灯 BOARD
r,g,b = 13,11,15
# 各灯亮起时间 秒 s
rt,yt,gt = 10,5,5
# 抓拍图片保存路径
save_path = './image'
# 抓拍距离 米 m
capture_distance = 0.3
# 抓拍间隔 秒 s
capture_interval = 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup((r,g,b), GPIO.OUT)
GPIO.output((r,g,b),0)
def save():
    path = ft(save_path+"/%Y-%m-%d")
    if not os.path.exists(path):
        os.makedirs(path)
    os.system(ft('fswebcam --title "%Y-%m-%d %H:%M:%S" --no-timestamp -q '+save_path+'/%Y-%m-%d/%H%M%S.jpg'))
def ft(text):
    return time.strftime(text, time.localtime())
while True:
    GPIO.output(g,1)
    time.sleep(gt)
    for i in range(yt//0.5+1):
        GPIO.output((r,g),1)
        time.sleep(0.25)
        GPIO.output((r,g),0)
        time.sleep(0.25)
    GPIO.output(r,1)
    capture_time = time.time()
    end_time = time.time() + rt
    while time.time() < end_time:
        print(dis.distance)
        if dis.distance < capture_distance:
            alert.on()
            if time.time() > capture_time:
                capture_time = time.time() + capture_interval
                save()
                os.system('mpg123 ./alert.mp3')
        else:
            alert.off()
    alert.off()
    GPIO.output(r,0)
