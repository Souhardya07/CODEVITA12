#HERE N IS THE NO. OF ELEMENTS AND THE K IS THE NO. OF OPERATIONS 

# LETS SAY N = 4 AND K = 3

# ARRAY = [20,7,5,4]
# (K==1) OPERATION 1 => REMOVE(20) AND PUT(20/2) 
# (K==2) OPERATION 2 => REMOVE(10) AND PUT(10/2)
# (K==3) OPERATION 3 => REMOVE(7) AND PUT (7/2) 



n,k= (map(int,input().split()))
array=list(map(int,input().split()))
while(k):
    maximum=max(array)
    array.remove(maximum)
    array.append(maximum//2)
    k=k-1
print(sum(array))

#Using heapq

import heapq
test = int(input())
while(test):
    n,k= (map(int,input().split()))
    array=list(map(int,input().split()))
    l1 = [-i for i in array]
    heapq.heapify(l1)
    while(k):
        top = heapq.heappop(l1)
        heapq.heappush(l1,-(-top//2))
        k=k-1
    test=test-1
print(abs(sum(l1))) 

