"""
Programmer: Boris Sodji
Date: 11AUG23
Lab 12
"""
# Creating a class named Account
class Account:
    """
    Initialized method
    :param name: name on the account
    """
    def __init__(self, name: str) -> None:
        self.__account_name = name
        self.__account_balance = 0
# Deposit transaction
    """
    This method deposit money into the account
    :param amount: amount being deposited
    :return: False if the transaction failed
    """
    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self.__account_balance += amount
            return  True
        else:
            return False
    """
    This method withdraw money into the account
    :param amount: amount being deposited
    :return: False if the transaction failed
    """
# Withdrawal transaction
    def withdraw(self,amount: float) -> bool:

        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
    """
    This method show the account balance
    :return: account_balance
    """
# Account balance
def get_balance(self) -> float:
    return self.__account_balance

# Account name
  """
    This method show the account name
    :return: account_name
    """
def __get_name(self) -> str :
    return self.__account_name