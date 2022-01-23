from account import Accounts
import unittest


class testCredentials(unittest.TestCase):
    def tearDown(self):
        Accounts.user_accounts = []


def setUp(self):
    '''
    runs before every tests runs
    '''
    self.new_account = Accounts(
        'clinton', 'kioge', 'clinton72@gmail.com', 'kingsly')


def test_init(self):
    '''
    test every credentiials whether its its true,when property is callled
    '''
    self.assertEqual(self.new_account.firstname, 'clinto')
    self.assertEqual(self.new_account.lastname, 'kioge')
    self.assertEqual(self.new_account.email, 'clinton72@gmail.com')
    self.assertEqual(self.new_account.username, 'kingsly')


def test_save_account(self):
    '''
    tests the saved accounts users
    '''
    self.new_account.save_account()
    self.assertEqual(len(Accounts.user_accounts), 1)


def test_save_multiple_accounts(self):
    '''
    a test that checks whether both values appended to the array are actually present\ and returns the acount itself
    '''
    self.new_account.save_account()
    test_account = Accounts('abcd', 'efgh', 'ijkl', 'mnop')
    test_account.save_account()
    self.assertEqual(len(Accounts.user_accounts), 2)


def test_del_account(self):
    '''
    test that check the delete function
    '''
    self.new_account.save_account()
    test_account = Accounts('abcdeefghiklmnopqrstuvwxyx')
    test_account.save_account()
    self.new_account.delete_account()
    self.assertEqual(len(Accounts.user_accounts), 1)


def test_find_account_by_username(self):
    '''
    test to check whether the function used to find accounts really works
    '''
    self.new_account.save_account()
    test_account = Accounts('abcdefghijklmnopqrstuvwxyz')
    test_account.save_account()
    found_account = Accounts.find_by_username('abcdefghijklmnopqrstuvwxyz')
    self.assertEqual(found_account.username, test_account.username)


def test_account_exists(self):
    '''
    unlike the previous test this test returns a true/false soort of answer depending on whether the account exists or not
    '''
    self.new_account.save_account()
    test_account = Accounts('abcdefghijklmnopqrstuvwxyz')
    test_account.save_account()
    account_exists = Accounts.account_exists('abcdefghijklmnopqrstuvwxyz')
    self.assertTrue(account_exists)


def test_display_accounts(self):
    '''
    a test to check the display accounts function
    '''
    self.assertEqual(Accounts.display_accounts(),
                     Accounts.user_accounts)


if __name__ == '__main__':
    unittest.main()
