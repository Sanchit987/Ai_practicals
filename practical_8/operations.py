"""
Practical 8 : Write a program to create simple calculator with following options
- add
- subtract
- multiply
- division
- check number is even odd
- number is prime or not
- print prime in range
- exit
"""
import sys

def add():
    print("Enter first Number : ")
    a = int(input())
    print("Enter Second Number : ")
    b = int(input())

    print("Sum : ",a+b)

def sub():
    print("Enter first Number : ")
    a = int(input())
    print("Enter Second Number : ")
    b = int(input())

    print("Subtraction : ",a-b)

def mul():
    print("Enter first Number : ")
    a = int(input())
    print("Enter Second Number : ")
    b = int(input())

    print("Multiplication : ",a*b)

def div():
    print("Enter numerator : ")
    a = int(input())
    print("Enter denomirator but not zero : ")
    b = int(input())

    if(b !=0 ):
        print("Division : ",a/b)
    else:
        print("invalid")


def eveorodd():
    print("Enter a Number : ")
    x = int(input())
    if(x%2 ==0):
        print("Even")
    else:
        print("odd")

def pon():
    x = int(input("Enter the number :"))
    i = 2
    p=True
    while(i<int(x/2)):
        if(x%i == 0):
            p = False
    print("It's",p,"that x is prime")

def print_prime():
    print("Enter the number upto which you want prime numbers : ")
    num = int(input())
    arr = [i for i in range(2,num)]
    for i in arr:
        if(i != -1):
            for j in arr:
                if(j%i == 0 and j != i):
                    arr[arr.index(j)] = -1
        else:
            continue

    for i in arr:
        if(i != -1):
            print(i)

def oper():
    print("Enter the operation to be performed : ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Check Number even or odd")
    print("6. Number Prime or Not")
    print("7. Print Prime Numbers In range.")
    print("8. Exit")


oper()
x = True
while(x):
    print("Enter Choice : ")
    choice = int(input())
    if(choice == 1):
        add()
    elif(choice == 2):
        sub()
    elif(choice == 3):
        mul()
    elif(choice == 4):
        div()
    elif(choice == 5):
        eveorodd()
    elif(choice == 6):
        pon()
    elif(choice == 7):
        print_prime()
    elif(choice == 8):
        sys.exit()
    oper()
