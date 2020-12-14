def BubbleSort(n, size):
    for i in range(size-1, 0, -1):
        for j in range(0,i):
            if (n[j] > n[j+1]):
                temp = n[j]
                n[j] = n[j+1]
                n[j+1] = temp
    return n

size = int(input("Size: "))
n = [int(x) for x in input().strip().split()]

n = BubbleSort(n, size)

for i in n:
    print(i, end=' ')
