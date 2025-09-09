import pyinputplus as pyip
from gkeep import TestGKeep

if __name__ == "__main__":
    
    email = pyip.inputEmail(prompt='Please enter your email address: ')
    my_gkeep = TestGKeep(email=email) # Create a gkeep object

    token_type = pyip.inputChoice(choices=['mt', 'ot'], prompt='Please note if you have a master token or a oauth token by inputing mt or ot: ')
    if token_type == 'mt':
        master_token = pyip.inputPassword(prompt='Please enter your master token: ')
        my_gkeep.master_token = master_token # Update master token
        my_gkeep.login() # Login
    elif token_type == 'ot':
        oauth_token = pyip.inputPassword(prompt='Please enter your oauth token: ')
        my_gkeep.generate_master_token(oauth_token=oauth_token)
        my_gkeep.login()

    my_gkeep.create_list() # Create a sample list
    my_gkeep.read_list() # Read the sample list

        
