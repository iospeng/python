# -*- coding: utf-8 -*-
#!/usr/bin/python

from collections import namedtuple

# namedtuple函数，创建一个可以用属性来调用的不可变集合（tuple）
point = namedtuple('point',['x','y','z','a','b','c'])
p = point(1,2,3,4,5,6)
print(p)