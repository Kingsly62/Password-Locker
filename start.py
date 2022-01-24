from account import Accounts
from password import Password


def create_account(firstname, lastname, email, password):
    account = Accounts(firstname, lastname, email, password)
    return account


def save_account(account):
    account.save_account()


def delete_account(account):
    account.delete_account()


def find_account(username):
    return Accounts.find_by_username(username)


def isexist_page(pager):
    return Password.page_exist(pager)


def delete_page(password):
    password.delete_page()


def display_page():
    return Password.display_page()


def main():
    print('Welcome To PASSWORD-LOCKER')
    print('Press number below to continue')
    while True:
        print(
            '1)Login\n 2) Register\n 3) About Passlock\n 4) Available Accounts\n 5) Logout')
