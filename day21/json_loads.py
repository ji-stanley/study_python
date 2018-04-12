# __author__: Stanley
# date: 2018/4/12
import json

with open('json_text','r') as f:
    data = f.read()
    print(type(data))
    print(json.loads(data))
    print(type(json.loads(data)))
