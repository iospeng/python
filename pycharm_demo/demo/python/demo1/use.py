
from  enum import Enum,unique
# import function



'''
# x,y = function.login('zhangsan',13)
def fun (a,b,y):
    x,y = y(a,b)
    print('姓名：',x,'年龄:',y)

# 函数名作为函数参数
fun('zhangsan',12345,function.login)

class student(object):
    # _slots_限制动态添加函数时函数的参数
    #  __slots__ = ('pass')
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    num = 3

    def get_name(self):
        return sele.__name
    def get_age(self):
        return self.__age
    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        if not isinstance(age,int):
            print('error:age必须是整数！')
            raise ValueError('age必须是整数！')
        elif age < 0 or age > 100:
            print('error:age必须大于0且小于等于100！')
            raise ValueError('age必须大于0且小于等于100！')
        self.__age = age

    def print_score(self):
        print('%s,%s'%(self.__name,self.__age))



# 类对象的初始化(创建实例)，类方法、属性的调用
a = student('zhangsan',213)
b = student('lizhi',432)
a.print_score()
b.print_score()
a._student__name = 'asdf'
a.print_score()
# print('a对象调用属性name:',a._student__name,'b对象调用属性name：',b._student__name)

#
# a.set_age(0.01)

#获得类的所有属性and方法
print('student类的所有属性和方法：\n',dir(student))

# 动态给class添加属性函数
a.name = 'ssss'
a.print_score()
print(a.name)

def dynamis(test):
    print('这是student类的一个动态函:test = ',test)
student.dynamis = dynamis('hahha')
a.dynamis
'''

'''
# 定义枚举类(枚举值不可以改变)
class enums(Enum):
#     @unique 防止有重复值出现
    one = 1
    two = 2
# 枚举类如果要得到类属性变量的值，需要加.value
print('枚举类：',enums.one.value)

for a in enums:
    print('a:',a.value)

# try...except...finally...错误处理机制(finally一定会执行，可有可无)
try:
    print('try...')
    r = 10 / 0
    print('try:',r)
except BaseException as e:
    # print('error:',e)
    print('error:...')
    raise
finally:
    print('finally...该语句一定会执行，可有可无')
'''

'''
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        # print('Error:', e)
        print('error:...')
        raise
    finally:
        print('finally...')

main()
'''

a = 1
if a < 0 :
    print('a < 0')
if a >= 0 or a <= 0 :
    print('a == 0')
if a > 0:
    print('a > 0')



