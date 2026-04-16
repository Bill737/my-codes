# 要使用 RPi 的 GPIO,首先自行安裝 RPi.GPIO 函式庫
import RPi.GPIO as GPIO # 將加入的函式庫命名為 GPIO
import time # 加入時間函式庫,LED閃爍延遲的時間

# 初始化 RPi 的 GPIO 接腳
LED = 14    # LED 連接到GPIO14腳位
PB = 4     # push Button
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(PB,GPIO.IN)
GPIO.setwarnings(False)

while True:
    try:
        GPIO.output(LED, 1-GPIO.input(PB))
        time.sleep(0.1)
    except KeyboardInterrupt:
        print("程式中斷")
        GPIO.cleanup()
        break
