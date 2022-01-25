class Credential:

    def __init__(self,account_name,user_name,password):

        '''
        Args:
            user_name : New credential user name.
            password: New credential password.
        '''
        self.account_name= account_name
        self.user_name = user_name
        self.password = password

    credential_list = [] 
  
    def save_credential(self):

        Credential.credential_list.append(self)  
    def delete_credential(self):

        Credential.credential_list.remove(self)  

    @classmethod
    def find_by_user_name(cls, user_name):    
     for credential in cls.credential_list:
            if credential.user_name == user_name:
                return credential               

    @classmethod
    def account_exists(cls, user_name):
        for credential in cls.credential_list:
            if credential.user_name == user_name:
                    return True

        return False
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials
        '''
        return cls.credential_list