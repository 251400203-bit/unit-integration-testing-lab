import pytest
from bank_app import transfer, calculate_interest


def test_transfer_success():
    b1, b2 = transfer(1000, 500, 300)
    assert b1 == 700
    assert b2 == 800


def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(200, 500, 400)


def test_transfer_and_interest():
    b1, b2 = transfer(2000, 1000, 500)
    interest_balance = calculate_interest(b2, 10, 1)

    # FIX: floating point precision issue
    assert round(interest_balance, 2) == 1650
