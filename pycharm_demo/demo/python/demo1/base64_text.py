# -*- coding: utf-8 -*-
# !usr/bin/python

import base64
import hashlib
from html.parser import HTMLParser
# from html.entities import name2codepoint

noBase = 'abcdefg'
print('noBase:',noBase)
print('yesbase:',base64.b64encode(b'abcvdef'))


noMd5 = 'abcdef9'
md5 = hashlib.md5()
print(md5)
md5.update(noMd5.encode('utf-8'))
print(md5.hexdigest())


