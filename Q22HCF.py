def Hcf(x,y):
    small=0
    if(x>y):
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if((x%i==0)and(y%i==0)):
            hcf=i
    print(hcf)
    


x,y=map(int,input().split())
Hcf(x,y)
