from substrateinterface import Keypair


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