import json
import codecs
from collections import OrderedDict

json1_file = open('ptt_0726_s.json')
json1_str = json1_file.read()
json1_data = json.loads(json1_str)
json1_data = json.loads(json1_str)[0]
print (type(json1_data))

OrderedDict(sorted(json1_data.items(), key=lambda t: len(t[0])))

print (json1_data)


    


'''
# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)
'''