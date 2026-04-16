# 要使用 RPi 的 GPIO,首先自行安裝 RPi.GPIO 函式庫
import RPi.GPIO as GPIO # 將加入的函式庫命名為 GPIO
import time # 加入時間函式庫,LED閃爍延遲的時間
# 定義 LED 連接到RPi 的 GPIO 腳位
LED = 14    # LED 連接到GPIO14腳位
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)


while True:
    try:
        GPIO.output(LED,1)
        time.sleep(1)
        GPIO.output(LED,0)
        time.sleep(1)
    except:
        print("Keyboard interrupt!!!!")
        exit()