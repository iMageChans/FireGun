from django.core.exceptions import ObjectDoesNotExist

from service.utils import keystone
from service.contracts import usdt, main_mining
from service.utils.env import config
from service.utils import accounts
from service.utils.json import extractor
from users_profile.models import UserBurningProfile


class Fire:
    def __init__(self, validated_data):
        self.allowances_extrinsice = None
        self.keypair = keystone.check_keypair(validated_data['keypair'])
        if "account_id" in validated_data:
            self.account_id = accounts.ValidAddress(validated_data['account_id'])
        else:
            address = "Dn" + self.keypair.ss58_address
            self.account_id = accounts.ValidAddress(address)

    def results(self):
        pass

    def is_success(self):
        pass

    def update_or_create_burning_profile(self):
        try:
            self.user_burning_profile = UserBurningProfile.objects.get(pk=self.account_id.mate_data_address())
        except ObjectDoesNotExist:
            call = main_mining.MainMining(self.keypair)
            res = call.get_portfolio(self.account_id.get_valid_address())
            data = extractor.get_burning_portfolio(res.value_serialized)
            data.update({"account_id": self.account_id.mate_data_address()})

            self.user_burning_profile, created = UserBurningProfile.objects.update_or_create(
                account_id=data['account_id'],
                defaults=data
            )
            print({"account_id": self.user_burning_profile.account_id, "created": created})

    def update_or_create_burning_profile_read(self):
        try:
            self.user_burning_profile = UserBurningProfile.objects.get(pk=self.account_id.mate_data_address())
        except ObjectDoesNotExist:
            call = main_mining.MainMining(self.keypair)
            res = call.get_portfolio(self.account_id.get_valid_address())
            data = extractor.get_burning_portfolio_read(res.value_serialized)
            data.update({"account_id": self.account_id.mate_data_address()})

            self.user_burning_profile, created = UserBurningProfile.objects.update_or_create(
                account_id=data['account_id'],
                defaults=data
            )
            print({"account_id": self.user_burning_profile.account_id, "created": created})

    def add_allowances(self, contract: str, amount: int):
        allowances_extrinsic = usdt.USDT(self.keypair)
        receipt = allowances_extrinsic.increase_allowance(contract, amount)
        return receipt

    def remove_allowances(self, contract: str, amount: int):
        allowances_extrinsic = usdt.USDT(self.keypair)
        receipt = allowances_extrinsic.decrease_allowance(contract, amount)
        return receipt
