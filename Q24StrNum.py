x=str(input())
for i in x:
    if i.isdigit()==False:
        m=False
        print("no")
        break
    else:
        m=True
if(m==True):
    print("yes")
            
