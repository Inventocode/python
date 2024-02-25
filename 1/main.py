from gpiozero import DistanceSensor,LED
import RPi.GPIO as GPIO
import time,os,math

# rgb灯 BOARD
r,g,b = 13,11,15
# 各灯亮起时间 秒
rt,yt,gt = 10,3,7
# 超声波传感器 BRM
dis = DistanceSensor(19,26,max_distance=2)
# 抓拍距离 米
capture_distance = 0.7
# 抓拍间隔 秒
capture_interval = 2
# 警报灯 BRM
alert_led = LED(13)
# 警报声音效
alert_audio = './media/alert.mp3'
# 抓拍图片保存路径
save_path = './image'
# 启用语音播报
enable_tts = True
# 语音路径
tts_path = './media/number'

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
def sleep(t,end=1):
    for i in range(t+end-1,end-1,-1):
        if enable_tts:
            os.system('mpg123 -q '+tts_path+'/'+str(i)+'.mp3 &')
        time.sleep(1)
while True:
    GPIO.output(g,1)
    sleep(gt,4)
    for i in range(yt,0,-1):
        if enable_tts:
            os.system('mpg123 -q '+tts_path+'/'+str(i)+'.mp3 &')
        GPIO.output((r,g),1)
        time.sleep(0.5)
        GPIO.output((r,g),0)
        time.sleep(0.5)
    GPIO.output(r,1)
    capture_time = time.time()
    end_time = time.time() + rt
    while time.time() < end_time:
        if dis.distance < capture_distance:
            alert_led.on()
            if time.time() > capture_time:
                capture_time = time.time() + capture_interval
                save()
                os.system('mpg123 -q media/alert.mp3 &')
        else:
            alert_led.off()
        if (end_time - time.time()) % 1 < 0.001:
            os.system('mpg123 -q '+tts_path+'/'+str(math.floor(end_time-time.time()+1))+'.mp3 &')
    alert_led.off()
    GPIO.output(r,0)