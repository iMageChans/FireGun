def format_number(value, precision=12):
    result = value / 10 ** precision

    # 如果结果是一个整数，返回整数类型
    if result.is_integer():
        return int(result)
    else:
        return result


def to_number(value, precision=12):
    result = value * 10 ** precision

    # 如果结果是一个整数，返回整数类型
    if result.is_integer():
        return int(result)
    else:
        return result