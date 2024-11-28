#GIST OF THE PROBLEM 

# The Bride who have the quality (all) then the bride will be selected
# If the bride do not have any quality then print not a suitable bride 
# if the two brides have the same no. of qualities then choose the bride who is close to sam 
# If the both the brides have same no. of qualities as well as same distance from sam then print polygami not allowed 


# ALL THE MARRIAGABLE BRIDES ARE MARKED AS 1 AND THEIR QUALITIES ARE DETERMINED BY THEIR (1)NEIGHBOURS 
# SAM'S PLACE HAVE THE DISTANCE AS (1,1)

# TAKING INPUTS

m,n=map(int,input().split())
g=[]
for i in range(m):
    temp=list(map(int,input().split()))
    g.append(temp)

# Calculate qualities
def check(x,y):
    if(x<0 or x>m-1 or y<0 or y>n-1 ):
        return 0
    return g[x][y]

def calc_qualities(x,y):
    if (g[x][y]==0):
        return 0
    return check(x-1,y)+check(x+1,y)+check(x,y-1)+check(x-1,y+1)+check(x-1,y-1)+check(x,y+1)+check(x+1,y+1)+check(x+1,y-1)     
g[0][0]=0
for i in range(m):
    for j in range(n):
        qualities=0
        if(i!=0 or j!=0): #Avoids grooms house
            qualities=calc_qualities(i,j)
            if (qualities!=0):
                bride[i+1,j+1]=qualities # type: ignore
  
 # MAXIMUM QUALITY 
max_qualities=-1
for coordinates in bride: # type: ignore
    cur_qualities=bride[coordinates] # type: ignore
    if(max_qualities<=cur_qualities):
        max_qualities=cur_qualities

print(max_qualities)

# FIND THE MIN DISTANCE 
[4,4,3]
count=0
min_dis=999999999999999999

for coordinates in bride: # type: ignore
    if(max_qualities==bride[coordinates]): # type: ignore
        cur_distance=max(coordinates[0],coordinates[1])
        if(cur_distance==min_dis):
            count+=1   
        elif(cur_distance<min_dis):
            count=1
            min_dis=cur_distance   
            x=coordinates[0]
            y=coordinates[1]

if (count==1):
    print(str(x)+":"+str(y)+":"+str(max_qualities))
else:
    print("Polygamy not allowed")

