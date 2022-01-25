class User:
    def __init__(self, account, password):
        '''
        initializing method
        '''
        self.account = account
        self.password = password

    user_passwords = []

    def save_account(self):
        '''
        save account
        '''
        User.user_passwords.append(self)

    def delete_account(self):
        '''
        delete account
        '''
        User.user_passwords.remove(self)

    @classmethod
    def display_account(cls):
        '''
        method that dispalys the account details
        '''
        return cls.user_passwords

    @classmethod
    def find_by_account(cls, accounts):
        '''
        method finds specific account via account name
        '''
        for account in cls.user_passwords:
            if account.account == accounts:
                return account

    @classmethod
    def account_exists(cls, accounts):
        '''
        method that checks whether an account is already created
        '''
        for account in cls.user_passwords:
            if account.account == accounts:
                return account
        return False
