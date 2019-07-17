a=int(input())
li=list(map(str,input().split()[:a]))
li.sort()
li.sort(key=len)
for i in li:
        print(i,end=" ")
