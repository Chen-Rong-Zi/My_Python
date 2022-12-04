# coding=utf-8
class Animal:
    def __init__(self,age=0,clour=None,speed=0):
        self.age   = age
        self.clour = clour
        self.speed = speed
        
    # 类方法
    def greet():
        print('你好')
        return
         
    def run(self):
        print(f'正在以{self.speed}的速度奔跑')
        return self.speed
        
    def hello(self):
        greet()
        
        
