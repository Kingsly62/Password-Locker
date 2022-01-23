class Accounts:
    def __init__(self, firstname, lastname, email, username):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username


user_accounts = []


def save_user(self):

    Accounts.user_accounts.append(self)


'''
   save_user saves new user
   '''


def delete_user(self):
    '''
   used to delete new user account
   '''

    Accounts.user_accounts.remove(self)


@classmethod
def find_by_username(cls, username):
    '''
    used to check username provided whether its true and returns the accounts if its true
    '''

    for account in cls.user_accounts:
        if account.username == username:
            return account


@classmethod
def account_exists(cls, username):
    '''
    loops through the function to check whether the account provided is true
    '''
    for account in cls.user_accounts:
        if account.username == username:
            return True
        return False


@classmethod
def display_accounts(cls):
    return cls.user_accounts


'''
displays the account of the user
'''
