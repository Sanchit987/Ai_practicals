#This program checks for prime numbers
x = int(input("Enter the number :"))
i = 2
p=True
while(i<int(x/2)):
    if(x%i == 0):
        p = False

print("It's",p,"that x is prime")
