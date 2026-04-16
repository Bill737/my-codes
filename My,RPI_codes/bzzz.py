
# 使用 Raspberry Pi 的 GPIO 12 連接 Buzzer，通過 PWM 方式播放《小蜜蜂》旋律
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
    'Rest': 0,
}

melody = [
    ('Mi', 0.25), ('Mi', 0.25), ('So', 0.25), ('So', 0.25), ('La', 0.25), ('La', 0.25), ('So', 0.5),
    ('Fa', 0.25), ('Fa', 0.25), ('Mi', 0.25), ('Mi', 0.25), ('Re', 0.25), ('Re', 0.25), ('Do', 0.5),
    ('Mi', 0.25), ('Mi', 0.25), ('So', 0.25), ('So', 0.25), ('La', 0.25), ('La', 0.25), ('So', 0.5),
    ('Fa', 0.25), ('Fa', 0.25), ('Mi', 0.25), ('Mi', 0.25), ('Re', 0.25), ('Re', 0.25), ('Do', 0.5),
]

pause = 0.05
duty_cycle = 50


def play_note(note_name, duration=0.3, duty=50):
    frequency = notes.get(note_name)
    if frequency is None:
        raise ValueError(f"Unknown note: {note_name}")
    if frequency == 0:
        pwm.ChangeDutyCycle(0)
        time.sleep(duration)
        return
    pwm.ChangeFrequency(frequency)
    pwm.ChangeDutyCycle(duty)
    time.sleep(duration)
    pwm.ChangeDutyCycle(0)


if __name__ == '__main__':
    try:
        print('Playing 小蜜蜂 on GPIO 12...')
        for note_tuple in melody:
            note_name, note_duration = note_tuple
            print(f'Playing {note_name} ({note_duration}s)')
            play_note(note_name, note_duration, duty=duty_cycle)
            time.sleep(pause)
    except KeyboardInterrupt:
        print('\nInterrupted by user.')
    finally:
        pwm.stop()
        GPIO.cleanup()
