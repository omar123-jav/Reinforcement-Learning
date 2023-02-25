# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
def generate_grid():
   row0=["","","","End State Reward=+1"]
   row1= ["", "Wall", "", "End State Reward=-1"]
   row2=["Initial State","","",""]
   grid=[row0,row1,row2]
   gridreward=np.zeros(shape=(3,4),dtype=int)
   gridreward[0][3]=1
   gridreward[1][3]=-1
   return grid,gridreward
def state_value(grid):
 equations=np.zeros(shape=(9,9),dtype=int)
 constants=np.zeros(shape=(1,9),dtype=int)
 for i in range(0,3):
    for j in range(0,4):
       if( (i==0 and j==3) or (i==1 and j==3) or(i==1 and j==1)):
          continue
       i1=i-1
       i2=i+1
       j1=j-1
       j2=j+1
       if i1<0:       #up movement
          equations[j][j]=0.9
       else:
          if  not (i1==1 and j==1):
            if i==1:
               if j==0:
                equations[3][0]+=0.9
                constants[3]+=grid[i1][j]

               elif j==2:
                  equations[4][2]+=0.9
                  constants[4]+=grid[i1][j]



            else:
             if j==0:
               equations[5 + j][3+j] += 0.9
               constants[5 + j] += grid[i1][j]

       if i2>2:
          equations[5+j][5+j]=0.9
       else:
          if not (i1 == 1 and j == 1):
             if i == 1:

                equations[3 + j][j] += 0.9
                constants[3 + j] += grid[i2][j]
             else:
                equations[ j][j] += 0.9
                constants[j] += grid[i2][j]


       if j2>3:
          equations[8][8]+=0.9
       if j1<0:
          if i==0:
             equations[0][0]+=0.9
          if i==1:
             equations[3][3]+=0.9
          else:
             equations[5][5]+=0.9






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
grid,gridreward=generate_grid()
print(gridreward)