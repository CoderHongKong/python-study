# -*- coding: UTF-8 -*-
#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:       
# Purpose:
#
# Author:      hekai
#-------------------------------------------------------------------------------
import sys
import os


print(sys.path)

cmd_res = os.popen("dir").read()
print("-->", cmd_res)
os.mkdir("new_dir")

