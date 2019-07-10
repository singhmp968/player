x=int(input(""))
li=list(map(int,input().split()))[:x]
max=0
mi=0
for i in range(1,len(li),1):
    k=li.count(i)
    if(k==1):
        mi+=i   
print(mi)
