# -*- coding: UTF-8 -*-
#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:       
# Purpose:
#
# Author:      hekai
#-------------------------------------------------------------------------------
arrs = ['a', 'b', 'c', 'd', 'e']

print(arrs)

print(arrs[0])
print(arrs[1:4])
print(arrs[-1])
print(arrs[-2])
print(arrs[-2:-1])
print(arrs[-2:])
print(arrs[:4])
arrs.append('f')
print(arrs)
arrs.insert(1, 'gg')
print(arrs)
arrs[2] = 'B'
print(arrs)
arrs.remove('a')
print(arrs)
arrs.pop()
print(arrs)
arrs.pop(3)
print(arrs)
print(arrs.index('gg'))
print(arrs.count('B'))
print(arrs.clear())
