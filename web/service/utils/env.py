import os
import environ
from pathlib import Path


class EnvConfig:
    def __init__(self, env_file='.env'):
        self.env = environ.Env()
        self.env.read_env(env_file)
        base_dir = Path(__file__).resolve().parent.parent.parent
        self.env.read_env(os.path.join(base_dir, '.env'))

    def get(self, key, default=None):
        return self.env(key, default=default)



config = EnvConfig()

print(config.get('NODE_REWARD_CONTRACT'))