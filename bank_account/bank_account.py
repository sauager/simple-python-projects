from abc import ABC, abstractmethod
import json
from datetime import datetime
import random


class AbstractBankClass(ABC):
    """Abstract class for Bank System"""

    @property
    @abstractmethod
    def balance(self):
        """self balance getter"""
        pass

    @abstractmethod
    def pin_accuracy(self, value):
        """Checks does 'value' coincide with self pin code"""
        pass

    @abstractmethod
    def deposit(self, value, pincode_verification):
        """tops up self balance with 'value' and checks if 'pincode_verification' coincide with self pin code"""
        pass

    @abstractmethod
    def _deposit_admin(self, value):
        """the same method as 'deposit' method, but do not request pincode verification"""
        pass

    @abstractmethod
    def _validate_deposit(self, value):
        """checks if deposit by 'value' possible"""
        pass

    @abstractmethod
    def withdraw(self, value, pincode_verification):
        """withdraw operation from self balance with 'value' amount of money.
        Checks if 'pincode_verification' coincide with self pin code"""
        pass

    @abstractmethod
    def _withdraw_admin(self, value):
        """the same method as 'withdraw' method, but do not request pincode verification"""
        pass

    @abstractmethod
    def _validate_withdraw(self, value):
        """checks if withdraw by 'value' possible"""
        pass

    @abstractmethod
    def transfer(self, other, value, pincode_verification):
        """transfer operation from one user to another.
        args:
            other: another user
            value: amount of money to transfer
            pincode_verification: self pincode verification
            """
        pass

    @abstractmethod
    def _get_account_info(self):
        """returns dictionary with Bank Account data"""
        pass

    @abstractmethod
    def _get_account_info_json(self):
        """returns json formatted string with Bank Account data"""
        pass

    @abstractmethod
    def change_pin(self, pincode_verification, new_pin):
        """Changes an old self pin code to new one"""
        pass

    @abstractmethod
    def are_balances_equal(self, other):
        """Checks if self balance equals other balance"""
        pass

    @abstractmethod
    def _get_account_operations_history(self):
        """returns list with all self operations ever"""
        pass

    @abstractmethod
    def _get_account_operations_history_json(self):
        """returns json format with all self operations ever"""
        pass

    @abstractmethod
    def set_new_random_pin(self):
        """Changes an old self pin code to new random one"""
        pass


class Errors:
    """Potential errors that may appear while doing some operations"""

    @staticmethod
    def value_error():
        raise ValueError('Please,Choose right values')

    @staticmethod
    def init_error():
        raise ValueError('Choose right value(s) for initialization')

    @staticmethod
    def withdraw_error():
        raise ValueError('Your credit card balance is too low to do this operation')

    @staticmethod
    def pincode_error():
        raise ValueError("You've entered wrong pin code")

    @staticmethod
    def instance_error(other):
        raise TypeError(f"Object {other} is not a BankAccount object")

    @staticmethod
    def new_pin_error():
        raise ValueError("You've entered wrong value for new pin code")


class BankInit:
    """Userdata initialisation"""

    __slots__ = ('name', 'surname', '_balance', '_pin_code', 'id', '_operations')

    def __init__(self, name: str, surname: str, balance: int | float, pin_code: str):
        # name
        if isinstance(name, str):
            self.name = name
        else:
            Errors.init_error()
        # surname
        if isinstance(surname, str):
            self.surname = surname
        else:
            Errors.init_error()
        # balance
        if isinstance(balance, (int, float)) and balance >= 0:
            self._balance = float(balance)
        else:
            Errors.init_error()
        # pin_code
        if isinstance(pin_code, str) and pin_code.isdigit() and 1000 <= int(pin_code) <= 9999:
            self._pin_code = pin_code
        else:
            Errors.init_error()
        # id
        BankAccount._user_id = str(int(BankAccount._user_id) + 1).zfill(5)
        self.id = BankAccount._user_id
        # operations_history
        self._operations = []


class Dunder:

    def __eq__(self, other):
        if not isinstance(self, BankAccount):
            Errors.instance_error(self)
        if not isinstance(other, BankAccount):
            Errors.instance_error(other)
        return self._balance == other._balance


class BankAccount(BankInit, AbstractBankClass, Dunder):
    """Main Bank Account class"""
    _user_id = '00000'
    __slots__ = tuple()

    @property
    def balance(self):
        return self._balance

    def pin_accuracy(self, value):
        if value == self._pin_code:
            return True
        return False

    def deposit(self, value, pincode_verification):
        if self.pin_accuracy(pincode_verification):
            if isinstance(value, (int, float)):
                if value >= 0:
                    self._balance += value
                    self._operations.append({'operation': 'deposit', 'value': '+' + str(value),
                                             'date': datetime.now().strftime(f'%d/%m/%y %X')})
                else:
                    Errors.value_error()
            else:
                Errors.value_error()
        else:
            Errors.pincode_error()

    def _deposit_admin(self, value):
        if isinstance(value, (int, float)):
            if value >= 0:
                self._balance += value
                self._operations.append(
                    {'operation': 'deposit', 'value': '+' + str(value),
                     'date': datetime.now().strftime(f'%d/%m/%y %X')})
            else:
                Errors.value_error()
        else:
            Errors.value_error()

    def _validate_deposit(self, value):
        if isinstance(value, (int, float)):
            if value >= 0:
                pass
            else:
                Errors.value_error()
        else:
            Errors.value_error()

    def withdraw(self, value, pincode_verification):
        if self.pin_accuracy(pincode_verification):
            if isinstance(value, (int, float)):
                if value <= self._balance:
                    if value >= 0:
                        self._balance -= value
                        self._operations.append(
                            {'operation': 'withdraw', 'value': '-' + str(value),
                             'date': datetime.now().strftime(f'%d/%m/%y %X')})
                    else:
                        Errors.value_error()
                else:
                    Errors.withdraw_error()
            else:
                Errors.value_error()
        else:
            Errors.pincode_error()

    def _withdraw_admin(self, value):
        if isinstance(value, (int, float)):
            if value <= self._balance:
                if value >= 0:
                    self._balance -= value
                    self._operations.append(
                        {'operation': 'withdraw', 'value': '-' + str(value),
                         'date': datetime.now().strftime(f'%d/%m/%y %X')})
                else:
                    Errors.value_error()
            else:
                Errors.withdraw_error()
        else:
            Errors.value_error()

    def _validate_withdraw(self, value):
        if isinstance(value, (int, float)):
            if value <= self._balance:
                if value >= 0:
                    pass
                else:
                    Errors.value_error()
            else:
                Errors.withdraw_error()
        else:
            Errors.value_error()

    def transfer(self, other, value, pincode_verification):
        if not isinstance(other, BankAccount):
            Errors.instance_error(other)

        self._validate_withdraw(value)
        other._validate_deposit(value)

        self.withdraw(value, pincode_verification)
        other._deposit_admin(value)

    def _get_account_info(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'balance': self._balance,
            'id': self.id
        }

    def _get_account_info_json(self):
        data = self._get_account_info()
        return json.dumps(data, ensure_ascii=False)

    def change_pin(self, pincode_verification, new_pin):
        if self.pin_accuracy(pincode_verification):
            if isinstance(new_pin, str) and new_pin.isdigit() and 1000 <= int(new_pin) <= 9999:
                self._pin_code = new_pin
            else:
                Errors.new_pin_error()
        else:
            Errors.pincode_error()

    def are_balances_equal(self, other):
        return self.__eq__(other)

    def _get_account_operations_history(self):
        return self._operations

    def _get_account_operations_history_json(self):
        data = self._get_account_operations_history()
        return json.dumps(data, ensure_ascii=False)

    def set_new_random_pin(self):
        new_rand_pin = str(random.randint(1000, 9999))
        self._pin_code = new_rand_pin
