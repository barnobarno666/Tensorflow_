import  gymnasium as  gym
import numpy as np
from gymnasium import spaces

import numpy as np
import cv2
import random
import time

from collections import deque

SNAKE_LEN_GOAL=30

def collision_with_apple(apple_position, score):
    apple_position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
    score += 1
    return apple_position, score

def collision_with_boundaries(snake_head):
    if snake_head[0]>=500 or snake_head[0]<0 or snake_head[1]>=500 or snake_head[1]<0 :
        return 1
    else:
        return 0

def collision_with_self(snake_position):
    snake_head = snake_position[0]
    if snake_head in snake_position[1:]:
        return 1
    else:
        return 0


class SnakeEnv(gym.Env):
    metadata={'render.modes':['human'] }
    def __init__(self):
        super(SnakeEnv,self).__init__()
        self.action_space=spaces.Discrete(4)
        self.observation_space=spaces.Box(low=-500,high=500,shape=(5+SNAKE_LEN_GOAL,),dtype=np.int64)
        
        
    def step(self,action):
        self.prev_actions.append(action)
        
        cv2.imshow('a',self.img)
        cv2.waitKey(1)
        img = np.zeros((500,500,3),dtype='uint8')
        # Display Apple
        cv2.rectangle(self.img,(self.apple_position[0],self.apple_position[1]),(self.apple_position[0]+10,self.apple_position[1]+10),(0,0,255),3)
        # Display Snake
        for position in self.snake_position:
            cv2.rectangle(self.img,(position[0],position[1]),(position[0]+10,position[1]+10),(0,255,0),3)
        
        # Takes step after fixed time
        t_end = time.time() + 0.05
        k = -1
        while time.time() < t_end:
            if k == -1:
                k = cv2.waitKey(1)
            else:
                continue
                
        # 0-Left, 1-Right, 3-Up, 2-Down, q-Break
        # a-Left, d-Right, w-Up, s-Down

    
        # Change the head position based on the button direction
        if action == 1:
            self.snake_head[0] += 10
        elif action == 0:
            self.snake_head[0] -= 10
        elif action == 2:
            self.snake_head[1] += 10
        elif action == 3:
            self.snake_head[1] -= 10

        # Increase Snake length on eating apple
        if self.snake_head == self.apple_position:
            self.apple_position, self.score = collision_with_apple(self.apple_position, self.score)
            self.snake_position.insert(0,list(self.snake_head))

        else:
            self.snake_position.insert(0,list(self.snake_head))
            self.snake_position.pop()
        
        # On collision kill the snake and print the score
        if collision_with_boundaries(self.snake_head) == 1 or collision_with_self(self.snake_position) == 1:
            font = cv2.FONT_HERSHEY_SIMPLEX
            self.img = np.zeros((500,500,3),dtype='uint8')
            cv2.putText(self.img,'Your Score is {}'.format(self.score),(140,250), font, 1,(255,255,255),2,cv2.LINE_AA)
            cv2.imshow('a',self.img)
            self.done=True
            
        if collision_with_self(self.snake_position) == 1:
            self.reward=-10000
        elif self.done==True:
            self.reward=-10
        else:
            self.reward=self.score*10
        
                  #d
        head_x=self.snake_head[0]
        head_y=self.snake_head[1]
        
        apple_delta_X=head_x-self.apple_position[0]
        apple_delta_X=head_x-self.apple_position[1]
        snake_length=len(self.snake_position)        
        
        
        
        self.observation=[head_x,head_y,apple_delta_X,apple_delta_X,snake_length]+list(self.prev_actions)
        self.observation=np.array(self.observation)
        self.info={}

        return self.observation,self.reward,self.done,self.done,self.info

        
    def reset(self,seed=None):
        self.done=False
        
        self.img = np.zeros((500,500,3),dtype='uint8')
# Initial Snake and Apple position
        self.snake_position = [[250,250],[240,250],[230,250]]
        self.apple_position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
        self.score = 0
        self.reward=0
        prev_button_direction = 1
        self.button_direction = 1
        self.snake_head = [250,250]
        
        
        #d
        head_x=self.snake_head[0]
        head_y=self.snake_head[1]
        
        apple_delta_X=head_x-self.apple_position[0]
        apple_delta_X=head_x-self.apple_position[1]
        snake_length=len(self.snake_position)        
        
        
        self.prev_actions=deque(maxlen=SNAKE_LEN_GOAL)
        
        for _ in range(SNAKE_LEN_GOAL):
            self.prev_actions.append(-1)
        
        self.observation=[head_x,head_y,apple_delta_X,apple_delta_X,snake_length]+list(self.prev_actions)
        self.observation=np.array(self.observation)
        
        
        
        
        return (self.observation,self.info)
    
    
    def render(self, mode='human', close=False):
    # Get the current state of the environment
        state = self.state
        # Get the size of the grid
        size = self.size
        # Create an empty image array
        img = np.zeros((size, size, 3), dtype=np.uint8)
        # Fill the image array with colors according to the state
        for i in range(size):
            for j in range(size):
                if state[i][j] == 0: # Empty cell
                    img[i][j] = [255, 255, 255] # White
                elif state[i][j] == 1: # Agent
                    img[i][j] = [0, 0, 255] # Blue
                elif state[i][j] == 2: # Goal
                    img[i][j] = [255, 0, 0] # Red
        # Handle different render modes
        if mode == 'human':
            # Display the image on the screen using OpenCV
            cv2.imshow('CustomEnv', img)
            cv2.waitKey(1)
        elif mode == 'rgb_array':
            # Return the image array
            return img
        else:
            # Raise an exception for unsupported modes
            raise NotImplementedError(f'Render mode {mode} is not supported')
        # Close the rendering window if requested
        if close:
            cv2.destroyAllWindows()

        
        
    

    
    
