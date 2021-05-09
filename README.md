# Magic-Gesture-Wand
Code for ESP8266 and MPU6050 to control Mouse with Gesture

<a href="https://ibb.co/bRQ1x84"><img src="https://i.ibb.co/Z1Gd3kQ/IMG-20210507-231920.jpg" alt="IMG-20210507-231920" border="0"></a>

<a href="https://ibb.co/N377phb"><img src="https://i.ibb.co/9vGG2XS/IMG-20210509-142740.jpg" alt="IMG-20210509-142740" border="0"></a>

<a href="https://ibb.co/SwRVh5N"><img src="https://i.ibb.co/hFD2PLs/IMG-20210509-151136.jpg" alt="IMG-20210509-151136" border="0"></a>

## Steps:
1. Flash the `esp8266_mpu6050.ino` code to ESP8266 using Arduino IDE
2. Connect the Circuit as Follows: MPU6050 SDA-> D2 , MPU6050 SCL-> D1 , BUTTON PIN -> D3 , And power pin to 3,3V and GND

<a href="https://ibb.co/k8txdpc"><img src="https://i.ibb.co/J79KhNk/Screenshot-from-2021-05-09-16-11-32.png" alt="Screenshot-from-2021-05-09-16-11-32" border="0"></a>
3. Install python packages `pip3 install pyserial pyautogui`
4. Then for reading the serial data in `read_mousecontrol.py` edit the Port ID (For Windows find it in Device Manager eg:COM1,COM2 , in Linux run command `lsusb`) and run the code using `python3 read_mousecontrol.py`.
5. Then Whenever You press the button you can control the position of the mouse
