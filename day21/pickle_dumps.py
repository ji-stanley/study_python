# __author__: Stanley
# date: 2018/4/12

import pickle

def foo():
    print("foo")

data = pickle.dumps(foo)

with open('pickle_text','wb') as f:
    f.write(data)