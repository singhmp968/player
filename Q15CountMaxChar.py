imp=str(input())
max1=0
for i in imp:
    co=imp.count(i)
    if(co>max1):
        max1=imp.count(i)
        mix=i
print(mix)
