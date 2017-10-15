import RPi.GPIO as GPIO
import time
from pygame import mixer
import os
GPIO.setmode(GPIO.BCM)
TRIG1=18
TRIG2=14
ECHO1=24
ECHO2=17
while True:
 print "Measuring distance1"
 GPIO.setup(TRIG1,GPIO.OUT)
 GPIO.setup(ECHO1,GPIO.IN)
 while True:
  GPIO.output(TRIG1,False)
  print "Waiting for sensor1"
  time.sleep(2)
  GPIO.output(TRIG1,True)
  time.sleep(0.00001)
  GPIO.output(TRIG1,False)
  while GPIO.input(ECHO1)==0:
   pulse_start=time.time()
  while GPIO.input(ECHO1)==1:
   pulse_end=time.time()
  pulse_duration=pulse_end-pulse_start
  distance=pulse_duration*17150
  distance=round(distance,2)
  if distance > 2 and distance < 400:
     print "Distance1:",distance-0.5,"cm"
     if distance > 2 and distance < 100:
       os.system("omxplayer obstacle_ahead.mp3")
       os.system("fswebcam image.jpg")
       import os
       from pygame import mixer
       from PIL import Image
       from PIL import ImageChops
       im1 = Image.open("image1.jpg")
       im2 = Image.open("image.jpg")
       dif1 = ImageChops.difference(im1, im2)
       if dif1<100.00:
          os.system("omxplayer chair.mp3")
       else:
           os.system("omxplayer notchair.mp3")




       os.system("omxplayer other_side.mp3")
             
       continue
     else:
       os.system("omxplayer move_ahead.mp3")
       break
  else:
     print "Out of range1"
 print "Measuring distance2"
 GPIO.setup(TRIG2,GPIO.OUT)
 GPIO.setup(ECHO2,GPIO.IN)
 while True:
  GPIO.output(TRIG2,False)
  print "Waiting for sensor2"
  time.sleep(2)
  GPIO.output(TRIG2,True)
  time.sleep(0.00001)
  GPIO.output(TRIG2,False)
  while GPIO.input(ECHO2)==0:
   pulse_start=time.time()
  while GPIO.input(ECHO2)==1:
   pulse_end=time.time()
  pulse_duration=pulse_end-pulse_start
  distance=pulse_duration*17150
  distance=round(distance,2)
  if distance > 2 and distance < 400:
     print "Distance2:",distance-0.5,"cm"
     if distance > 2 and distance < 80:
       os.system("omxplayer obstacle_behind.mp3")
       break
     else:
       os.system("omxplayer move_ahead.mp3")
       break
  else:
     print "Out of range"
time.sleep(5)

     

