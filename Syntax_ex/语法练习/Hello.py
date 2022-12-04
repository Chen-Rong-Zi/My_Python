# coding=utf-8
'''这是一个定义类的测试，看看python是怎么实现类的定义'''


class HelloWorld:
    # 类变量的设置
    name2 = 'HelloWorldPrograme'
    func2 = 'I can say:"Hello Wrold!"'
    # 构造方法
    def __init__(self, name3=name2, func3=func2):
        self.name = name3
        self.func = func3


    def say(self):
        for i in range(2):
            print(self.func,end='\n {} \n'.format('*'*50))
            print(self.name)


    def change_the_attr(self, name3=name2, func3=func2):
        self.name = name3
        self.func = func3
        print(self.name, end=' ')
        print(self.func)
        print('The attributes are successfully changed!')
        
    def hi():
        print('HI')
        
        
# Debugging
a = HelloWorld()

a.change_the_attr('Andy','Nothing')

a.name = 'haha'
a.test = 'sod'
a.say()
HelloWorld.hi()
# print(a.name)
# print(a.test)
'''总结：python中面向对象编程的实现是通过创建类来创造对象
的：
    1. 首先应定义类，再定义构造函数 def __init__(self):  ；  
    其中，创造构造函数的目的是：帮助完成有关实例对象的属性和方法的创建。
        因为想要为对象创建属性，不一定要在类的定义中完成。在类创建后，可以直接
    以赋值的形式创建  对象名.属性名 = 赋值语句  但这种方式显然不适用于创建多个属性(你肯定不想
    浪费大量时间把一个变量分别绑定在几个对象上)，所以构造函数的的作用就体现出来了----
    帮助我们一次性创建多个属性而不用重复劳动，并且这种方式同时能为将来的所有对象都绑定
    一个或几个属性。
    
    2. 其次应该
'''
