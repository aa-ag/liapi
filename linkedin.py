############------------ IMPORTS ------------############
import requests
import settings

############------------ GLOBAL VARIABLE(S) ------------############

           
############------------ FUNCTION(S) ------------############
def get_user_info():
    '''
     hit endpoint and retreive user info
    '''
    response = requests.get('https://api.linkedin.com/v2/me')

    print(response.status_code)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    get_user_info()
