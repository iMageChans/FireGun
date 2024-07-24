from service.utils import numbers


class JSONExtractor:

    def __init__(self):
        self.check = False

    def extract_last_ok(self, data):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == "Ok":
                    self.check = True
                    return self.extract_last_ok(value)
                elif key == "Err":
                    self.check = False
                    return self.extract_last_ok(value)
                else:
                    result = self.extract_last_ok(value)
                    if result is not None and result != value:
                        return result
        elif isinstance(data, (dict, list, tuple, int, str)):
            return data
        return None

    def d9_to_usdt(self, data):
        keys = ['d9', 'usdt']
        value = self.extract_last_ok(data)
        if self.check:
            return dict(zip(keys, value))
        return value

    def usdt_to_d9(self, data):
        keys = ['usdt', 'd9']
        value = self.extract_last_ok(data)
        if self.check:
            return dict(zip(keys, value))
        return value

    def get_data_or_err(self, data):
        value = self.extract_last_ok(data)
        if self.check:
            return value
        return value

    def get_balances_d9(self, data):

        if data is not None:
            self.check = True
        self.check = False

        return data.value_serialized['data']['free']

    def get_transfer_data(self, data):

        if data is not None:
            self.check = True
        self.check = False

        return {
            "block_hash": data.block_hash,
            "extrinsic_hash": data.extrinsic_hash
        }

    def get_burning_portfolio(self, data):

        if isinstance(data, dict):
            self.check = True
        self.check = False

        res = data['result']['Ok']['data']['Ok']
        return {
            "amount_burned": numbers.DecimalTruncator(2).format_d9(res['amount_burned']),
            "balance_due": numbers.DecimalTruncator(2).format_d9(res['balance_due']),
            "balance_paid": numbers.DecimalTruncator(2).format_d9(res['balance_paid']),
            "last_withdrawal": res['last_withdrawal']['time'],
            "last_burn": res['last_burn']['time'],
        }

    def get_merchant_portfolio(self, data):

        if isinstance(data, dict):
            self.check = True
        self.check = False

        res = data['result']['Ok']['data']['Ok']
        return {
            "green_points": numbers.DecimalTruncator(2).format_usdt(res['green_points']),
            "relationship_factors": res['relationship_factors'],
            "last_withdrawal": res['last_withdrawal'],
            "redeemed_usdt": numbers.DecimalTruncator(2).format_usdt(res['redeemed_usdt']),
            "redeemed_d9": numbers.DecimalTruncator(2).format_d9(res['redeemed_d9']),
            "created_at": res['last_burn'],
        }


extractor = JSONExtractor()
