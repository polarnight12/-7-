#\w和\W的用法
import re
str1 = '123Qwe!_@#你我他'
print(re.findall('\w', str1))
print(re.findall('\W', str1))
#\s和\S的用法
import re
str2 = "123Qwe!_@#你我他\t \n\r"
print(re.findall('\s', str2))
print(re.findall('\S', str2))
#\w和\W的用法
import re
str3 = "123Qwe!_@#你我他\t \n\r"
print(re.findall('\d', str3))
print(re.findall('\D', str3))
#^和$的用法
import re
str4 = '你好吗，我很好'
print(re.findall('^你好', str4))
str5 = '我很好，你好'
print(re.findall('你好$', str5))
#.、*、？的用法
import re
str6 = 'abcaaabb'
print(re.findall('a.b', str6))
print(re.findall('a?b', str6))
print(re.findall('a*b', str6))
print(re.findall('a.*b', str6))
print(re.findall('a.*?b', str6))
#\转义字符的用法
import re
str7 = '\t123456'
print(re.findall('t', str7))
str8 = '\\t123456'
print(re.findall('t', str8))
str9 = r'\t123456'
print(re.findall('t', str9))
#[ ]字符集的用法
import re
str10 = 'aab abb acb azb a1b'
print(re.findall('a[a-z]b', str10))
print(re.findall('a[0-9]b', str10))
print(re.findall('a[ac1]b', str10))
#（）’分组+元字符的搭配使用
import re
str11 = '123qwer'
print(re.findall('(\w+)q(\w+)', str11))
#|逻辑或的用法
import re
str12 = '你好，女士们先生们，大家好好学习呀'
print(re.findall('女士|先生', str12))
