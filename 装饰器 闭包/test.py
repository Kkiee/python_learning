def outer(func):
    def inner():
        print("我睡觉了")
        func()
        print("我起床了")

    return inner

# 给sleep函数增加一些功能
@outer
def sleep():
    import time
    import random
    print("睡眠中......")
    time.sleep(random.randint(1,5))

sleep()