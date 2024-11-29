m,n =map(int,input().split())  
ir,ic=map(int,input().split())
g=[]
for i in range (m):
    temp=list(input().split())
    g.append(temp)

time=[[0 for i  in range(m)] for j in range(n)]

def countTime(row,col,cur_time):
    #boundary 
    if(row<0 or row>m-1 or col<0 or col>n-1):
        return 
    #TREE (NOT WATER )
    if(g[row][col]== 'W'):
        return 
    # time
    if(time[row][col] != 0 and cur_time>=time[row][col]):
        return
    
    time[row][col]=cur_time

    countTime(row+1,col,cur_time+1)
    countTime(row-1,col,cur_time+1)
    countTime(row,col+1,cur_time+1)
    countTime(row,col-1,cur_time+1)
    countTime(row+1,col+1,cur_time+1)
    countTime(row+1,col-1,cur_time+1)
    countTime(row-1,col+1,cur_time+1)
    countTime(row-1,col-1,cur_time+1)




countTime(ir-1,ic-1,1)
print (time)
ans=-1
for i in range(m):
    for j in range(n):
        if(ans<time[i][j]):
            ans=time[i][j]

print(ans)

#  OUTPUT
# 3 3   
# 1 3
# W T T
# T W W
# W T T

# [[0, 2, 1], [3, 0, 0], [0, 4, 5]]
# 5