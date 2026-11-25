def get_withdrawal_limit(kyc_level):
    limits = {0: 0, 1: 1000, 2: 10000, 3: 100000}
    return limits[kyc_level]