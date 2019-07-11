a,b=map(int,input().split())

input()

li=list(map(int,input().split()))[:a]
addli=list(map(int,input().split()))[:b]
result=[]
for i in addli:
    li.append(i)
    print(max(li),end= " ");
    
