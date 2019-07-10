x=int(input())
s="kabali"
count=0
for i in range(0,x,1):
    s1=input()
    if(sorted(s)==sorted(s1)):
       count=count+1
print(count)
