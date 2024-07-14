def agreement(n,k):
    if k == 0 or k == n:
        return 1
    else:
        return (agreement(n-1,k)+agreement(n-1,k-1))

n, k = map(int,input().split())
print(agreement(n,k))