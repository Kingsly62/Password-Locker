from account import Accounts
from password import Password


def create_account(firstname, lastname, username, email, password):
    account = Accounts(firstname, lastname, username, email, password)
    return account


def save_page(account):
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

        choice = int(input())
        if choice == 1:
            print('Enter your  username')
            username = input()
            print('Enter your  password')
            account = find_account(username)
            if account.username == username and account.password == password:
                print('Already logged in')
                while True:
                    print(
                        f'Welcome {username}, use the numbers below to select values')
                    print(
                        '1)Save new Password \n 2) Delete Password \n 3)Display saved password credentials \n 4)Logout')
                    log_choice = int(input())
                    if log_choice == 1:
                        print('New Page')
                        print('*'*100)

                        print("Kindly provide your page name")
                        page = input()
                        print('Provide password')
                        password = input()

                        save_page(create_account(page, password))
                    elif log_choice == 2:
                        print('Enter name to be erased')
                        page = input()
                        if isexist_page(page):
                            remove_page = (page)
                            delete_page(remove_page)

                    elif log_choice == 3:
                        if display_page():
                            for pag in display_page():
                                print(
                                    f'{pag.page}:{pag.password}'
                                )
                            else:
                                print('No password')
                                print('/n')

                        elif log_choice == 4:
                            print('welcome again')
                            break
                        else:
                            print('Wrong credentials provided')

                    if choice == 2:
                        print('New Account')
                        print('*'*100)

                        print('Enter first Name')
                        firstname = input()

                        print('Enter last Name')
                        lastname = input()

                        print('Enter username')
                        username = input()

                        print('Enter Preferred EMAIL')
                        email = input()

                        print('Enter passWord')
                        password = input()

                        save_page(create_account(
                            firstname, lastname, username, email, password))

                        print('SUCCESSFULLY CREATED ACCOUNT')
                        while True:
                            print(
                                f'Welcome{username} Select the Numbers To Continue')
                            print(
                                f'1)Save Password \n 2)Delete password \n 3)Display saved password\n 4)Logout')
                            log_choice = int(input())

                            if log_choice == 1:
                                print('New Page')
                                print('*'*100)

                                print('Provide Name Page')
                                page = input()

                                print('Enter your password')
                                password = input()

                                save_page(create_account(page, password))
                            elif log_choice == 2:
                                print('Enter name of page to delated')

                                page = input()
                                if isexist_page(page):
                                    remove_page = (page)
                                    delete_page(remove_page)

                                else:
                                    print(f'Page not available')

                            elif log_choice == 3:
                                if display_page():
                                    for pag in display_page:
                                        print
                                print(f'{pag.page}:{pag.password}')
                            else:
                                print('No password saved yet')
                    elif log_choice == 4:
                        break

                    elif choice == 4:
                        if display_page():
                            for account in display_page():
                                print(f'{username}')

                            else:
                                print('No accounts Found')

                        elif choice == 5:
                            print('Try again later')
                            break

    if __name__ == ' __main__':
        main()
