class Student:  # 由一个单词或多个单词组成，首字母大写
    native_pace = '四川'  # 直接写在类里的变量，称为类属性

    def __init__(self, name, age):
        self.name = name  # self.name 称为实体属性， 进行了一个赋值操作，将局部变量的name的值付给实体属性
        self.name = name  # self.name 称为实体属性， 进行了一个赋值操作，将局部变量的name的值付给实体属性
        self.age = age
# 实例方法

    def eat(self):
        print('学生在吃饭。。。')

    # 静态方法
    @staticmethod
    def method():
        print('使用了staticmetho进行修饰，所以我是静态方法')
    # 类方法

    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')

# 定义在类之外的称为函数，在类之内的定义称为方法


def drink():
    print('喝水')


# 类属性的使用方法
print(Student.native_pace)
stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace = '天津'
print(stu1.native_pace)
print(stu2.native_pace)

print('===============类方法的使用=====================')
Student.cm()
print('===============静态方法的使用=====================')
Student.method()
