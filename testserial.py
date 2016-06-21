import serial
from time import sleep

arduino = serial.Serial('/dev/ttyACM2', 9600)

arduino.write('000000')
sleep(2)
arduino.write('101010')
sleep(2)
arduino.write('010101')
sleep(2)
arduino.write('111111')
