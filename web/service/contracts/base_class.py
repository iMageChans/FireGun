import os
from pathlib import Path
from service.utils.interface import D9Interface
from substrateinterface.contracts import ContractInstance
from substrateinterface import Keypair
from enum import Enum
from service.utils.env import EnvConfig


config = EnvConfig()


class D9Contract(ContractInstance):

    def __init__(self, contract_address: str, metadata_file: str,  keypair: Keypair):
        self.contract = ContractInstance.create_from_address(
            contract_address=config.get(contract_address),
            metadata_file=os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'abis',
                metadata_file
            ),
            substrate=D9Interface(url=config.get('MAIN_NET_URL'))
        )
        self.keypair = keypair

    def contract_exec(self, call_name: str, call_params: dict | None = None, value: int = 0):
        return self.contract.exec(self.keypair, call_name, call_params, value)

    def contract_read(self, call_name: str, call_params: dict | None = None, value: int = 0):
        return self.contract.read(self.keypair, call_name, call_params, value)


class Currency(Enum):
    D9 = 0
    USDT = 1


class Direction:
    def __init__(self, from_currency: Currency, to_currency: Currency):
        self.from_currency = from_currency
        self.to_currency = to_currency

    def __eq__(self, other):
        if isinstance(other, Direction):
            return (self.from_currency == other.from_currency and
                    self.to_currency == other.to_currency)
        return False

    def __repr__(self):
        return f"Direction(from_currency={self.from_currency}, to_currency={self.to_currency})"

    def __copy__(self):
        return Direction(self.from_currency, self.to_currency)

    def __deepcopy__(self, memodict={}):
        return Direction(self.from_currency, self.to_currency)