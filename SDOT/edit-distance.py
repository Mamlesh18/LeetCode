def edit(s1,s2):
    dp = [[-1 for _ in range(len(s2) + 1)] for _ in range (len(s1) +1)]
    return rec(s1,s2,len(s1),len(s2),dp)

def rec(s,t,x,y,dp):
    if x == 0:
        return y
    if y == 0:
        return x
    if dp[x][y] != -1:
        return dp[x][y]

    if s[x-1] == t[y-1]:
        dp[x][y] = rec(s,t,x-1,y-1,dp)

    else:
        dp[x][y] = min(1+rec(s,t,x,y-1,dp), min(1+rec(s,t,x-1,y-1,dp),1+rec(s,t,x-1,y-1,dp)))
    return dp[x][y]

s1 = input()
s2 = input()
print(edit(s1,s2))