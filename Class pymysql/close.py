class Phone:
    def __init__(self):
        res = input("True还是False 5g")
        # 把输入字符串转为布尔
        res = input("True还是False 5g")
        self.__is_5g_enable = (res == "True")

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭,使用4g")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone=Phone()
phone.call_by_5g()
