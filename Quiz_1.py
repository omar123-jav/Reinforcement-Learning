import numpy as np
import matplotlib.pyplot as plt 
import time
import gym
import math

class Q_Learning:
     
    def __init__(self,env,alpha,gamma,epsilon,numberEpisodes,bins,lowerBounds,upperBounds):
         
        self.env=env
        self.alpha=alpha
        self.gamma=gamma 
        self.epsilon=epsilon 
        self.action=env.action_space.n 
        self.numberEpisodes=numberEpisodes
        self.bins=bins
        self.lowerBounds=lowerBounds
        self.upperBounds=upperBounds
         
        self.sumRewardsEpisode=[]
         
        self.q_table=np.random.uniform(low=0, high=1, size=(bins[0],bins[1],bins[2],bins[3],self.action))
     

    def State_Index(self,state):

        x = state[0]
        x_dot = state[1]
        theta = state[2]
        theta_dot = state[3]

        # Evenly spaced bins between lowerBounds and upperBounds
        x_Bin = np.linspace(self.lowerBounds[0],self.upperBounds[0],self.bins[0])
        x_dot_bin = np.linspace(self.lowerBounds[1],self.upperBounds[1],self.bins[1])
        theta_bin = np.linspace(self.lowerBounds[2],self.upperBounds[2],self.bins[2])
        theta_dot_bin = np.linspace(self.lowerBounds[3],self.upperBounds[3],self.bins[3])

        # Returns the index of the bins to which each value in input array belongs 
        x_index = np.maximum(np.digitize(state[0],x_Bin)-1,0)
        x_dot_index = np.maximum(np.digitize(state[1],x_dot_bin)-1,0)
        theta_index = np.maximum(np.digitize(state[2],theta_bin)-1,0)
        theta_dot_index = np.maximum(np.digitize(state[3],theta_dot_bin)-1,0)
         
        # A tuple holding the indices of each bin for each state 
        return tuple([x_index,x_dot_index,theta_index,theta_dot_index])   
    
 
    def Action_Move(self,state,index):
         
        r = np.random.random()

        if r < self.epsilon:

            return np.random.choice(self.action)            
        
        else:
        
            return np.random.choice(np.where(self.q_table[self.State_Index(state)]==np.max(self.q_table[self.State_Index(state)]))[0])
      

    def simulation(self):
     
        for episode in range(self.numberEpisodes):
             
            episodicRewards = []
             
            (curr_state,_) = self.env.reset()
            curr_state = list(curr_state)
           
            print("Simulating episode {}".format(episode)) 
             
            terminal_state=False
            
            while not terminal_state:
                 
                curr_state_index = self.State_Index(curr_state)
                 
                action = self.Action_Move(curr_state,episode)
                
                (next_state, reward, terminal_state,_,_) = self.env.step(action)          
                 
                episodicRewards.append(reward)
                 
                next_state = list(next_state)
                 
                next_state_index = self.State_Index(next_state)
                 
                q_Max = np.max(self.q_table[next_state_index])                                               
                                              
                if not terminal_state:

                    error=reward+self.gamma*q_Max-self.q_table[curr_state_index+(action,)]
                    self.q_table[curr_state_index+(action,)]=self.q_table[curr_state_index+(action,)]+self.alpha*error

                else:

                    error=reward-self.q_table[curr_state_index+(action,)]
                    self.q_table[curr_state_index+(action,)]=self.q_table[curr_state_index+(action,)]+self.alpha*error
                                    
                curr_state=next_state
         
            print("Sum of rewards {}".format(np.sum(episodicRewards)))        
            self.sumRewardsEpisode.append(np.sum(episodicRewards))


    def optimal_Policy(self):

        env1 = gym.make('CartPole-v1',render_mode='human')
        (currentState,_) = env1.reset()
        env1.render()
        timeSteps = 1000
        obtainedRewards = []
         
        for timeIndex in range(timeSteps):

            print(timeIndex)
        
            curr_state_Action = np.random.choice(np.where(self.q_table[self.State_Index(currentState)]==np.max(self.q_table[self.State_Index(currentState)]))[0])
            
            currentState, reward, terminated, truncated, info = env1.step(curr_state_Action)
            
            obtainedRewards.append(reward)   
            
            time.sleep(0.05)
            
            if (terminated):
                
                time.sleep(1)
                break

        return obtainedRewards,env1


if __name__ == '__main__':

    env = gym.make('CartPole-v1')
    (state,_) = env.reset()
    
    upperBounds = env.observation_space.high
    lowerBounds = env.observation_space.low
    x_dot_min = -4
    x_dot_max = 4
    theta_dot_min = -3*math.pi
    theta_dot_max = 3*math.pi
    upperBounds[1] = x_dot_max
    upperBounds[3] = theta_dot_max
    lowerBounds[1] = x_dot_min
    lowerBounds[3] = theta_dot_min
    
    x_bin = 50
    x_dot_bin = 50
    theta_bin = 50
    theta_dot_bin = 50
    bins = [x_bin,x_dot_bin,theta_bin,theta_dot_bin]
    
    epsilon = 0.05
    alpha = 0.1
    gamma = 0.9
    numberOfEpisodes = 500
    
    Q1 = Q_Learning(env,alpha,gamma,epsilon,numberOfEpisodes,bins,lowerBounds,upperBounds)

    Q1.simulation()

    (obtainedRewardsOptimal,env1) = Q1.optimal_Policy()
    
    plt.figure(figsize = (12, 5))
    plt.plot(Q1.sumRewardsEpisode,color='blue',linewidth=1)
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.yscale('log')
    plt.show()

    env1.close()

    np.sum(obtainedRewardsOptimal)