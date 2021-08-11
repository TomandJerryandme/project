nick = ''

def abc():
    # global nick
    nick = 'abc'

abc()
print(nick)

"""
__name__ : 在 __name__ 变量的帮助下，你可以判断出这时代码是被直接运行，还是被导入到其他程序中去了

eg:
    test_func.py
        def test():
            print(__name__)
        test()
    # 控制台输出：__main__

    import.py
        import test
        test.test()
    # 控制台输出：test_func(文件名)

"""

'''
__repr__()方法的作用
主要用于在命令行中或者debug模式下，直接输入obj后的显示情况

示例：
>>> class Car():
...     def __init__(self, color, size):
...             self.color = color
...             self.size = size
...     def __str__(self):
...             return "Car: color-" + str(self.color) + "\tsize-" + str(self.size)
...     def __repr__(self):
...             return "\n\tCar:\n\t color: " + str(self.color) + "\n\t size:" + str(self.size)
... 
>>> car = Car("blue", 100)
>>> car

        Car:        
         color: blue
         size:100   
>>> print(car)
Car: color-blue size-100

eg:
    class Person():
        def __init__(self,name,age):
            self.name = name
            self.age = age
        def __repr__(self):
            return 'Person类，包含name='+self.name+'和age='+str(self.age)+'两个实例属性'
    person = Person('吕星辰',20)
    
    print(person) # Person类，包含name=吕星辰和age=20两个实例属性

__str__()方法
主要用于print(obj)时的输出形式
'''