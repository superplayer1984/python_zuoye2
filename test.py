# 汉字占两英文宽，则每存在一个汉字少填充一个长度
def pad_len(string, length):
    return length - len(string.encode('GBK')) + len(string)

products = [["iphone", 6888], ["MacPro", 14800], ["小米米6", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]

print("---- 商品格式 ----")
for i in range(len(products)):
    #print("%-2d%-10s%10d" % (i, products[i][0], products[i][1]))  # 遇到中文会对不齐
    print("{0:<{len1}}\t{1:<{len2}}\t{2:<{len3}}".format(i, products[i][0], products[i][1], len1=2,
                                                         len2 = pad_len(products[i][0], 10), len3 = 10))
