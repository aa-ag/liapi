############------------ IMPORTS ------------############
import requests
from requests.api import head
import settings

############------------ GLOBAL VARIABLE(S) ------------############
authorization_code = settings.authorization_code

headers = {'Content-Type': 'application/json',
           'X-Restli-Protocol-Version': '2.0.0',
           'Authorization': f'Bearer {authorization_code}'}
           
           
############------------ FUNCTION(S) ------------############
def get_user_info():
    '''
     hit endpoint and retreive user info
    '''
    response = requests.get('https://api.linkedin.com/v2/me', headers=headers)

    print(response.status_code)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    get_user_info()
