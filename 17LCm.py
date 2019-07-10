def gcd(x, y): 
     while(y): 
       x, y = y, x % y 
     return x 
def lcm(x,y):
    lcm=(x*y)//gcd(x,y)
    return lcm
x,y=map(int,input().split())
print(lcm(x,y))
