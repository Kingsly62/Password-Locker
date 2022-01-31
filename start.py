# #!/usr/bin/env python3.9
# from account import Accounts
# from password import Password


# def create_account(firstname, lastname, username, email, password):
#     account = Accounts(firstname, lastname, username, email, password)
#     return account


# def save_page(account):
#     account.save_account()


# def delete_account(account):
#     account.delete_account()


# def find_account(username):
#     return Accounts.find_by_username(username)


# def isexist_page(pager):
#     return Password.page_exist(pager)


# def delete_page(password):
#     password.delete_page()


# def display_page():
#     return Password.display_page()


# def main():
#     print('Welcome To PASSWORD-LOCKER')
#     print('Press number below to continue')
#     while True:
#         print(
#             '1)Login\n 2) Register\n 3) About Passlock\n 4) Available Accounts\n 5) Logout')

#         choice = int(input())
#         if choice == 1:
#             print('Enter your  username')
#             username = input()
#             print('Enter your  password')
#             account = find_account(username)
#             if account.username == username and account.password == password:
#                 print('Already logged in')
#                 while True:
#                     print(
#                         f'Welcome {username}, use the numbers below to select values')
#                     print(
#                         '1)Save new Password \n 2) Delete Password \n 3)Display saved password credentials \n 4)Logout')
#                     log_choice = int(input())
#                     if log_choice == 1:
#                         print('New Page')
#                         print('*'*100)

#                         print("Kindly provide your page name")
#                         page = input()
#                         print('Provide password')
#                         password = input()

#                         save_page(create_account(page, password))
#                     elif log_choice == 2:
#                         print('Enter name to be erased')
#                         page = input()
#                         if isexist_page(page):
#                             remove_page = (page)
#                             delete_page(remove_page)

#                     elif log_choice == 3:
#                         if display_page():
#                             for pag in display_page():
#                                 print(
#                                     f'{pag.page}:{pag.password}'
#                                 )
#                             else:
#                                 print('No password')
#                                 print('/n')

#                         elif log_choice == 4:
#                             print('welcome again')
#                             break
#                         else:
#                             print('Wrong credentials provided')

#                     if choice == 2:
#                         print('New Account')
#                         print('*'*100)

#                         print('Enter first Name')
#                         firstname = input()

#                         print('Enter last Name')
#                         lastname = input()

#                         print('Enter username')
#                         username = input()

#                         print('Enter Preferred EMAIL')
#                         email = input()

#                         print('Enter passWord')
#                         password = input()

#                         save_page(create_account(
#                             firstname, lastname, username, email, password))

#                         print('SUCCESSFULLY CREATED ACCOUNT')
#                         while True:
#                             print(
#                                 f'Welcome{username} Select the Numbers To Continue')
#                             print(
#                                 f'1)Save Password \n 2)Delete password \n 3)Display saved password\n 4)Logout')
#                             log_choice = int(input())

#                             if log_choice == 1:
#                                 print('New Page')
#                                 print('*'*100)

#                                 print('Provide Name Page')
#                                 page = input()

#                                 print('Enter your password')
#                                 password = input()

#                                 save_page(create_account(page, password))
#                             elif log_choice == 2:
#                                 print('Enter name of page to delated')

#                                 page = input()
#                                 if isexist_page(page):
#                                     remove_page = (page)
#                                     delete_page(remove_page)

#                                 else:
#                                     print(f'Page not available')

#                             elif log_choice == 3:
#                                 if display_page():
#                                     for pag in display_page:
#                                         print
#                                 print(f'{pag.page}:{pag.password}')
#                             else:
#                                 print('No password saved yet')
#                     elif log_choice == 4:
#                         break

#                     elif choice == 4:
#                         if display_page():
#                             for account in display_page():
#                                 print(f'{username}')

#                             else:
#                                 print('No accounts Found')

#                         elif choice == 5:
#                             print('Try again later')

#     if __name__ == ' __main__':
#         main()


#!/usr/bin/env python3.6
from account import Accounts
from password import Password


def create_account(first_name, last_name, user_name, password):
    accounts = Accounts(first_name, last_name, user_name, password)
    return accounts


def save_account(accounts):
    accounts.save_account()


def delete_account(accounts):
    accounts.delete_account()


def find_accounts(user_name):
    return Accounts.find_by_user_name(user_name)


def isexist_accounts(user_name):
    return Accounts.account_exists(user_name)


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
    print('WELCOME TO PASSLOCK')
    print('Use the following numbers to pick their corresponding values')
    while True:

        print(" 1) LOGIN \n 2) SIGN UP \n 3) ABOUT PASSLOCK \n 4) DISPLAY ACCOUNTS \n 5) SIGN OUT")

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
                            print('NO PASSWORD SAVED YET')
                            print('\n')

                    elif log_choice == 4:
                        print('adios')
                        break
            else:
                print('wrong credentials')

        if choice == 2:
            print('NEW ACCOUNT')
            print('*'*100)

            print('FIRSTNAME')
            first_name = input()

            print('LASTNAME')
            last_name = input()

            print('USERNAME')
            user_name = input()

            print('PASSWORD')
            password = input()

            save_account(create_account(
                first_name, last_name, user_name, password))
            # create and save a new account
            print('ACCOUNT CREATED')
            while True:

                print(
                    f'Welcome {user_name}, Use the following numbers to select their corresponding values')
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
                        print('NO PASSWORD SAVED YET')

                elif log_choice == 4:
                    break

        elif choice == 3:
            print('What password is about')
            print(
                '''
            Passlock is an sort of script application that allows you to store  password from different ccounts. In case of many accounts on social media passlock can be used to store the different password from the social media  accounts.Instead of having to use one password for all your sites so that you can remember  easily,you can use different password and store them in passlock and only have to remember your passlock password. This can prove to be very helpful especially  against hackers.
                                    ''')

        elif choice == 4:
            if display_accounts():
                for account in display_accounts():
                    print(
                        f'{account.user_name}'
                    )
            else:
                print('NO ACCOUNTS')

        elif choice == 5:
            print('adios')
            break


if __name__ == '__main__':
    main()
