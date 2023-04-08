#F1:列表法
import time
start = time.process_time()
content = input("请输入内容:")
#利用集合排他性提取出列表中的元素
str_set=set(content)
#将该集合传化为列表，方便处理
str_set_list=list(str_set)
str_set_list.sort()
#初始化储存元素出现次数的列表
count=len(str_set)*[0]
#计算列表中与所找元素一致的个数
for i in range(len(str_set)):
        for j in range(len(content)):
            if str_set_list[i] == content[j]:
                count[i]=count[i]+1
for i in range(len(str_set)):
    if 'a'<=str_set_list[i]<='z' or 'A'<=str_set_list[i]<='B':
        print(f'{str_set_list[i]}({count[i]}个)')
print(time.process_time() - start)