def course(N,M,pre):
    pass





n = int(input())
M = int(input())
pre = []
for i in range(M):
    x,y = map(int,input().split())
    pre.append([x,y])


print(course(n,M,pre))
