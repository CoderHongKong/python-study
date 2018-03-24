# -*- coding: UTF-8 -*-
#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:       
# Purpose:
#
# Author:      hekai
#-------------------------------------------------------------------------------
arrs = ['a', 'b', 'c', ['x', 'y'],'d', 'e']
print(arrs)
# 浅拷贝
arrs_copy = arrs.copy()
print(arrs_copy)
arrs_ = arrs[:]
print(arrs_)
l = list(arrs)
print(l)

print(arrs[0:-1:2])
print(arrs[:2])
print('------------')
for i in arrs:
    print(i)
