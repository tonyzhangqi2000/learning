"""
练习：判断闰年
        四年一润，百年不润
        四百年再润
"""
import day01.helloworld as hw

year = int(input("输入年："))
print((year % 400) == 0 or ((year % 4) == 0 and (year % 100) != 0))


hw.HW()