from user import User
import unittest


class Test(unittest.TestCase):
    def tearDown(self):
        '''
        this test clears the user_passwords array beore every test
        '''
        User.user_passwords = []

    def setUp(self):
        '''
        this test creates a new instance of the passwords class
        before every test
        '''
        self.new_password = User('instagram', '454545')

    def test_init(self):
        '''
        this test checks whether the data enterd into the properties if called wll appear
        '''
        self.assertEqual(self.new_password.account, 'instagram')
        self.assertEqual(self.new_password.password, '454545')

    def test_save_account(self):
        '''
        this is a test to check whether the value append to the user_passwords array
        '''
        self.new_password.save_account()
        self.assertEqual(len(User.user_passwords), 1)

    def test_save_multiple(self):
        '''
        this test like the first now test whether both instances created are appended to the array
        '''
        self.new_password.save_account()
        test_pass = User('twitter', '545454')
        test_pass.save_account()
        self.assertEqual(len(User.user_passwords), 2)

    def test_delete_account(self):
        '''
        this test checks for the delete function that uses the .remove methos
        '''
        self.new_password.save_account()
        test_pass = User('twitter', '545454')
        test_pass.save_account()
        self.new_password.delete_account()
        self.assertEqual(len(User.user_passwords), 1)

    def test_display_account(self):
        self.assertEqual(User.display_account(), User.user_passwords)

    def test_find_account(self):
        '''
        this test checks whether a password saved can be searched
        '''
        self.new_password.save_account()
        test_pass = User('twitter', '545454')
        test_pass.save_account()
        found_account = User.find_by_account('twitter')
        self.assertEqual(found_account.account, test_pass.account)

    def account_exists(self):
        '''
        returns a true/false value depending on prescence of the searched password
        '''
        self.new_password.save_account()
        test_pass = User('twitter', '545454')  # new contact
        test_pass.save_account()
        account_exist = User.account_exists('twitter')
        self.assertTrue(account_exist)


if __name__ == '__main__':
    unittest.main()
