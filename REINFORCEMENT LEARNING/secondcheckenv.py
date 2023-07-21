from snakeenv import SnakeEnv

env=SnakeEnv()
episodes=100

for episode in range(episodes):
    done=False
    obs=env.reset()
    while True:
        action=env.action_space.sample()
       # print("action",action)
        next_state,reward,done,done2,info=env.step(action)
        print('reward: ' ,reward,done,done2,info)
        if done:
            break