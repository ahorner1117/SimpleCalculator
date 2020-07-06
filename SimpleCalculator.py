# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:41:00 2020

@author: Anthony
"""

operands = ('+','-','/','*','%','^','exp','log','abs')

def calc(x, y, choice):
    a = str(x)
    b = str(y)
    if choice == '+':
        #return a+ "+"+ b + "\=" a+b
        return x+y
    elif choice == '-':
        return x-y
    elif choice == '*':
        return x*y
    elif choice == '/':
        return x/y
    elif choice == '^':
        return x**y
    elif choice == 'exp':
        return ''       #Need to fix the following three elif's
        #exit
    elif choice == 'log':
        return ''
    elif choice  == 'abs':
        return ''
        

def main():
    while True:
        try:     
            num1 = float(input("Enter first number: "))
        except ValueError:
            print("exiting the program...")
            break
        print("Enter one of the following operations:\n", operands, ":")
        choice = input()
        if choice == 'x':
            print("exiting the program...")
            break
        while choice not in operands:
            print("Invalid operation, choose from the list:\n ", operands)
            choice = input()
        try:
            num2=float(input("Enter the second number: "))
        except ValueError:
            print("exiting the program...")
            break          
        print(calc(num1,num2, choice))
        
if __name__ == "__main__":
    main()        
