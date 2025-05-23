import sys
import pygame as pg
import numpy as np
import gymnasium as gym
from gymnasium import spaces
from stable_baselines3 import PPO

WIDTH = 800
HEIGHT = 100
BOX_SIZE = 100

class BoxEnv(gym.Env):
    def __init__(self):
        super(BoxEnv, self).__init__()

        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=0, high=WIDTH, shape=(1,), dtype=np.float32)

        self.max_steps = 150
        self.current_step = 0

        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('BoxAgent')
        self.clock = pg.time.Clock()

        self.box_x = 0
        self.box_y = 0
        self.clock = pg.time.Clock()

    def reset(self, seed=None):
        self.box_x = 0
        self.current_step = 0

        observation = np.array([self.box_x], dtype=np.float32)
        info = {}

        return observation, info

    def step(self, action):
        reward = 0

        if action == 0:
            reward -= 5
        elif action == 1:
            self.box_x -= 10
            reward -= 1
        elif action == 2:
            self.box_x += 10
            reward += 2

        self.box_x = np.clip(self.box_x, 0, WIDTH - BOX_SIZE)

        distance_to_target = abs((WIDTH - BOX_SIZE) - self.box_x)
        reward -= distance_to_target * 0.1

        terminated = distance_to_target < 5
        truncated = False

        if self.current_step > self.max_steps:
            truncated = True
            reward -= 20

        if self.current_step < self.max_steps and terminated:
            reward += 100

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.close()
                sys.exit(0)

        self.screen.fill((255, 255, 255))
        pg.draw.rect(self.screen, (255, 0, 0), (self.box_x, 0, BOX_SIZE, BOX_SIZE))

        pg.display.flip()

        self.clock.tick(120)

        observation = np.array([self.box_x], dtype=np.float32)

        self.current_step += 1

        info = {}

        return observation, reward, terminated, truncated, info

    def close(self):
        pg.quit()
