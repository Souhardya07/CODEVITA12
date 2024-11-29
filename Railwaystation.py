# N is the no. of trains 
# n,2 is a 2D Array having rows as no. of trains and 2 as of the arrival time and the stopage time
#  we have to find that the minimum stations required to keep the trains 


n = int(input())
arrival=[]
departure=[]
for i in range(n):
    a,b=map(int,input().split())
    arrival.append(a)
    departure.append(a+b)

arrival.sort()
departure.sort()
cur_platform,ans=1,1
i,j=1,0
while(i<n and j<n):
    if(arrival[i]<=departure[j]):
        cur_platform+=1
        i+=1
    else:
        cur_platform-=1
        j+=1
    ans=max(ans,cur_platform)
print(ans)

#   ata/Local/Programs/Python/Python311/python.exe c:/Users/hp/OneDrive/Documents/GitHub/CODEVITA12/Railwaystation.py
# INPUT 
# 3
# 10 2
# 5 10
# 13 5
# OUTPUT 
# 2     