#F1:列表或字符串统计
content=input("请输入内容：")
dict = {}
# 循环遍历列表或字符串，如果不在则创建（key,value)，如果字符在字典中则值加1
for i in content:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

# 根据value值，找对应的key值，打印出字符出现次数
for k, v in dict.items():
    if 'a'<=k<='z' or 'A'<=k<='B':
        print( k, "(", v,"个)")



