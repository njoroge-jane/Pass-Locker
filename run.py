#!/usr/bin/env python3.8

from sqlalchemy import select
from credential import Credential
from user import User
import random


def create_credentials(account_name, user_name, password):
    credential = Credential(account_name, user_name, password)
    return credential


def save_credential(credential):
    credential.save_credential()


def delete_credential(credential):
    credential.delete_credential()


def find_accounts(user_name):
    return Credential.find_by_user_name(user_name)


def exist_accounts(user_name):
    return Credential.account_exists(user_name)


def display_credentials():
    return Credential.display_credentials()


def create_account(account, password):
    accounts = User(account, password)
    return accounts


def save_account(accounts):
    accounts.save_account()


def find_account(accounts):
    return User.find_by_account(accounts)


def isexist_account(accounts):
    return User.account_exists(accounts)


def delete_account(accounts):
    accounts.delete_account()


def display_account():
    return User.display_account()


def main():
    print('PASSWORD LOCKER')
    print('Select action below')
    while True:

        print(" 1. LOGIN \n 2. SIGN UP  \n 3. DISPLAY ACCOUNTS \n 4. SIGN OUT")

        selected = int(input())
        if selected == 1:
            print('Enter account name')
            name_account = input()
            print('Enter username')
            username = input()
            print('Enter passoword')
            password = input()
            account = find_account(name_account)
            if account:

                if account.account == name_account and account.password == password:

                    print('logged in ')
                    while True:

                        print(
                            f'Welcome {username}, select action below using corresponding number')

                        print(
                            ' 1. Save new password \n 2. Delete password \n 3. Display saved passwords')

                        selectOption = int(input())
                        if selectOption == 1:
                            print('New account')

                            print('account name')
                            account = input()

                            print('1. Create password \n 2.Generate password')
                            choice = int(input())
                            if choice == 1:

                                print('password')
                                password = input()
                            elif choice == 2:
                                randoms = random.randint(1000,9999)
                                print(randoms) 
                                password = randoms

                            else:
                                print('Not an option')      

                            save_account(create_account(account, password))

                        elif selectOption == 2:
                            print("Enter the name of the account you want to delete")

                            account = input()
                            if isexist_account(account):
                                # remove_account = (account)
                                delete_account(isexist_account(account))

                            else:
                                print(f'{account} does not exist')

                        elif selectOption == 3:
                            if display_account():
                                for acc in display_account():
                                    print(
                                        f'{acc.account}:{acc.password}'
                                    )
            else:
                print('Does not exist')

        if selected == 2:
            print('Sign Up New acc')

            print('Enter Account Name')
            account_name = input()

            print('Enter Username')
            user_name = input()

            print('Enter Password')
            password = input()

            save_account(create_account(
                account_name, password))

            print('Successful')

        elif selected == 3:
            if display_account():
                for account in display_account():
                    print(
                        f'{account.account}'
                    )
            else:
                print('Nothing Yet')

        elif selected == 4:
            print('Thank YOU')
            break


if __name__ == '__main__':
    main()
