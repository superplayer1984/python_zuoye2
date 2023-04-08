#初始化商品
products =[[r"iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]

dict1={}
# 汉字占两英文宽，则每存在一个汉字少填充一个长度
def pad_len(string, length):
    return length - len(string.encode('GBK')) + len(string)
print(10*"-","商品列表","-"*10)
for i in range(len(products)):
    len2 = pad_len(products[i][0], 10)
    print(f"{i:<2}\t{products[i][0]:<{len2}}\t{products[i][1]:<10}")
    dict1[i] = products[i]

judge=input("请输入商品编号：")
cart=[]
while 1:
    if(judge.isdigit() and int(judge)<len(dict1)-1):
        cart.append(dict1[int(judge)])
        print("购物车：",cart)
        judge = input("请输入商品编号：")
    elif(judge=='q'):
        break
    else:
        judge = input("请输入正确的商品编号:")