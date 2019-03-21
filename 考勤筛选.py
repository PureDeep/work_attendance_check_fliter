#!/usr/bin/env python
#coding=utf-8

x = input("请将考勤记录文件复制一份并改名为“考勤记录.txt”，然后输入你想查找的月份（格式：2018-10）或人名：\n")

f = open("考勤记录.txt","r")
b = open("%s.txt"%x,"a")
'''
count = len(f.readlines())
print(count)
'''
for line in f.readlines():
    m = line.find('%s'%x)
    if (m != -1):
        '''print(m)
        print(type(m))'''
        b.write("%s"%line)


"""
while True:
    line = f.readline()
    m = line.find('%s'%x)
    if m == True:
        b.write("%s"%line)
"""

f.close()
b.close()
    
"""
b = open("%s.txt"%x,"a")
lines = f.readline()
print("+" + "-" * 79+ "+")
for line in f.readlines():
    if
"""
