a,b=map(str,input().split())
"""cha,che=input().split()
if cha[:len(cha)-1]==che[:len(che)-1]:
  print("yes")
else:
  print("no")"""
y=len(a)
count=0
for i in range(y):
    if(a[i]!=b[i]):
        
       count=count+1
if(count==1):
       print("yes")
else:
       print("no")
