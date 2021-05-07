'''
https://www.indetail.co.jp/blog/8431/
https://www.indetail.co.jp/blog/8947/
'''

import time
import RPi.GPIO as GPIO
import time

def f(n):
	if n <= 2:
		return 1
	else:
		return f(n - 2) + f(n - 1)

def flash():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT)
	GPIO.output(18, True)
	time.sleep(0.5)
	GPIO.output(18, False)
	GPIO.cleanup()

num=1
nextnum=1

while 1:
	nextnum = f(num)
	print(nextnum)
	flash()
	time.sleep(nextnum)
	num += 1
	
