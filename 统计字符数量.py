#F2:字典统计
import time
start = time.process_time()

content = input("请输入内容:")
d = {}
# 用字典键不能重复的特点，就可以除去重复的字符，把字符转挨个填入字典中
set_content=set(content)
for i in set_content:
    print(type(i))
    count = content.count(i)
    d[i] = count
# 返回第一个字符,就是我们要找的次数最多的字符
for k, v in d.items():
    if 'a'<=k<='z' or 'A'<=k<='B':
        print( k, "(", v,"个)")

# your code here
print(time.process_time() - start)