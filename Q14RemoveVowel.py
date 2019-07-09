x=int(input())
n=[i for i in input()]
vowel='aeiouAEIOU'
for i in n:
    
    if i in vowel:
        
        n.remove(i)
print(''.join(n[::-1]))
