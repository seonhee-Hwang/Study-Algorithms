n,m=map(int,input().split())
bulbs=list(map(int, input().split()))
for i in range(m):
    a,b,c=map(int, input().split())
    if a==1: bulbs[b-1]=c
    elif a==2 :
        for j in range(b-1,c):
            if bulbs[j]==1:bulbs[j]=0
            else : bulbs[j]=1
    elif a==3:
        for j in range(b-1, c):
            bulbs[j]=0
    elif a==4:
        for j in range(b-1, c):
            bulbs[j]=1
print(*bulbs)