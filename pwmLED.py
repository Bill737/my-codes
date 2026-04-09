# 要使用 RPi 的 GPIO,首先自行安裝 RPi.GPIO 函式庫
import RPi.GPIO as GPIO # 將加入的函式庫命名為 GPIO
import time # 加入時間函式庫,LED閃爍延遲的時間

# 定義 LED 連接到RPi 的 GPIO 腳位
LED = 14    # LED 連接到GPIO14腳位
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)

# GPIO PIN PWM設定(初始化)
pwm = GPIO.PWM(LED, 50)   # 50H 建立PWM通道
pwm.start(0)

# 不斷執行
while True:
    try:
        for duty in range(0, 101, 5):
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.1)
            for duty in range(100, -1, -5):
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.1)
    except:
        print("Keyboard interrupt!!!!")
        pwm.stop()
        GPIO.cleanup()
        exit()