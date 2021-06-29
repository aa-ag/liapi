############------------ IMPORTS ------------############
import requests
import secrets
import settings


############------------ FUNCTION(S) ------------############
def generate_authorization_url():
    url = f'https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={settings.client_id}&redirect_uri={settings.linkedin_redirect}&state={secrets.token_hex(8).upper()}&scope=r_liteprofile%20r_emailaddress%20w_member_social'
    print(url)

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    generate_authorization_url()
