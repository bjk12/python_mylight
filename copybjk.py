# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 13:27:20 2020

@author: BJK

"""
import logging
#打印日志
logging.basicConfig(level=logging.INFO)
from shutil import copyfile
import os
def copy233(source,destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
#    for path in os.listdir(os.path.split(destination)[0]):
#        print(path)
    for root, dirs, files in os.walk(source):
        #root目录下面如果什么都没有就直接跳出以下两个循环
        destination1=root.replace(source,destination)
        for path1 in dirs:
            dir_of_root=os.path.join(destination1, path1)
            if not os.path.exists(dir_of_root):
                os.mkdir(dir_of_root)
                logging.info(dir_of_root)
        for file in files:
#            if not os.path.exists(destination1):
#                os.mkdir(destination1)
            copyfile(os.path.join(root, file),os.path.join(destination1, file))
if __name__=='__main__':
    source=input('请输入源文件路径：')
#    source=r'C:\Users\BJK\Desktop\current'
    destination=input('请输入目的文件路径：')
    copy233(source,destination)
#    with open(r'C:\Users\BJK\Desktop\aa.txt', 'wb') as f:
#        pass