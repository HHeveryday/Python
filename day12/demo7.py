from telnetlib import DO


class Animal(object):
    def eat(self):
        print('动物会吃东西')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Dog(Animal):
    def eat(self):
        print('狗吃骨头')


class Person():
    def eat(self):
        print('人吃五谷杂粮')


def fun(obj):
    obj.eat()


fun(Cat())
fun(Dog())
fun(Animal())
print('===============================')
fun(Person())
