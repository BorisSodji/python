import pytest

from account import *


class Test:
    def setup(self):
        self.account_one = Account('John')

    def teardown(self):
        del self.account_one

    def test_init(self):
        assert self.account_one.get_name() == 'John'
        assert self.account_one.get_balance() == pytest.approx(0)

    def test_deposit(self):
        assert self.account_one.deposit(-100) is False
        assert self.account_one.get_balance() == pytest.approx(0)

        assert self.account_one.deposit(0) is False
        assert self.account_one.get_balance() == pytest.approx(0)

        assert self.account_one.deposit(100) is True
        assert self.account_one.get_balance() == pytest.approx(100)

    def test_withdraw(self):
        assert self.account_one.withdraw(-100) is False
        assert self.account_one.get_balance() == pytest.approx(0)

        assert self.account_one.withdraw(0) is False
        assert self.account_one.get_balance() == pytest.approx(0)

        self.account_one.deposit(200)
        assert self.account_one.withdraw(100) is True
        assert self.account_one.get_balance() == pytest.approx(100)
