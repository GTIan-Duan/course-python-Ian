# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:53:05 2022

@author: Dilig
"""

for a in 'abc':
    print(a,end=" ")
print("int str")

for a in {0,1,2}:
    print(a,end=" ")
print("int set")

for a in{"a":0,"b":1,"c":2}:
    print(a,end=" ")
print("int dict")

print("老虎","大象","兔子的群",sep="  是動物和 ",end="都是兔子的朋友?\n")

a=input("數字A\n")
print("您輸入了{a}\n")
b=input("數字B\n")
print("您輸入了{b}\n")

