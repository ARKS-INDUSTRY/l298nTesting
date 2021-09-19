import RPi.GPIO as GPIO
import time

right_forward = 17
right_backward = 18
left_forward = 27
left_backward = 22


def initialise():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(right_forward, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(right_backward, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(left_forward, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(left_backward, GPIO.OUT, initial=GPIO.LOW)


def destroy():
    GPIO.output(right_forward, GPIO.LOW)
    GPIO.output(right_backward, GPIO.LOW)
    GPIO.output(left_forward, GPIO.LOW)
    GPIO.output(left_backward, GPIO.LOW)
    GPIO.cleanup()


def main():
  timeSleep = time.sleep(1)
  while True:
    initialise()
    GPIO.output(right_forward, GPIO.HIGH)
    timeSleep
    GPIO.cleanup()
    initialise()
    GPIO.output(right_backward, GPIO.HIGH)
    timeSleep
    GPIO.cleanup()
    initialise()
    GPIO.output(left_forward, GPIO.HIGH)
    timeSleep
    GPIO.cleanup()
    initialise()
    GPIO.output(left_backward, GPIO.HIGH)
    timeSleep
    GPIO.cleanup()
    initialise()
    GPIO.output(right_forward, GPIO.HIGH)
    GPIO.output(left_forward, GPIO.HIGH)
    timeSleep
    GPIO.cleanup()
    initialise()
    GPIO.output(right_backward, GPIO.HIGH)
    GPIO.output(left_backward, GPIO.HIGH)
    timeSleep
    GPIO.cleanup()
    initialise()
    GPIO.output(right_forward, GPIO.HIGH)
    GPIO.output(left_backward, GPIO.HIGH)
    timeSleep
    GPIO.cleanup()
    initialise()
    GPIO.output(right_backward, GPIO.HIGH)
    GPIO.output(left_forward, GPIO.HIGH)
    timeSleep
    GPIO.cleanup()
    initialise()


if __name__ == '__main__':
    try:
        main()
    # When 'Ctrl+C' is pressed, the child program
        # destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()
        print("end")