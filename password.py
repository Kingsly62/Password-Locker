class Password:
    '''
    class of the password file
    '''


def __init__(self, page, password):
    self.page = page
    self.password = password


'''
function for class properties
'''

'''
user properties
'''

user_password = []


def save_page(self):
    Password.user_passwords.append(self)
    '''
    save password created by new user
    '''


def delete_page(self):
    Password.user_passwords.remove(self)
    '''
    deletes password created by new user
    '''


def display_page(cls):
    return cls.user_passwords


'''
displays new user passwords generated
'''


def find_by_page(cls, pager):
    for pagy in cls.user_passwords:
        if pagy.page == pager:
            return pagy


'''
function generates new user generated passwords
'''


def page_exists(cls, pager):
    for pagy in cls.user_passwords:
        if pagy.page == pager:
            return pagy
    return False


'''
functions displays already generated account credentials 
'''
