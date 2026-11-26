import pytest
from app.limits import get_withdrawal_limit, can_withdraw


def test_level_1_limit():
    limit = get_withdrawal_limit(1)
    assert limit == 1000

def test_level_3_limit():
    limit = get_withdrawal_limit(3)
    assert limit == 100000

def test_unknown_level_raises_error():
    with pytest.raises(KeyError):
        get_withdrawal_limit(245)

def test_withdraw_within_limit_allowed():
    kyc_level = 1
    amount = 500
    result = can_withdraw(kyc_level, amount)
    assert result, "User with KYC level 1 should be able to withdraw 1000"

def test_withdraw_boundary_limit_allowed():
    kyc_level = 1
    amount = 1000
    result = can_withdraw(kyc_level, amount)
    assert result, "User with KYC level 1 should be able to withdraw 1000"

def test_withdraw_over_limit_forbidden():
    kyc_level = 1
    amount = 1001
    result = can_withdraw(kyc_level, amount)
    assert not result, "User with KYC level 1 shouldn't be able to withdraw 1001"
