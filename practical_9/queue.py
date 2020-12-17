class myqueue:
    def __init__(self):
        self.arr = []

    def mypush(self,element):
        (self.arr).append(element)

    def mydel(self):
        (self.arr).pop(0)

    def myprint(self):
        for i in range(len(self.arr)):
            print(self.arr[i],end = " ")
        print(" ")

q = myqueue()
while(True):
    print("1. Enter The Element")
    print("2. Delete The Element")
    print("3. See the queue")
    print("4. Exit")
    print("Enter the required action.")
    opt = int(input())
    if(opt == 1):
        ele = int(input())
        q.mypush(ele)
        print("done")
    elif(opt == 2):
        q.mydel()
        print("done")
    elif(opt == 3):
        q.myprint()
    elif(opt == 4):
        break
    else:
        print("------------------")
        continue

print("Thanks For using.")
