import os
from service.utils.interface import D9Interface
from substrateinterface.contracts import ContractInstance, ContractExecutionReceipt, ContractMetadata
from substrateinterface import Keypair
from enum import Enum
from service.utils.env import config
from typing import Optional


class D9Contract(ContractInstance):

    def __init__(self, contract_address: str, metadata_file: str,  keypair: Keypair):
        self.contract = ContractInstance.create_from_address(
            contract_address=config.get(contract_address),
            metadata_file=os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                'abis',
                metadata_file
            ),
            substrate=D9Interface(url=config.get('TEST_NET_URL'))
        )
        self.keypair = keypair
        self.gas_predit_result = None

    def contract_exec(self, call_name: str, call_params: dict | None = None, value: int = 0):
        return self.exec(self.keypair, call_name, call_params, value)

    def contract_read(self, call_name: str, call_params: dict | None = None, value: int = 0):
        return self.contract.read(self.keypair, call_name, call_params, value)

    def exec(self, keypair: Keypair, method: str, args: dict = None,
             value: int = 0, gas_limit: Optional[dict] = None, storage_deposit_limit: int = None,
             wait_for_inclusion: bool = True, wait_for_finalization: bool = False
             ) -> ContractExecutionReceipt:

        if gas_limit is None:
            self.gas_predit_result = self.contract.read(keypair, method, args, value)
            gas_limit = self.gas_predit_result.gas_required

        input_data = self.contract.metadata.generate_message_data(name=method, args=args)

        call = self.contract.substrate.compose_call(
            call_module='Contracts',
            call_function='call',
            call_params={
                'dest': self.contract.contract_address,
                'value': value,
                'gas_limit': gas_limit,
                'storage_deposit_limit': storage_deposit_limit,
                'data': input_data.to_hex()
            }
        )

        extrinsic = self.contract.substrate.create_signed_extrinsic(call=call, keypair=keypair)

        receipt = self.contract.substrate.submit_extrinsic(
            extrinsic, wait_for_inclusion=wait_for_inclusion, wait_for_finalization=wait_for_finalization
        )

        return ContractExecutionReceipt.create_from_extrinsic_receipt(receipt, self.contract.metadata, self.contract.contract_address)


class Currency(Enum):
    D9 = 'D9'
    USDT = 'USDT'


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

    def encode(self):
        return [self.from_currency.value, self.to_currency.value]

