import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pwm_pin = 33
pwm_en_pin = 23

frequency = 100
duty_cycle = 0

period = 1/frequency
high_time = 0
low_time = 0


GPIO.setup(pwm_pin, GPIO.OUT)
GPIO.setup(pwm_en_pin, GPIO.OUT)

def set_duty_cycle(new_duty_cycle):
    global duty_cycle, high_time, low_time
    duty_cycle = new_duty_cycle 
    high_time = (duty_cycle /100)*period
    low_time = period-high_time
    GPIO.output(pwm_pin, GPIO.HIGH)

def main():
    GPIO.output(pwm_en_pin, GPIO.HIGH)
    try:
        while True:
            new_duty_cycle = float(input("Enter new duty_cycle: "))
            set_duty_cycle(new_duty_cycle)

            while high_time > 0 and low_time > 0:
                GPIO.output(pwm_pin, GPIO.HIGH)
                time.sleep(high_time)
                GPIO.output(pwm_pin, GPIO.LOW)
                time.sleep(low_time)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()

