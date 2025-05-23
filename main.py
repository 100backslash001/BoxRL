import sys
import pygame as pg
import numpy as np
import gymnasium as gym
from gymnasium import spaces
from stable_baselines3 import PPO
from box_env import BoxEnv


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'train':
        env = BoxEnv()

        model = PPO(
            'MlpPolicy',
            env,
            device='cpu',
            verbose=1,
            tensorboard_log='./tensorboard_logs/'
        )

        model.learn(total_timesteps=20000)

        model.save('model/box')

        env.close()
    else:
        env = BoxEnv()

        model = PPO.load('model/box', device='cpu')

        obs, _ = env.reset()

        for _ in range(200):
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(action)

            if terminated or truncated:
                obs, _ = env.reset()

        env.close()
