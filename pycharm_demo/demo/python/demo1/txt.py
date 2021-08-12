# print('"hello"')
# input输入，print输出
# name = input()
# print("hello,",name)
# print("1024*768=",1024*768)
# print('I\'m')
# 三个单引号'''...'''可以直接换行输出
# print('''1
# 2
# 3
# /''')
# ord把字符转换为编码；chr把编码转换为字符
# print(ord('a'))
# print(chr(ord('a')))
# encode  指定编码格式
# print('李志鹏'.encode('utf-8'))
# print('a'.encode('ascii'))
#集合 list：可变集合
# aggregate = [1,2,'三',4,5]
# print(aggregate)
# # len 获得集合元素个数
# print("集合元素个数：",len(aggregate))
# # 读取集合第一个元素
# print(aggregate[0])
# # 读取集合最后一个元素
# print(aggregate[-1])
# # 追加元素，到集合末尾
# aggregate.append(6)
# print(aggregate)
# # 追加元素，到集合指定位置
# aggregate.insert(6,7)
# print(aggregate)
# # 删除集合末尾元素
# aggregate.pop()
# print(aggregate)
# # 删除集合指定位置元素
# aggregate.pop(5)
# print(aggregate)
# # 替换集合中某个元素（直接给该元素赋值）
# aggregate[2] = 3
# print(aggregate)

# 元组（有序列表）tuple :不可变集合
nuchange = (1,2,3,4,5)
# 不可变集合，不能再次赋值,否则报错.
# nuchange[0] = '一'
# print(nuchange)
# 定义只有一个元素的不可变集合(后面必须加逗号，否则就是给onlyOne赋值数字1)
# onlyOne = (1,)
# 循环
# for x in [1,2,3,4,5]:
#     print('循环次数：',x)

# range函数生成一个整数序列，配合list函数转换为集合
# aggregate = list(range(10))
# print(aggregate)
# for x in aggregate:
#     print('循环次数：',x)
#
# n = 0
# while n < 10 :
#     print('while循环次数：', n)
#     n = n + 1

# 字典   dic和set
dictionary = {'one':1,'two':2,'three':3}
# print(dictionary)
# dictionary['one'] = 'zhangsan'
# print(dictionary)
# # .get判断key是否存在，in 判断字符是否存在
# print(dictionary.get('a',"key不存在"))
# if 'a' in dictionary:
#     print('key 存在')
# else:
#     print('key 不存在')
# aggregate = [1,2,3,4]
# dictionary['one'] = aggregate
# print(dictionary)
# nuaggregate = (1,2,3,4,5)
# dictionary['two'] = nuaggregate
# print(dictionary)
# a = 4
# dictionary['three'] = a
# print(dictionary)

# .replace 字符替换
# a = 'abc'
# a.replace('a','B')
# print(a)
# a = a.replace('a','B')
# print(a)


a = '1?23'
#删除字符串中的最后一个字符
b = a[:-1]
#字符串转换为数字
c = int(a)
#截取指定位置的字符,截取？号之前的字符串，需导入re三方库
d = re.match(r'.*?\?',a)

