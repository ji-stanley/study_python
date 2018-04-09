# __author__: Stanley
# date: 2018/4/8

import re
# ret = re.findall('w\w{2}l','hello world')
# print(ret)

#  . 匹配任意一个字符
print(re.findall('w..l','hello world'))

# ^ 以什么为开头
print(re.findall('^hello','aahello world'))
print(re.findall('^hello','hello world'))

# $ 以什么为结尾
print(re.findall('world$','aahello world'))
print(re.findall('world$','aahello worldaa'))

# \ 去除2元字符的特殊意义，给字符赋予特殊功能。

# \b    匹配一个特殊字符边界，也就是指单词和空格间的位置。
# 例如，“er\b”可以匹配“never”中的“er”，但不能匹配“verb”中的“er”。
print(re.findall(r'abc\b','wer wqe rabc www'))

# \d    匹配一个数字字符。等价于[0-9]。
print(re.findall('\d{5}',"afd1231wfafas2342414214324dfadfa"))

# \D    匹配一个非数字字符。等价于[^0-9]。
print(re.findall('\D{5}',"afd1231wfafas2342414214324dfadfa"))

# \s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于[ \f\n\r\t\v]。
print(re.findall('\s',"afd12 31wfafas 23424 1421432 4dfadfa"))

# \S	匹配任何非空白字符。等价于[^ \f\n\r\t\v]。
print(re.findall('\S',"afd1231wfafas2342414214324dfadfa"))

# \w	匹配包括下划线的任何单词字符。等价于“[A-Za-z0-9_]”。
print(re.findall('\w{2}',"afd1 231wfa fas23 424142 14324dfadfa"))

# \W	匹配任何非单词字符。等价于“[^A-Za-z0-9_]”。
print(re.findall('\W{3}',"afd123 1wfafa     s23 424142      14324df adfa"))


# 匹配出满足条件的第一个结果
print(re.search('abc','abcfdaabc'))
print(re.search('abc','abcfdaabc').group())


# re.split 分成列表
print(re.split('[a,c]','abcfasdfasf'))

# re.sub 替换
s = 'abcfdasfasabc'
print(s)
print(re.sub('a.c','a4c',s,1))

