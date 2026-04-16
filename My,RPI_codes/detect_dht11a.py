# 偵測目前環境溫濕度並顯示
# 要使用 RPi 的 GPIO,首先自行安裝 RPi.GPIO 函式庫
import RPi.GPIO as GPIO # 將加入的函式庫命名為 GPIO
import time # 加入時間函式庫,LED閃爍延遲的時間
import Adafruit_DHT   # 加入DHT11 函式庫
# 初始化 RPi 的 GPIO 接腳
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIN = 23   # DHT11 GPIO 23腳位
dht11 = Adafruit_DHT.DHT11# 定義DHT11感測器

startTime = time.time()
while True:
    if time .time() - startTime >= 5:
        hum, temp = Adafruit_DHT.read_retry(dht11, PIN)
        if hum is not None and temp is not None:
            print(f"溫度: {temp:.2f}c  濕度: {hum:.2f}%")
        else:
            print("讀取 DHT11 感測器失敗")
        
        startTime = time.time()