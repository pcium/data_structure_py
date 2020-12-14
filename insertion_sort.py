def InsertionSort(n, size):
    k=0
    for i in range(1, size):
        key = n[i]
        for j in range(i-1, -2, -1):
            if(n[j]>key and j>=0):
                n[j+1]=n[j]
            else:
                k=j
                break
        n[k+1]=key
    return n

size = int(input("Size: "))
n = [int(x) for x in input().strip().split()]

n = InsertionSort(n, size)

for i in n:
    print(i, end=' ')
