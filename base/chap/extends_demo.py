# 开发者: 五行缺雨

# 时间: 2020/12/17 0:06
# 继承和多态

# 父类
class Animal(object):
    def run(self):
        print('Animal is run...')


# 子类
class Dog(Animal):
    def run(self):
        print('Dog is run...')


class Cat(Animal):
    def run(self):
        print('Cat is run...')


a = Animal()
a.run()

dog = Dog()
dog.run()

cat = Cat()
cat.run()


def run_twice(Animal):
    print(Animal, 'is run...')


run_twice(dog)


class Mouse(object):
    def run(self):
        print('mouse is run...')


mouse = Mouse()
mouse.run()
print(isinstance(mouse,Animal))
