############------------ IMPORTS ------------############
import requests
import secrets
import settings


############------------ FUNCTION(S) ------------############
def generate_authorization_url():
    '''
     prepare each element of the url necessary to
     retreive authorization code according to
     documentation: https://tinyurl.com/5umjmm42
    '''
    a = 'https://www.linkedin.com/oauth/v2/authorization?'
    b = 'response_type=code&'
    c = f'client_id={settings.client_id}&'
    d = f'redirect_uri={settings.linkedin_redirect}&'
    e = f'state={secrets.token_hex(8).upper()}&'
    f = 'scope=r_liteprofile%20r_emailaddress%20w_member_social'
    print(a + b + c + d + e + f)


def retreive_access_token():
    access_token_endpoint = 'https://www.linkedin.com/oauth/v2/accessToken?'
    a = 'grant_type=authorization_code&'
    b = f'code={settings.authorization_code}&'
    c = f'redirect_uri={settings.linkedin_redirect}&'
    d = f'client_id={settings.client_id}&'
    e = f'client_secret={settings.client_secret}'

    url = access_token_endpoint + a + b + c + d + e

    access_token = requests.post(url).json()

    return access_token





############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    # generate_authorization_url()

    print(retreive_access_token())
