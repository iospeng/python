
# 函数定义
def login (name,passs):
    print(name,passs)
    # 函数 isinstance(x,(数据类型，数据类型))，判断变量x的数据类型
    # if isinstance(name,(str)):
    #     print("name 是字符类型！")
    # elif isinstance(name, (int)):
    #     print('name 是int类型！')
    if not isinstance(name,(str)):
        #函数 reaise 抛出一个error
        raise TypeError(name,'not is str')
    return name,passs

print(login('1231',123456))