import numpy as np

def generate_grid():

   row0=["","","","End State Reward=+1"]
   row1= ["", "Wall", "", "End State Reward=-1"]
   row2=["Initial State","","",""]

   grid=[row0,row1,row2]

   gridreward=np.zeros(shape=(3,4),dtype=int)
   gridreward[0][3]=1
   gridreward[1][3]=-1

   print(grid)

   return grid,gridreward

def value_functions(grid,d):
 
 equations=np.zeros(shape=(9,9))
 constants=np.array([0,0,0,0,0,0,0,0,0],dtype=float)
 #print(constants)

 for i in range(0,3):
    for j in range(0,4):
       if( (i==0 and j==3) or (i==1 and j==3) or(i==1 and j==1)):
          continue
       
       i1=i-1 # Up
       i2=i+1 # Down
       j1=j-1 # Left
       j2=j+1 # Right

       if i1<0: # Upper Edge
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
               equations[5][3] += 0.25*d
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

 for i in range(0,9):
     equations[i][i]+=-1

 # State-Value Calculation
 #-------------------------------------------------# 

 solutions=np.linalg.solve(equations,constants)
 statevalues=np.zeros(shape=(3,4))
 
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

 print("These are the State-Values")
 print("-------------------------")
 print(statevalues)
 print("-------------------------")

 #-------------------------------------------------#

 #Action-Value Calculation
 #-------------------------------------------------#

 rewards = {(0,3):1, (1,3):-1}
 actions = {
            (0,0): ('D','R'),
            (0,1): ('L','R'),
            (0,2): ('L','D','R'),
            (0,3): (),
            (1,0): ('U','D'),
            (1,1): (),
            (1,2): ('U','D','R'),
            (1,3): (),
            (2,0): ('U','R'),
            (2,1): ('L','R'),
            (2,2): ('L','R','U'),
            (2,3): ('L','U'),
        }
                          
 actionvalues = []                                        # 2D Array responsible of carrying the Action-Values of each State (Q-Table)

 for keys in actions:
   #print(keys)
   i = 0
   l = []                                                 # Arrays to be appended to m (Action-Values for each State)
   selff = list(keys)

   if('U' in actions[keys]):

      temp1 = list(keys)
      temp1[0] = temp1[0]-1
      #print(temp1)

      if(tuple(temp1) in rewards):
         l.append(rewards[tuple(temp1)] + d*statevalues[temp1[0]][temp1[1]])
      else:
         l.append(0 + d*statevalues[temp1[0]][temp1[1]])

   elif('U' not in actions[keys]):
      l.append(0 + d*statevalues[selff[0]][selff[1]])

   #print(l)

   if('D' in actions[keys]):
      
      temp2 = list(keys)
      temp2[0] = temp2[0]+1
      #print(temp2)

      if(tuple(temp2) in rewards):
         l.append(rewards[tuple(temp2)] + d*statevalues[temp2[0]][temp2[1]])
      else:
         l.append(0 + d*statevalues[temp2[0]][temp2[1]])

   elif('D' not in actions[keys]):
      l.append(0 + d*statevalues[selff[0]][selff[1]])

   #print(l)

   if('R' in actions[keys]):
      
      temp3 = list(keys)
      temp3[1] = temp3[1]+1
      #print(temp3)

      if(tuple(temp3) in rewards):
         l.append(rewards[tuple(temp3)] + d*statevalues[temp3[0]][temp3[1]])
      else:
         l.append(0 + d*statevalues[temp3[0]][temp3[1]])

   elif('R' not in actions[keys]):
      l.append(0 + d*statevalues[selff[0]][selff[1]])

   #print(l)

   if('L' in actions[keys]):
      
      temp4 = list(keys)
      temp4[1] = temp4[1]-1
      #print(temp4)

      if(tuple(temp4) in rewards):
         l.append(rewards[tuple(temp4)] + d*statevalues[temp4[0]][temp4[1]])
      else:
         l.append(0 + d*statevalues[temp4[0]][temp4[1]])

   elif('L' not in actions[keys]):
      l.append(0 + d*statevalues[selff[0]][selff[1]])

   #print(l)

   actionvalues.append(l)
   
 print("  ")
 print("These are the Action-Values")
 print("-------------------------")
 print(actionvalues)                             # 1) It is a 2D array. For elements inside an individual array, the actions of U,D,R,L are calculated respectively
 print("-------------------------")              #    which means that the first element inside an array represent the action value of Up, the second element represent
                                                 #    the action value of Down, the third element represent the action value of Right, and the fourth value represent the
                                                 #    action value of Left. 
                                                 # 2) The number of arrays are 12, each of which represents the states in the Gridworld in ascending order.
                                                 #    Zeroes represent the Terminal States and inaccessible States (Walls)

 #-------------------------------------------------#

 return statevalues, actionvalues

if __name__ == '__main__':

 grid,gridreward=generate_grid()
 Values=value_functions(gridreward,0.9)

