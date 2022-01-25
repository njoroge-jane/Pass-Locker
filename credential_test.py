import unittest 
from credential import Credential 

class TestCredential(unittest.TestCase):
    def tearDown(self):

            Credential.credential_list = []

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("linkedin","janey","123456")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account_name,"linkedin")
        self.assertEqual(self.new_credential.user_name,"janey")
        self.assertEqual(self.new_credential.password,"123456")
   

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)



    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("telegram","mary","989898") # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list), 2)

    def test_delete_credential(self):
            self.new_credential.save_credential()
            test_credential = Credential("telegram","mary","989898") 
            test_credential.save_credential()

            self.new_credential.delete_credential()
            self.assertEqual(len(Credential.credential_list), 1)

    def test_find_by_user_name(self):
        '''
        test to check if we can find a credential by user name and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("telegram","mary","989898") 
        test_credential.save_credential()

        found_credential = Credential.find_by_user_name("mary")

        self.assertEqual(found_credential.user_name, test_credential.user_name)


    def test_account_exists(self):

        self.new_credential.save_credential()
        test_credential = Credential("telegram","mary","989898") 
        test_credential.save_credential()

        credential_exists = Credential.account_exists("mary")

        self.assertTrue(credential_exists)  

    def test_display_credentials(self):
        '''
        method that returns credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)
        
if __name__ ==  '__main__':
    unittest.main()