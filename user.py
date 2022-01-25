class User:
    def __init__(self, account, password):
        self.account = account
        self.password = password

    user_passwords = []

    def save_account(self):
        User.user_passwords.append(self)

    def delete_account(self):
        User.user_passwords.remove(self)

    @classmethod
    def display_account(cls):
        return cls.user_passwords

    @classmethod
    def find_by_account(cls, accounts):
        for account in cls.user_passwords:
            if account.account == accounts:
                return account

    @classmethod
    def account_exists(cls, accounts):
        for account in cls.user_passwords:
            if account.account == accounts:
                return account
        return False
