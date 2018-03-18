# -*- coding: UTF-8 -*-
#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:       
# Purpose:
#
# Author:      hekai
#-------------------------------------------------------------------------------
import getpass

_name = 'hekai'
_pwd = 'hekai'

name = input("name:")
pwd = input("pwd:")
print(name, pwd)

if _name == name and _pwd == pwd:
    print("welcome")
else:
    print("user name or pwd is invalid")
