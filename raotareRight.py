a,k=map(int,input().split())
#arr=list(map(int,input().split())
arr=[int(x) for x in input().split()]
result=[0]*len(arr)
for i in range(len(arr)):
        
        if i+k < len(arr):
            result[i+k]=arr[i]
        else:
            index=(i+k)%len(arr)
            result[index]=arr[i]
for i in range(len(arr)):
    print(result[i],end=' ')
