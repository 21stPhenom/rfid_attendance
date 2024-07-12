import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

rfid = SimpleMFRC522()

tags_dict = {}

for i in range(1, 100+1):
	id, tag = rfid.read()
	tags_dict[str(i)] = id
	time.sleep(1.5)
	print(i)

with open('tags_file.txt', 'w') as tags_file:
	for key, value in tags_dict.items():
		tags_file.write(f'{key}:{value}\n')
