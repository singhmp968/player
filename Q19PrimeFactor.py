n1=int(input())

i1=1
while(i1<=n1):
    k1=0
    if(n1%i1==0):
        j1=1
        while(j1<=i1):
            if(i1%j1==0):
                k1=k1+1
            j1=j1+1
        if(k1==2):
            print(i1,end=" ")
    i1=i1+1
