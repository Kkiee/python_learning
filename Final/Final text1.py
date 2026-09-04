try:
    a = float(input("请输入数字a："))
    b = float(input("请输入数字b："))
    res = a / b
    print(f"a ÷ b = {res}")
except ZeroDivisionError:
    print("错误：除数b不能为0！")
except ValueError:
    print("错误：输入的内容不是有效数字！")