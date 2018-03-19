# -*- coding: UTF-8 -*-
#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:       
# Purpose:
#
# Author:      hekai
#-------------------------------------------------------------------------------

name = input("name:")
pwd = input("pwd:")
age = int(input("age:"))
print(type(age))
print(name, pwd)

info = '''
age:%d
''' %(age)
print(info)


info = '''
age:{age}
'''.format(age = age)
print(info)

info = '''
age:{0}
'''.format(age)
print(info)
