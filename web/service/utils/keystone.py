from substrateinterface import Keypair

def check_keypair(data):
    if Keypair.validate_mnemonic(data):
        try:
            return Keypair.create_from_mnemonic(data, ss58_format=9)
        except ValueError:
            raise ValueError("ECDSA mnemonic only supports english")
    elif isinstance(data, list):
        try:
            mnemonic = ' '.join(data)
            return Keypair.create_from_mnemonic(mnemonic, ss58_format=9)
        except ValueError:
            raise ValueError("ECDSA mnemonic only supports english")
    elif isinstance(data, str):
        return Keypair.create_from_private_key(data, ss58_format=9)