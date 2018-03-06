# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 14:39:20 2018

@author: hp
"""

import re
print("Calculator")
print("Type quit to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter Equation: ")
    else:
        equation = input(str(previous))
    #equation = input("Enter Equation: ")
    if equation == "quit":
        print("GoodBye! Meet you soon!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]','',equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        #print("You typed: " , previous)
        

while run:
    performMath()
