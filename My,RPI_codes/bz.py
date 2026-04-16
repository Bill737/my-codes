import RPi.GPIO as GPIO
import time

# 設定模式
GPIO.setmode(GPIO.BCM)
buzzer_pin = 12
GPIO.setup(buzzer_pin, GPIO.OUT)

# 初始化 PWM (設定初始頻率為 440Hz)
pwm = GPIO.PWM(buzzer_pin, 440)
pwm.start(0) # 初始佔空比為 0 (無聲)

# 音符頻率表
TONES = {
    'G3': 196, 'A3': 220, 'B3': 247,
    'C4': 262, 'D4': 294, 'E4': 330, 'F4': 349, 'G4': 392, 'A4': 440,
    'REST': 0
}

# 旋律定義：(音符, 拍子長度)
# 拍子長度 1.0 = 1秒，可自行縮放
voyager_farewell = [
    ('G3', 0.8), ('C4', 0.8), ('D4', 0.8), ('E4', 1.6),
    ('G4', 0.8), ('E4', 0.8), ('D4', 1.6),
    ('C4', 0.8), ('A3', 0.8), ('C4', 0.8), ('G3', 1.6),
    ('REST', 0.4),
    ('G3', 0.4), ('A3', 0.4), ('C4', 0.8), ('D4', 0.8), ('C4', 2.0)
]

def play_tone(frequency, duration):
    if frequency == 0:
        pwm.ChangeDutyCycle(0)
    else:
        pwm.ChangeFrequency(frequency)
        pwm.ChangeDutyCycle(50) # 50% 佔空比產生標準方波
    
    time.sleep(duration * 0.9) # 播放時間
    pwm.ChangeDutyCycle(0)     # 音符間的極短停頓
    time.sleep(duration * 0.1)

try:
    print("遠航星正在發送最後的訊號...")
    for note, duration in voyager_farewell:
        play_tone(TONES[note], duration)

except KeyboardInterrupt:
    print("\n通訊中斷。")

finally:
    pwm.stop()
    GPIO.cleanup()