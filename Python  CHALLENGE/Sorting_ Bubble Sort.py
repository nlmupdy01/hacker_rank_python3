from itertools import product
def countSwaps(a):
    swaps = 0
    for i,j in product(range(len(a)),range(len(a)-1)):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            swaps += 1
    print("Array is sorted in %s swaps." %swaps)
    print("First Element:", a[0])
    print("Last Element:", a[-1])

n = int(input())
a = list(map(int,input().split()))
countSwaps(a)