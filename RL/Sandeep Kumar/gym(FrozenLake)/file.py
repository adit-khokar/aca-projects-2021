import gym
import numpy as np

env = gym.make('FrozenLake-v0')
gamma=0.9 #Value of discount


class Value_iterating_agent():
    def __init__(self,env,gamma):
        env = gym.make('FrozenLake-v0')
        self.max_iter=1000
        self.gamma=gamma
        self.no_of_states=env.observation_space.n
        self.no_of_actions=env.action_space.n
        self.probs=env.env.P
        self.values=np.zeros(env.observation_space.n)
        self.policy=np.zeros(env.observation_space.n)

    def value_iter(self):
        for i in range(self.max_iter):
            new_values=np.zeros(self.no_of_states)
            for state in range(self.no_of_states):
                q_value=0
                flag=0
                for action in range(self.no_of_actions):
                    next_state_rewards=0
                    for next_state_info in self.probs[state][action]:
                        trans_prob,next_state,reward,_=next_state_info
                        next_state_rewards+=trans_prob*(reward+gamma*self.values[next_state])

                    if flag==0:
                        q_value=next_state_rewards
                        flag=1
                    else:
                        q_value=max(q_value,next_state_rewards)
                    
                new_values[state]=q_value
            self.values=new_values
        return self.values
    def extract_policy(self):
        for state in range(self.no_of_states):
            #q_val=np.zeros(self.no_of_actions)
            flag=0
            q_val=0
            index=0
            for action in range(self.no_of_actions):
                q=0
                for next_state_info in self.probs[state][action]:
                    trans_prob,next_state,reward,_=next_state_info
                    q+=trans_prob*(reward+gamma*self.values[next_state])
                if flag==0:
                    q_val=q
                    flag=1
                    index=action
                    
                else:
                    if q_val < q:
                        q_val=q
                        index=action
            self.policy[state]=index
    def choose_action(self,observation):
        return self.policy[observation]

agent = Value_iterating_agent(env,gamma)
agent.value_iter();
agent.extract_policy();

all_rewards=[]
for i in range(1000):
	obs=env.reset()
	total_reward = 0
	while True:
	    action = agent.choose_action(obs)
	    obs,reward,done,info = env.step(action)
	    if done:
	    	all_rewards.append(reward)
	    	break
print ("Average Reward: ", np.mean(all_rewards))