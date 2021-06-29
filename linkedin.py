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

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    generate_authorization_url()
