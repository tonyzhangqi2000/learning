# 单行注释
"""
多行注释
"""
def HW():
    print('Hello World!')
    print(123456)

    str1 = "abc"
    str2 = 'abc'
    print(str1 == str2)
    print(str1 is str2)

    dictl1 = {1: 10, 2: 20, 3: 30}

    for key in dictl1:
        print(key)
        print(dictl1[key])

    for value in dictl1.values():
        print(value)


    def printUserName():
        print("zxl")

        print("zxl2")


    print("调用之前")
    printUserName()
    print("调用之后")
    str3 = '''这个既可以当注释
              又可以当字符串呀！！！'''
    print(str3)
