a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter third Number : "))

if(a>=b and a>=c):
    print(a,"is greatest")
elif(b>=a and b>=c):
    print(b,"is greatest")
else:
    print(c,"is greatest")
