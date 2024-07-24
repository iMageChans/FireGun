import os
import environ
from pathlib import Path
from substrateinterface import Keypair


class EnvConfig:
    def __init__(self, env_file='.env'):
        self.env = environ.Env()
        self.env.read_env(env_file)
        base_dir = Path(__file__).resolve().parent.parent.parent
        self.env.read_env(os.path.join(base_dir, '.env'))

    def get(self, key, default=None):
        return self.env(key, default=default)

    def get_private_key(self):
        private_key = self.get('WEB_PRIVATE_KEY')
        if private_key:
            return private_key
        else:
            mnemonic = Keypair.generate_mnemonic()
            keypair = Keypair.create_from_mnemonic(mnemonic, ss58_format=9)
            private_key = keypair.public_key
            return private_key



config = EnvConfig()