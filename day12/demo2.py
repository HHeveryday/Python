class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.__age = age  # 年龄不希望在类的外部使用

    def show(self):
        print(self.name, self.__age)


stu1 = Student('张三', 20)
stu1.show()

# 在类的外部使用name和age
print(stu1.name)
# print(stu1.__age)
# print(dir(stu1))
print(stu1._Student__age)  # 在类的外面可以通过_Student__age进行访问
