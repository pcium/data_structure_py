def SWAP(i, least, n1):
    temp = n1[i]
    n1[i] = n1[least]
    n1[least] = temp
    return n1

size = int(input("Size: "))
n1=[]
n = list(map(int, input().strip().split())) # 반복하면서 요소 반환
n1 = n[:]
#   n = [int(x) for x in input().strip().split()]

for i in range(size):
    least = i
    for j in range(i+1,size):
        if(n1[j] < n1[least]):
            least = j

    if (i != least):
        n1 = SWAP(i, least, n1)

for i in n1:
    print(i, end=' ')
        
