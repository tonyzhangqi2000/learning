# 练习题：
# 输入四位整数，分别取出各位数据
# 计算各位数字之和
inputValue = input("请输入四位整数：")

inputValue = int(inputValue)
a = inputValue % 10
b = (inputValue // 10) % 10
c = (inputValue // 100) % 10
d = inputValue // 1000
e = a + b + c + d

print(e)
