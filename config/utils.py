import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from server.models import Tag

GPIO.setwarnings(False)

rfid = SimpleMFRC522()

#tags_dict = {}

#for i in range(1, 100+1):
#	id, tag = rfid.read()
#	tags_dict[str(i)] = id
#	time.sleep(1.5)
#	print(i)

#with open('tags_file.txt', 'w') as tags_file:
#	for key, value in tags_dict.items():
#		tags_file.write(f'{key}:{value}\n')

def get_tag_id():
	tag_id, value = rfid.read()
	return str(tag_id)

def tag_exists(tag_id: str):
	queryset = Tag.objects.filter(tag_id=tag_id)
	exists = queryset.exists()
	return (queryset, exists)

def check_tags():
	print('Ready to scan tags...')
	tag_id = get_tag_id()
	queryset, tag_in_db = tag_exists(tag_id)


