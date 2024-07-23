from service.utils import types
from service.contracts import main_mining
from service.utils.accounts import get_valid_address
from service.requests.base import abs_class
from service.utils.json import extractor


class GetAncestors(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        valid_address = get_valid_address(validated_data['account_id'])
        self.call = main_mining.MainMining(self.keypair)
        self.res = self.call.get_ancestors(valid_address)

    def results(self):
        values = extractor.get_data_or_err(self.res.value_serialized)
        return values

    def is_success(self):
        extractor.get_data_or_err(self.res.value_serialized)
        return extractor.check