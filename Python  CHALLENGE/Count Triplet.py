from collections import Counter

def countTriplets(arr, r):
    a = Counter(arr)
    b = Counter()
    s = 0
    for i in arr:
        j = i//r
        k = i*r
        a[i]-=1
        if b[j] and a[k] and i%r == 0:
            s+=b[j]*a[k]
        b[i]+=1
    return s

n,r = map(int,input().split())
arr = list(map(int,input().split()))
print(countTriplets(arr, r))