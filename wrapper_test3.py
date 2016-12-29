#coding:utf-8
#用于转换为粗体
def makebold(fn):
    # 结果返回该函数
    def wrapper():
        # 插入一些执行前后的代码
        return "<b>" + fn() + "</b>"
    return wrapper
 
# 装饰器makeitalic用于转换为斜体
def makeitalic(fn):
    # 结果返回该函数
    def wrapper():
        # 插入一些执行前后的代码
        return "<i>" + fn() + "</i>"
    return wrapper
@makebold
@makeitalic
def say():
	return "Hello"
print (say())
