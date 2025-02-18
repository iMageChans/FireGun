from service.pallets.base_class import PalletQueriesBase, PalletExtrinsicsBase


class BalancesQueries(PalletQueriesBase):
    def __init__(self):
        super().__init__('Balances')

    def get_balance(self, account_id: str):
        """
        gets balance from chain
        Args:
             account_id (str): account address
        Returns:
             float: balance
        """
        return self.chain_interface.query('System', 'Account', [account_id])

    def get_locks(self, account_id: str):
        """
        gets locks from chain
        Args:
             account_id (str): account address
        Returns:
             list: locks
        """
        return self.compose_query('Locks', [account_id])


class BalancesExtrinsics(PalletExtrinsicsBase):
    def __init__(self):
        super().__init__('Balances')

    def transfer(self, recipient: str, amount: int):
        """
        transfer funds from one account to another
        Args:
             recipient (str): recipient account address
             amount (int): amount to transfer in base units
        Returns:
             dict: extrinsic result
        """
        result = self.compose_call('transfer', {
            'dest': recipient,
            'value': amount
        })

        return result