from substrateinterface import Keypair


class ValidAddress:
    def __init__(self, address):
        self.address = address

    def get_valid_address(self):
        prefix = "Dn"
        if self.address.startswith(prefix):
            # 提取实际地址部分
            actual_address = self.address[len(prefix):]
            try:
                keypair = Keypair(ss58_address=actual_address)
                return actual_address
            except ValueError as e:
                print(f"Invalid address: {e}")
                return None
        else:
            print("Invalid prefix")
            return self.address

    def mate_data_address(self):
        return self.address


def get_valid_address(address_with_prefix):
    prefix = "Dn"
    if address_with_prefix.startswith(prefix):
        # 提取实际地址部分
        actual_address = address_with_prefix[len(prefix):]
        try:
            keypair = Keypair(ss58_address=actual_address)
            return actual_address
        except ValueError as e:
            print(f"Invalid address: {e}")
            return None
    else:
        print("Invalid prefix")
        return address_with_prefix