# -*- coding: UTF-8 -*-
#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:       
# Purpose:
#
# Author:      hekai
#-------------------------------------------------------------------------------

num = 100
count = 0
while count <= 3:

    gussNum = int(input("gussNum:"))

    if gussNum > num:
        print("think smaller")
    elif gussNum < num:
        print("think bigger")
    else:
        print("yes, you got it")
        break
    count += 1
else:
    print("you try to many times, shit...")


for count in range(3):

    gussNum = int(input("gussNum:"))

    if gussNum > num:
        print("think smaller")
    elif gussNum < num:
        print("think bigger")
    else:
        print("yes, you got it")
        break
else:
    print("you try to many times, shit...")



