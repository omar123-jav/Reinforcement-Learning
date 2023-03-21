import random

import gym
import numpy as np
def state_idx(position,angle):
     if position>=-4.8 and position<-2.4:
         if angle>=-4.2 and  angle<-2.115:
             return 0
         elif angle>=-2.115 and angle<-0.01:
             return 1
         elif angle>=-0.01 and angle< 0.2095:
             return 2
         else:
             return 3
     elif position>=-2.4 and position<0:
         if angle>=-4.2 and  angle<-2.115:
             return 4
         elif angle>=-2.115 and angle<-0.01:
             return 5
         elif angle>=-0.01 and angle< 0.2095:
             return 6
         else:
             return 7
     elif position>=0 and position<2.4:
         if angle>=-4.2 and  angle<-2.115:
             return 8
         elif angle>=-2.115 and angle<-0.01:
             return 9
         elif angle>=-0.01 and angle< 0.2095:
             return 10
         else:
             return 11
     else:
         if angle >= -4.2 and angle < -2.115:
             return 12
         elif angle >= -2.115 and angle < -0.01:
             return 13
         elif angle >= -0.01 and angle < 0.2095:
             return 14
         else:
             return 15




env=gym.make('CartPole-v1')
qtable=np.zeros(shape=(16,2))
episode=1
epsilone=0.05
#print(qtable)
for _ in range(50):
    state,info = env.reset()
    run=0
    totalreward=0
    while(True):
      action=-1

      st_idx = state_idx(state[0], state[2])
     # print(state[0],state[2],st_idx)
      if np.random.rand()<epsilone:
         action=random.randrange(0,2,1)
      else:
        action=np.argmax(qtable[st_idx])
      #print(action)

      state_next, reward, terminated, truncated, info = env.step(action)
      totalreward+=reward
      state_next_idx=state_idx(state_next[0],state_next[2])
      run += 1
      if  truncated:
          qtable[st_idx][action] = qtable[st_idx][action] + 0.01 * (reward- qtable[st_idx][action])
          print('Episode',episode,':')
          print()
          print('Qtable:')
          print()
          print('left','right')
          print(qtable)
          print()
          print('Runs',run)
          print('Reward:',totalreward)
          print('.........')
          break



      qtable[st_idx][action]=qtable[st_idx][action]+0.01*(reward+np.max(qtable[state_next_idx])-qtable[st_idx][action])
      state=state_next
      #print(state_next,reward)

    episode+=1

env.close()


