# #!/usr/bin/env python3.9

#!/usr/bin/env python3.6
from account import Accounts
from password import Password


def create_account(firstname, lastname, username, password):
    accounts = Accounts(firstname, lastname, username, password)
    return accounts


def save_account(accounts):
    accounts.save_account()


def delete_account(accounts):
    accounts.delete_account()


def find_accounts(username):
    return Accounts.find_by_username(username)


def isexist_accounts(username):
    return Accounts.account_exists(username)


def display_accounts():
    return Accounts.display_accounts()


def create_page(page, password):
    passwords = Password(page, password)
    return passwords


def save_page(passwords):
    passwords.save_page()


def find_page(pager):
    return Password.find_by_page(pager)


def isexist_page(pager):
    return Password.page_exists(pager)


def delete_page(passwords):
    passwords.delete_page()


def display_pages():
    return Password.display_page()


def main():
    print('Welcome To PassWord Locker')
    print('Enter Number To Continue........')
    while True:

        print(" 1) Sigin-in \n 2) Register \n 3) ABOUT PASSLOCK \n 4) Display Accounts \n 5) Log out")

        choice = int(input())
        if choice == 1:
            print('Enter username')
            username = input()
            print('Enter passoword')
            password = input()
            account = find_accounts(username)
            if account.user_name == username and account.password == password:

                print('logged in ')
                while True:

                    print(
                        f'Welcome {username}, Use the following numbers to select their corresponding          values')

                    print(
                        ' 1) Save new password \n 2) Delete password \n 3) Display saved passwords \n 4) Log out ')

                    log_choice = int(input())
                    if log_choice == 1:
                        print('New page')
                        print('*'*100)

                        print('Page name')
                        page = input()

                        print('password')
                        password = input()

                    # created and saved page
                        save_page(create_page(page, password))

                    elif log_choice == 2:
                        print("Enter the name of the page you want to delete")

                        page = input()
                        if isexist_page(page):
                            remove_page = (page)
                            delete_page(remove_page)

                        else:
                            print(f'I cant find {page}')

                    elif log_choice == 3:
                        if display_pages():
                            for pag in display_pages():
                                print(
                                    f'{pag.page}:{pag.password}'
                                )
                        else:
                            print('No password account saved yet')
                            print('\n')

                    elif log_choice == 4:
                        print('adios')
                        break
            else:
                print('wrong credentials')

        if choice == 2:
            print('NEW ACCOUNT Name')
            print('*'*100)

            print('Firstname')
            firstname = input()

            print('Lastname')
            lastname = input()

            print('Username')
            username = input()

            print('Enter desired password')
            password = input()

            save_account(create_account(
                firstname, lastname, username, password))
            # create and save a new account
            print('ACCOUNT CREATED')
            while True:

                print(
                    f'Welcome {username}, Use the following numbers to select their corresponding values')
                print(
                    ' 1) Save new password \n 2) Delete password \n 3) Display saved passwords \n 4) Log out ')

                log_choice = int(input())
                if log_choice == 1:
                    print('New page')
                    print('*'*100)

                    print('Page name')
                    page = input()

                    print('password')
                    password = input()

                    # created and saved page
                    save_page(create_page(page, password))

                elif log_choice == 2:
                    print("Select page to delete")

                    page = input()
                    if isexist_page(page):
                        remove_page = (page)
                        delete_page(remove_page)

                    else:
                        print(f'I cant find {page}')

                elif log_choice == 3:
                    if display_pages():
                        for pag in display_pages():
                            print(
                                f'{pag.page}:{pag.password}'
                            )
                    else:
                        print('NO PASSWORD SAVED YET')

                elif log_choice == 4:
                    break

        elif choice == 3:
            print('Password-Locker???')
            print(
                '''
            Passlock is an sort of script application that allows you to store  password from different ccounts. In case of many accounts on social media passlock can be used to store the different password from the social media  account.Prevents hackers from accessing your account details
                                    ''')

        elif choice == 4:
            if display_accounts():
                for account in display_accounts():
                    print(
                        f'{account.username}'
                    )
            else:
                print('no account available')

        elif choice == 5:
            print('adios')
            break


if __name__ == '__main__':
    main()
