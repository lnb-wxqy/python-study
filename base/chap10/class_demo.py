# 类和实例
# 类的定义
# 表达式： class 类名(object):
#            pass
# 注意：1.类名通常首字母开头
#      2.(object)表示该类是从哪个类继承下来的，通常没有合适的继承类，就是用object类，所有类的父类

# 类定义举例：
class Student(object):
    # pass
    # 类似于java的构造方法
    # __init__方法的第一个参数永远是self,表示创建实例的本身
    # 在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 类的方法
    def print_score(self):
        print('%s: %s' % (self.name, self.score))


# 创建实例
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
# 但self不需要传，Python解释器自己会把实例变量传进去
s = Student('Mary', 99)
s.print_score()  # 方法调用
print(s.name, s.score)
# 可以自由的给一个实例变量绑定属性,比如给实例s绑定一个name
s.name = 'Cherry'
print(s.name)


# 访问限制，类属性私有化
class Person(object):
    # __name表示属性私有，外部无法访问到
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_fun(self):
        print("%s: %s" % (self.__name, self.__age))

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


pon = Person('五行缺雨', 18)
pon.print_fun()
pon.set_age(20)
print(pon.get_name())
print(pon.get_age())
