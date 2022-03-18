class Student():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:  # 重写__str__方法
        return '我的名字是{0}，今年{1}岁了'.format(self.name, self.age)


stu = Student('张三', 20)

print(stu)  # 默认调用__str__方法
