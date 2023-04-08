import re
def phone():
    n = input("请输入一个手机号：")
    if str(n) == '0':
        print("退出校验。")
        return False
    if re.match(r'1[3,4,5,7,8]\d{9}', n) and len(n) == 11:
        print("您输入的的手机号码是：{}".format(n))
        # 中国联通：
        # 130，131，132，155，156，185，186，145，176
        if re.match(r'13[0,1,2]\d{8}', n) or \
                re.match(r"15[5,6]\d{8}", n) or \
                re.match(r"18[5,6]", n) or \
                re.match(r"145\d{8}", n) or \
                re.match(r"176\d{8}", n):
            print("该号码属于：中国联通")
        # 中国移动
        # 134, 135 , 136, 137, 138, 139, 147, 150, 151,
        # 152, 157, 158, 159, 178, 182, 183, 184, 187, 188；
        elif re.match(r"13[4,5,6,7,8,9]\d{8}", n) or \
                re.match(r"147\d{8}|178\d{8}", n) or \
                re.match(r"15[0,1,2,7,8,9]\d{8}", n) or \
                re.match(r"18[2,3,4,7,8]\d{8}", n):
            print("该号码属于：中国移动")
        elif re.match(r"133\d{8}|153\d{8}|189\d{8}`",n):
            # 中国电信
            # 133,153,189
            print("该号码属于：中国电信")

    else:
        print("请输入正确的手机号")

    return True


if __name__ == '__main__':
    m_flag = True
    while m_flag:
        m_flag = phone()
