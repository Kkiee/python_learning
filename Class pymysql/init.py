class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    # 单独定义打印方法，把逻辑封装在类里
    def print_info(self, index):
        print(f"学生{index}信息录入完成，信息为：【学生姓名：{self.name}，年龄：{self.age}，地址：{self.address}】")

if __name__ == '__main__':
    total_students = 10
    students = []

    for i in range(1, total_students + 1):
        print(f"当前录入第{i}位学生信息，总共需录入{total_students}位学生信息")
        name = input("请输入学生姓名：")
        age = input("请输入学生年龄：")
        address = input("请输入学生地址：")

        stu = Student(name, age, address)
        students.append(stu)
        # 调用类的方法打印，主程序更简洁
        stu.print_info(i)
        print()