
from resources.config import settings_core
from resources.utility import string_to_list_of_dictionaries

settings = settings_core()


# need to have a proper setup for accounts. the data in the posts class is fine, it's only used as an id to tie to the accounts here. 

# Account secrets need to be encrypted

# need to basically move the setting "media accounts" to this class and give it an enumeration or id or something for which social media it is using. 


########## ACCOUNT CLASS

class Account:

    ########## INIT
    #####
    def __init__(self, display_name=None, name=None, key=None, secret=None, access_key=None, access_secret=None, media_platform=None):
        self.data = {
            "display_name": display_name,
            "name": name,
            "key": key,
            "secret": secret,
            "access_key": access_key,
            "access_secret": access_secret,
            "media_platform": media_platform
        }



    ########## LOAD DATA
    #####
    def load_data(self):
        data_loaded = False

        ## Load Account Data from Settings
        accounts = string_to_list_of_dictionaries(settings.read_encrypted_setting("accounts", "media_accounts"))

        for account in accounts:
            if account["name"] == self.data['name']:
                self.data = account
                data_loaded = True
                break

        return data_loaded
        

    ########## DATA TO LIST
    #####
    def data_to_list(self,data):

        display_name = data["display_name"]
        name = data["name"]
        key = data["key"]
        secret = data["secret"]
        access_key = data["access_key"]
        access_secret = data["access_secret"]
        media_platform = data["media_platform"]

        if data["access_key"] != None:
            return f"{display_name}|-|{name}|-|{key}|-|{secret}|-|{access_key}|-|{access_secret}|-|{media_platform}"
        else:
            return f"{display_name}|-|{name}|-|{key}|-|{secret}|-|{access_key}|-|{access_secret}|-|{media_platform}"


    ########## REGISTER
    #####
    def register(self, display_name, key, secret, access_key=None, access_secret=None, media_platform=None):
        # convert data to dictioinary
        data = {
            "display_name": display_name,
            "name": self.data['name'],
            "key": key,
            "secret": secret,
            "access_key": access_key,
            "access_secret": access_secret,
            "media_platform": media_platform
        }

        accounts = settings.media_accounts
        if accounts:
            accounts.append(data)
            # save new accounts
            settings.write_encrypted_setting("accounts","media_accounts",str(accounts))
        else:
            settings.write_encrypted_setting("accounts","media_accounts",str([data]))

        

    ########## UPDATE
    #####
    def update(self, display_name=None, key=None, secret=None, access_key=None, access_secret=None, media_platform=None):
        # get current accounts and add new one
        accounts = settings.media_accounts
        for account in accounts:
            if account["name"] == self.data['name']:
                account["display_name"] = display_name
                account["key"] = key
                account["secret"] = secret
                account["access_key"] = access_key
                account["access_secret"] = access_secret
                account["media_platform"] = media_platform
                break
        # save new accounts
        settings.write_encrypted_setting("accounts","media_accounts",str(accounts))

    
    ########## REMOVE
    #####
    def remove(self, name):
        # get current accounts and remove one
        accounts = self.media_accounts
        for account in accounts:
            if account['name'] == name:
                accounts.remove(account)
                break

        ## Save New Accounts
        self.write_encrypted_setting("accounts","media_accounts",str(accounts))

    



# Class for managing multiple accounts at once / posting. 
class AccountManager:
    def __init__(self):
        self.accounts = []
        print('Account Manager started')
