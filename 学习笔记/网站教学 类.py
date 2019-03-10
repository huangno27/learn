class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'Hello World'
#类的实例化
c = MyClass()

#访问类的属性和方法
print("MyClass 类的属性 i 为：", c.i)
print("MyClass 类的方法 f 输出为：", c.f())
