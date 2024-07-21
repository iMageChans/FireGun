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


def get_return_percent(total_amount_burned):
    total_amount_burned = format_number(total_amount_burned, 12)
    first_threshold_amount = 200_000_000
    percentage = 0.008

    if total_amount_burned <= first_threshold_amount:
        return percentage

    excess_amount = total_amount_burned - first_threshold_amount
    reductions = excess_amount // 100_000_000 + 1
    divided_percent_by = 2 ** reductions

    return percentage / divided_percent_by

