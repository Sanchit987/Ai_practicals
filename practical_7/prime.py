def print_prime(num):
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

print_prime(20)
