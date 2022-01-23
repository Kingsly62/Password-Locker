from password import Password
import unittest


class testPasswords(unittest.TestCase):
    def tearDown(self):
        '''
        deletes user password input
        '''


Password.user_passwords = []


def setUp(self):
    self.new_password = Password('twitter', '1234')


def test_init(self):
    '''
    tests whether data entered is clearly stated
    '''
    self.assertEqual(self.new_password.page, 'twitter')
    self.assertEqual(self.new_password.password, '1234')
    '''
    tests whether data entered is clearly stated
    '''


def test_save_page(self):
    '''
    saves appended new passwords
    '''
    self.new_password.save_page()
    self.assertEqual(len(Password.user_passwords), 1)


def test_delete_page(self):
    '''
    this test  checks for delete page 
    '''
    self.new_password.save_page()
    test_pass = Password('twitter', '1234')
    test_pass.save_page()
    self.new_password.delete_page()
    self.assertEqual(len(Password.user_passwords), 1)


def test_display_page(self):
    self.assertEqual(Password.display_page(), Password.user_passwords)


def test_find_page(self):
    '''
    this test checks whether a password saved can be searched
    '''
    self.new_password.save_page()
    test_pass = Password('twitter', '1234')
    test_pass.save_page()
    found_page = Password.find_by_page('twitter')
    self.assertEqual(found_page.page, test_pass.page)


def page_exists(self):
    '''
    returns a true/false value
    '''
    self.new_password.save_page()
    test_pass = Password('twitter', '1234')
    test_pass.save_page()
    page_exist = Password.page_exists('twitter')
    self.assertTrue(page_exist)


if __name__ == '__main__':
    unittest.main()
