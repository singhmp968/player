x=str(input())
x1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
newString=""
for i in x:
    if(i in x1):
        
        index1=x1.index(i)
        index1=index1+3
        newString=newString + x1[index1]
print(newString)
    
