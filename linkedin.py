############------------ IMPORTS ------------############
import requests
from requests.api import head
import settings

############------------ GLOBAL VARIABLE(S) ------------############
authorization_code = settings.authorization_code
           

############------------ FUNCTION(S) ------------############
def get_user_info():
    '''
     hit endpoint and retreive user info
    '''
    response = requests.get(f'https://api.linkedin.com/v2/me?oauth2_access_token={authorization_code}')

    print(response.status_code)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    get_user_info()
