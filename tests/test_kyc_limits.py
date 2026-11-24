import pytest


def get_withdrawal_limit(kyc_level):
    limits = {0: 0, 1: 1000, 2: 10000, 3: 100000}
    return limits[kyc_level]


def test_level_1_limit():
    limit = get_withdrawal_limit(1)
    assert limit == 1000

def test_level_3_limit():
    limit = get_withdrawal_limit(3)
    assert limit == 100000

def test_unknown_level_raises_error():
    with pytest.raises(KeyError):
        get_withdrawal_limit(245)