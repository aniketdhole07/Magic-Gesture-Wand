import  sys
import time 
import serial
import pyautogui

ArduinoSerial=serial.Serial('/dev/ttyUSB0',9600)  #Specify the correct COM port
time.sleep(1)                             #delay of 1 second

while 1:
   try:
   	data=str(ArduinoSerial.readline().decode('ascii'))   #read the data
   	(x,y)=data.split(":")           # assigns to x,y and z
   	print(x,y)                      # read the cursor's current position
   	(x,y)=(int(x),int(y))                   #convert to int
   	pyautogui.moveTo(700+x, 550+y)          #move cursor to desired position from centre of screen
   except:
   	pass
     
