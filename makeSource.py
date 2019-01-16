# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 13:56:23 2018

@author: ad
"""


num = input('숫자 : ')

star = '*'
count = 1
f = open('./src.txt', 'w')

for i in range(1, int(num)+1):
    strSrc = 'int {}ptr{} = &ptr{};\n'.format(star, count, count-1)
    #print(strSrc)
    f.writelines(strSrc)
    star = star + '*'
    count += 1


src1 = 'printf("%d", '
src2 = 'ptr'+num

for i in range(1, int(num)+1):
    src1 += '*('

src1 += src2

for i in range(1, int(num)+1):
    src1 += ')'

src1 += ');\n'

#print(src1)
f.writelines(src1)

f.close()
