#
# RGBRaspiTemp
#
# Script for check in 1 second the temperature of your Raspi, Simple! you look the single rgb led and the color show temperature. 
# created for using with octopus, but you can use everywhere.
#
#Note: make sure of the schema you want to build for the led, potentially you can use the led strip, but if you don't use external power,
# you can burn the raspi. 
#
# There is various video on youtube where explain the schema to build for stripes if you want to try.
#
#-------------------------------------------------------------
# HOW TO:
#
#  make executable:
#     $:chmod +x led.py
#
#  add to crontab with 
#     $:crontab -e
#
#  In editor add to last line:  !! Change /___folder_where_/your_put_the_file___/ with the folder
#                                  where you put the led.py file. !!!
#
#     @reboot sudo python /___folder_where_/your_put_the_file___/led.py       
#
#
#--------------------------------------------------------------
#   Author: Nowheel
#--------------------------------------------------------------
#
#  This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import time
import time, sys
from threading import Timer
import RPi.GPIO as GPIO
from gpiozero import CPUTemperature
from gpiozero import RGBLED
from colorzero import Color
from signal import pause


a = 20
b = 30
c = 40
d = 50
redPin = 13   #Set gpio pin (GPIO.BOARD format)
greenPin = 19 
bluePin = 26  
led = RGBLED(redPin, greenPin, bluePin, pwm = True)

global temp

def measure_temp():
        cpu = CPUTemperature()
        tempe = cpu.temperature
        return(tempe)
def main():
    temp = measure_temp()
    print(temp)
    if temp <= a :
#      led.color = Color('blue')
      led.pulse(fade_in_time=2, fade_out_time=2, on_color = Color("blu"), off_color = Color("dimgrey"))
    elif temp >= a and temp <= b :
#      led.color = Color('green')
      led.pulse(fade_in_time=2, fade_out_time=2, on_color = Color("green"), off_color = Color("dimgrey"))
    elif temp > b and temp <=  c :
#      led.color = Color('yellow')
      led.pulse(fade_in_time=2, fade_out_time=2, on_color = Color("blueviolet"), off_color = Color("dimgrey"))
    elif temp > c and temp < d :
#      led.color = Color('red')
      led.pulse(fade_in_time=2, fade_out_time=2, on_color = Color("red"), off_color = Color("dimgrey"))
      Timer(10, main).start()
    elif temp > d:
      led.pulse(fade_in_time=2, fade_out_time=2, on_color = Color("red"), off_color = Color("blue"))
      pause
      led.pulse(fade_in_time=2, fade_out_time=2, on_color = Color("green"), off_color = Color("white"))
      pause
      led.pulse(fade_in_time=2, fade_out_time=2, on_color = Color("red"), off_color = Color("blue"))
      pause
      led.pulse(fade_in_time=2, fade_out_time=2, on_color = Color("green"), off_color = Color("white"))
      pause

    Timer(10, main).start()

        Timer(10, main).start()

    while True:
            main()
            time.sleep(1)