############------------ IMPORTS ------------############
### Python
import requests
import secrets
from requests.api import post
### Project-specific
import settings


############------------ FUNCTION(S) ------------############
def generate_authorization_url():
    '''
     prepare each element of the url necessary to
     retreive authorization code according to
     documentation: https://tinyurl.com/5umjmm42
    '''
    i = 'https://www.linkedin.com/oauth/v2/authorization?'
    ii = 'response_type=code&'
    iii = f'client_id={settings.client_id}&'
    iv = f'redirect_uri={settings.linkedin_redirect}&'
    v = f'state={secrets.token_hex(8).upper()}&'
    vi = 'scope=r_liteprofile%20r_emailaddress%20w_member_social'
    print(i + ii + iii + iv + v + vi)


def retreive_access_token():
    '''
     uses authorization url generated in previous function
     to hit accessToken endpoint and generate, well, you guessed it: 
     an accessToken
    '''
    access_token_endpoint = 'https://www.linkedin.com/oauth/v2/accessToken?'
    i = 'grant_type=authorization_code&'
    ii = f'code={settings.authorization_code}&'
    iii = f'redirect_uri={settings.linkedin_redirect}&'
    iv = f'client_id={settings.client_id}&'
    v = f'client_secret={settings.client_secret}'

    url = access_token_endpoint + i + ii + iii + iv + v

    access_token = requests.post(url).json()

    return access_token['access_token']


def retreive_user_info():
    '''
     uses access_token retreived in 
     retreive_access_token() to retreive
     user info
    '''
    linkedin_user_profile_endpoint = 'https://api.linkedin.com/v2/me'

    request = requests.get(linkedin_user_profile_endpoint, headers={
        'Authorization': f'Bearer {settings.access_token}'})
    
    return request.json()


def post_on_linkedin():
    '''
     sets (i) endpoint that needs to be hit to post text
     (ii) sets json object with content necessary to post text
     per documentation, (iii) sets post request with required 
     headers, (iv) checks if connection is made successfully 
     and if so, posts to feed
    '''
    endpoint_to_post_text_on_linkedin = 'https://api.linkedin.com/v2/ugcPosts'

    to_be_posted = {
    "author": f"urn:li:person:{settings.user_id}",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "testing linkedin's api: a Roman soldier walks into a bar, sticks two fingers up and says, \"five beers please.\""
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    request = requests.post(endpoint_to_post_text_on_linkedin, headers={
        'Authorization': f'Bearer {settings.access_token}',
        'X-Restli-Protocol-Version': '2.0.0'}, json=to_be_posted)
    
    if request.status_code == 201:
        print("Posted.")
        print(request.content)
    else:
        print(request.content)
    
    

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    # generate_authorization_url()

    # print(retreive_access_token())

    # print(retreive_user_info())

    post_on_linkedin()
