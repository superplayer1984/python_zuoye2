# coding:utf-8;

s = "上海"
left = 0
right = len(s) - 1

while left <= right:
    if s[left] == s[right]:
        left += 1
        right -= 1
    else:
        break
if left < right:
    # print('{}是回文字符串！！！'.format(s))
    print("‘%s’不是回文字符串" % s)
else:
    # print('{}不是回文字符串！！！'.format(s))
    print("‘%s‘是回文字符串" % s)
