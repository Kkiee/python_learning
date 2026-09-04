# utils. 创建列表存放1-12月天数，2月固定28天
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 循环查询，输入0退出
while True:
    month = int(input("请输入要查询的月份（输入0结束程序）："))
    if month == 0:
        print("程序结束")
        break
    # 判断月份是否合法
    if 1 <= month <= 12:
        # 列表下标从0开始，月份-utils
        days = month_days[month - 1]
        print(f"{month}月有{days}天")
    else:
        print("输入月份无效，请输入1~12之间的数字")