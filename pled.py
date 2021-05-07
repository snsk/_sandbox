#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

r = requests.get("https://api.openweathermap.org/data/2.5/forecast?q=shinjuku&lang=Ja&units=metric&cnt=9&appid=key")
forecasts_data = json.loads(r.text)
print("today: " + forecasts_data["list"][1]["weather"][0]["description"])

status = forecasts_data["list"][1]["weather"][0]["description"]

if status == "Clouds":
    print("yellow")
    condision = "y"
elif status == "Clear":
    print("green")
    condision = "g"
elif status == "Snow" or status == "Rain" or status == "Drizzle"  or status == "Thunderstorm":
    print("red")
    condision = "r"
else:
    print("yellow")
    condision = "y"

'''
https://openweathermap.org/weather-conditions
Clouds: 曇り ＝ 黄色
Clear: 晴れ ＝ 緑
Snow: 雪 ＝ 赤
Rain: 雨 ＝ 赤
Drizzle：霧雨 ＝ 赤
Thunderstorm：雷雨 ＝ 赤
それ以外：曇り ＝ 黄色
'''

# ライブラリの読み込み
import RPi.GPIO as GPIO
import time
# GPIOピン番号の定義方法を設定する（BCM/BOARD）
GPIO.setmode(GPIO.BCM)
# 18番ピンを出力モードで初期化する
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

# LED点滅（2秒置き）を5400回=3繰り返す
if condision == "y":
    for x in xrange(5400):
        GPIO.output(23, True)
        time.sleep(1)
        GPIO.output(23, False)
        time.sleep(1)
if condision == "g":
    for x in xrange(5400):
        GPIO.output(25, True)
        time.sleep(1)
        GPIO.output(25, False)
        time.sleep(1)
if condision == "r":
    for x in xrange(5400):
        GPIO.output(18, True)
        time.sleep(1)
        GPIO.output(18, False)
        time.sleep(1)

# GPIOを解放
GPIO.cleanup()
