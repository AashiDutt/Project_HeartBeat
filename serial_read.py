import serial

Arduino_serial = serial.Serial("COM4", 9600)

while(True):
	my_data = Arduino_serial.readline().strip()
	print(my_data.decode())