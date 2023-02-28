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
def state_value(grid,d):
 equations=np.zeros(shape=(9,9))
 constants=np.array([0,0,0,0,0,0,0,0,0],dtype=float)
 #print(constants)
 for i in range(0,3):
    for j in range(0,4):
       if( (i==0 and j==3) or (i==1 and j==3) or(i==1 and j==1)):
          continue
       i1=i-1
       i2=i+1
       j1=j-1
       j2=j+1
       if i1<0:

          equations[j][j]+=0.25*d
          #print(equations[j][j])
       else:
          if  not (i1==1 and j==1):
            if i==1:
               if j==0:
                equations[3][0]+=0.25*d
                #constants[3]+=grid[i1][j]

               elif j==2:
                  equations[4][2]+=0.25*d
                  #constants[4]+=grid[i1][j]



            else:
             if j==0:
               equations[5 ][3] += 0.25*d
               #constants[5] += -grid[i1][j]

             elif j==2:
                equations[7][4]+=0.25*d
                #constants[7] += -grid[i1][j]
             else:
                 constants[8]+=0.25
          else:

             equations[6][6]+=0.25*d
       #print("1",equations[5][5])
       if i2>2:

          equations[5+j][5+j]+=0.25*d
          #print("2",equations[5][5])
       else:
          if not (i2 == 1 and j == 1):
             if i == 1:
                if j==0:
                 equations[3][5] += 0.25*d
                 #constants[3] += -grid[i2][j]
                else:
                   equations[4][7]+=0.25*d
             else:
                if j==0:
                 equations[0][3] += 0.25*d
                 #constants[0] += -grid[i2][j]
                else:
                   equations[2][4]+=0.25*d
                   #constants[2]+=-grid[i2][j]
          else:
             equations[1][1]+=0.25*d
          #print(3,equations[5][5])

       if j2>3:
          equations[8][8]+=0.25*d

       else:
         if not(i==1 and j2==1):
             if i==0:
                 if j2==3:
                  constants[2]+=-0.25
                 else:
                     equations[j][j2]+=0.25*d
                     #print(j,j2)
             elif i==1:
               constants[4]+=0.25
             else:
              equations[5+j][5+j2]+=0.25*d
              #constants[5+j]+=grid[i][j2]
         else:
             equations[3][3]+=0.25*d
         #print(4,equations[5][5])

       if j1<0:
          if i==0:
             equations[0][0]+=0.25*d
          elif i==1:
             equations[3][3]+=0.25*d
          else:
             equations[5][5]+=0.25*d
          #print(5,equations[5][5])
       else:
           if not (i == 1 and j1 == 1):
               if i==0:
                   equations[j][j1]+=0.25*d
               else:
                   equations[5+j][5+j1]+=0.25*d
           else:
               equations[4][4]+=0.25*d

# print(equations)
 for i in range(0,9):
     equations[i][i]+=-1
 #print(equations)
 #print(constants)
 solutions=np.linalg.solve(equations,constants)
 statevalues=np.zeros(shape=(3,4))
 #print(solutions)
 statevalues[0][0]=solutions[0]
 statevalues[0][1] = solutions[1]
 statevalues[0][2] = solutions[2]
 statevalues[0][3]=0
 statevalues[1][0]=solutions[3]
 statevalues[1][1]=0
 statevalues[1][2]=solutions[4]
 statevalues[1][3] = 0
 statevalues[2][0]=solutions[5]
 statevalues[2][1]=solutions[6]
 statevalues[2][2]=solutions[7]
 statevalues[2][3]=solutions[8]
 return statevalues


if __name__ == '__main__':

 # See PyCharm help at https://www.jetbrains.com/help/pycharm/
 grid,gridreward=generate_grid()
 state_values=state_value(gridreward,0.9)
 #print(state_values)