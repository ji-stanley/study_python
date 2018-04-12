# __author__: Stanley
# date: 2018/4/12

import sys,os
print(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# sys.path.append()