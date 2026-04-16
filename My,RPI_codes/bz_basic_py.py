# 使用 Raspberry pi 的GPIO 12 連接一個 Buzzer，通過 PWM 方式控制 Buzzer 發出 Do, Re, Mi, Fa, So, La, Si
import time
import RPi.GPIO as GPIO

BZ = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(BZ, GPIO.OUT)

pwm = GPIO.PWM(BZ, 440)
pwm.start(0)

notes = {
    'Do': 523,
    'Re': 587,
    'Mi': 659,
    'Fa': 698,
    'So': 784,
    'La': 880,
    'Si': 988,
}

def play_note(note_name, duration=0.5, duty=50):
    """Play a musical note for a specified duration."""
    frequency = notes.get(note_name)
    if frequency is None:
        raise ValueError(f"Unknown note: {note_name}")
    pwm.ChangeFrequency(frequency)
    pwm.ChangeDutyCycle(duty)
    time.sleep(duration)
    pwm.ChangeDutyCycle(0)


def play_scale(duration=0.5, pause=0.1):
    for note in ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Si']:
        print(f"Playing {note}")
        play_note(note, duration)
        time.sleep(pause)


if __name__ == '__main__':
    try:
        print('Playing Do Re Mi Fa So La Si on GPIO 12...')
        play_scale()
    except KeyboardInterrupt:
        print('\nInterrupted by user.')
    finally:
        pwm.stop()
        GPIO.cleanup()
