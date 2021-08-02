import json

with open('pictures.json') as f:
    data = json.load(f)

for animal in data['dogs']:
    print (animal['image'])
