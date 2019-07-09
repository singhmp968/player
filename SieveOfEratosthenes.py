def SieveOfEratosthenes(n1,n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    count=0
    for p in range(n1, n+1):
        
        if prime[p]: 
            count=count+1
    print(count) 
  
n1,n=map(int ,input().split())
SieveOfEratosthenes(n1,n) 
