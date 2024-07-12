from collections import Counter
from server.models import Tag

tags = {}

with open('tags_file.txt', 'rt') as file:
    entries = file.readlines()
    entries = [entry[0:-1] for entry in entries]
    # print(entries)
    
    for entry in entries:
        index, value = entry.split(':')
        tags[int(index)] = value

# check if all entries are unique
# print(len(Counter(tags)))

def show_tags():
    for i in range(1, 101):
        tag = Tag.objects.create(serial_number=i, tag_id=tags[i])
        print(tag)