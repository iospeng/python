
import pickle
import json
'''
# 打开文件open
f = open('D://python/IO.txt','r')
# 读文件 read()
print(f.read())
# 关闭文件(文件使用完毕后必须关闭)
if f:
    f.close()

# with open('D://python/IO.txt','r') as f :
#     print(f.read())

#写文件
w = open('D://python/IO.txt','w')
w.write('\n写文件')
if w:
    w.close()
'''
'''
# 序列化
pick = {'age':20,'score':88,'name':'李四'}
p = open('D://python/IO.txt','wb')
# 方法一 dumps
# end = pickle.dumps(pick)
# p.write(end)
# 方法二 dump
pickle.dump(pick,p)
if p:
    p.close()
# print('----',end)

# 反序列化
ps = open('D://python/IO.txt','rb')
OK = pickle.load(ps)
if ps:
    ps.close()
print(OK)
'''

# python格式转换为json格式，dict格式数据可以直接序列化为json格式(相当于序列化)
# num = {'age':20,'pass':123456,'genber':'男'}
py = {'name':'lishi','the':{'age':20,'pass':123456,'genber':'男'}}
jsondata = json.dumps(py)
print('python格式转换为json格式：\n',jsondata)

# json转换为python
pythondata = json.loads(jsondata)
print('json格式转换为python格式：\n',pythondata)

# 类对象不可以直接转换为json数据，需要先转换为dict，然后再转换为json数据
class student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
# 类对象转换为dict函数
def studentTodict(dict):
    return{
        'name':dict.name,
        'age':dict.age,
        'score':dict.score
    }
# dict转换为类对象函数
def dictTostudent(dict):
    return student(dict['name'],dict['age'],dict['score'])

str = student('王五',33,199)
# 类对象转换为json数据
# studentAndjson = json.dumps(str,default=studentTodict)
todict = studentTodict(str)
studentAndjson = json.dumps(todict)
print('类对象转换为dict，再转换为json数据：',studentAndjson)

# json数据转换为类对象
# stu = json.loads(studentAndjson,object_hook=dictTostudent)
d = json.loads(studentAndjson)
stu = dictTostudent(d)
print(stu)