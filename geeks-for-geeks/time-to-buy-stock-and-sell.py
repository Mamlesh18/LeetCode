def buy_stock(n):

    a = (n.index(min(n)))
    if a == (len(n) - 1):
        return 0
    if len(n) == 0:
        return None
    maxi = max(n[a+1:])
    b = maxi - a
    return b
n = list(map(int,input().split()))
print(buy_stock(n))