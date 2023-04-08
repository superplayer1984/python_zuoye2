#F2:字典统计
a=input("请输入a:")
b=input("请输入b的值:")

def fun(str0):
    # 用字典键不能重复的特点，就可以除去重复的字符，把字符转挨个填入字典中
    d = {}
    set_str0=set(str0)
    set_str0=list(set_str0)
    set_str0.sort()
    for i in set_str0:
        count = str0.count(i)
        d[i] = count
    return d

d1=fun(a)
d2=fun(b)

if d1==d2:
    print("相等")
else:
    print("不相等")

