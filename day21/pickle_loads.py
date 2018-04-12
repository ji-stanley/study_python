# __author__: Stanley
# date: 2018/4/12

import pickle


def foo():
    print("foo")


with open('pickle_text', 'rb') as f:
    data = f.read()
    data = pickle.loads(data)
    data()
