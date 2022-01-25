import unittest 
from credential import Credential 

class TestCredential(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("James","Muriuki","0712345678")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account,"James")
        self.assertEqual(self.new_credential.user_name,"Muriuki")
        self.assertEqual(self.new_credential.password,"0712345678")


if __name__ == '__main__':
    unittest.main()    

def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)

if __name__ ==  '__main__':
    unittest.main()

def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []

# other test cases here
def test_save_multiple_credential(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","user","password") # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)

if __name__ == '__main__':
      unittest.main() 

def test_delete_credential(self):
            self.new_credential.save_credential()
            test_credential = Credential("Test","user","password") # new contact
            test_credential.save_credential()

            self.new_credential.delete_credential()
            self.assertEqual(len(Credential.credential_list),1)
if __name__ == '__main__':
    unittest.main()  

    def test_find_credential_by_account(self):
        '''
        test to check if we can find a credential by account name and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","password") # new contact
        test_credential.save_credential()

        found_credential = Credential.find_by_account("intagram")

        self.assertEqual(found_credential.password,test_credential.password)


def test_credential_exists(self):

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","password") 
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("password")

        self.assertTrue(credential_exists)  

def test_display_credentials(self):
        '''
        method that returns credentials saved
        '''

        self.assertEqual(Credential.display_credential(),Credential.credential_list)        