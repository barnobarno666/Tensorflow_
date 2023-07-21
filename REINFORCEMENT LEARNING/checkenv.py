from stable_baselines3.common.env_checker import check_env
import snakeenv
from snakeenv import SnakeEnv
env=SnakeEnv()


check_env(env)