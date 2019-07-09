import math
a=int(input())
#arr=list(map(int,input().split())
temp=a
sq1=0
while temp!=0:
    rem = temp%10
    sq1+=pow(rem,2)
    temp=temp//10
print(sq1)
