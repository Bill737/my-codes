import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

# Create PWM object on GPIO 12
pwm = GPIO.PWM(12, 1000)  # 1000 Hz frequency

# Note frequencies (Hz)
notes = {
    'C4': 262, 'D4': 294, 'E4': 330, 'F4': 349, 'G4': 392,
    'A4': 440, 'B4': 494, 'C5': 523, 'D5': 587, 'E5': 659
}

# 小蜜蜂 melody (Twinkle Twinkle Little Star)
melody = [
    ('C4', 0.5), ('C4', 0.5), ('G4', 0.5), ('A4', 0.5),
    ('G4', 0.5), ('F4', 0.5), ('E4', 0.5), ('D4', 0.5),
    ('C4', 0.5), ('G4', 0.5), ('A4', 0.5), ('G4', 0.5),
    ('F4', 0.5), ('E4', 1.0)
]

def play_tone(frequency, duration):
    pwm.ChangeFrequency(frequency)
    pwm.start(50)  # 50% duty cycle
    time.sleep(duration)
    pwm.stop()
    time.sleep(0.1)  # Pause between notes

try:
    pwm.start(0)
    for note, duration in melody:
        play_tone(notes[note], duration)
finally:
    pwm.stop()
    GPIO.cleanup()