class Person(object):  # 继承object类
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, num) -> None:
        super().__init__(name, age)
        self.num = num


class Teacher(Person):
    def __init__(self, name, age, teachofyear) -> None:
        super().__init__(name, age)
        self.teachofyear = teachofyear


stu = Student('张三', 20, '1002')
teacher = Teacher('李四', 34, 5)
stu.info()
teacher.info()
