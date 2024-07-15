from service.pallets.base_class import PalletQueriesBase, PalletExtrinsicsBase


class ReferralsQueries(PalletQueriesBase):
    def __init__(self):
        super().__init__('D9Referral')

    def get_referral(self, account_id: str):
        """
        gets referral from chain
        Args:
             account_id (str): account address
        Returns:
             list: referral
        """
        result = self.compose_query('Referral', [account_id])
        return result.value

    def direct_referrals_count(self, account_id: str):
        """
        gets direct referrals count from chain
        Args:
             account_id (str): account address
        Returns:
             int: direct referrals count
        """
        result = self.compose_query('DirectReferralsCount', [account_id])
        return result.value

    def max_referral_depth(self):
        """
        gets max referral depth from chain
        Returns:
             int: max referral depth
        """
        result = self.compose_query('MaxReferralDepth', [])
        return result.value

    def get_referral_relationships(self, account_id: str):
        """
        gets referral relationships from chain
        Args:
             account_id (str): account address
        Returns:
             list: referral relationships
        """
        result = self.compose_query('ReferralRelationships', [account_id])
        return result.value


class ReferralsExtrinsics(PalletExtrinsicsBase):
    def __init__(self):
        super().__init__('D9Referral')