case = open('input.txt','r').read().split('\n')
n ,case=case[0],case[1:]
case = list(map(int,case))
n = int(n)

health = 2000
injuries = 1000000 
use = [0] * n
hlt = 2000
inj = 1
count = 0
i=0
noc=0
count = 0
while i<n:
    init = i
    j=i
    c=1
    hlt = health - case[i]
    inj *= case[i]
    
    while j < n:
        
        if hlt  < 0 or inj < injuries:
              if case[j] <  case[init] :
                  init+=1
                  hlt -= case[init]
                  inj /= case[init]
              else:
                  break
        hlt -= case[j] 
        inj *= case[j]
        j+=1
        c += 1 
    if c == 444:
        noc += 1
    count=max(count,c)
    i = j 
    print(i)
print(count,noc)