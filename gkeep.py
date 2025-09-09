import gpsoauth, sys
import gkeepapi
from gkeepapi.exception import LoginException

class TestGKeep:
    def __init__(self, email):
        self.email = email
        self.master_token = ''
        self.keep = gkeepapi.Keep()

    def generate_master_token(self, oauth_token):
        """Generate a master token using a oauth token.
        Returns a master token, else none."""
        android_id = '0123456789abcdef' # Generic id, not critical to token generation
        master_response = gpsoauth.exchange_token(email=self.email, token=oauth_token, android_id=android_id)
    
        if 'Token' in master_response:
            master_token = master_response['Token']
            return master_token
        else:
            print('A master token could not be generated.')
            sys.exit(1)

    def login(self):
        """Access your Google Keep Account."""
        try:
            self.keep.authenticate(self.email, self.master_token)
            print('Login successful')
        except LoginException:
            print('Failure to login')
            sys.exit(1)

    def create_list(self):
        """Create a new list in Google Keep."""
        list_title = "Test List"
        list_items = [
            ('Test Item 1', False),
            ('Penis Item 2', True),
            ('Why did Item 2 say Penis?', True)
        ]

        self.keep.createList(list_title, list_items)
        self.keep.sync()  # Push changes to Google Keep
        # If changes are not reflected on Google Keep, ensure that you are syncing changes
        print('A test note has been added to your Google Keep.')

    def read_list(self):
        """Read the items of a list."""
        test_list = self.keep.find(query='Test List')
        print('The following items are in your test list:')
        for item in test_list:
            print(item)