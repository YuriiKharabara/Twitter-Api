import requests
import hidden
def get_info(url):

    authorization = {"Authorization": "Bearer " + hidden.oauth()['token_secret']}
    response=requests.get(url, headers=authorization)
    return response.json()
    
def main():
    user_name=input('Please, print username, wh you want to know about: ')
    url_for_id=f'https://api.twitter.com/2/users/by/username/{user_name}'
    id=get_info(url_for_id)['data']['id']
    print(get_info(f'https://api.twitter.com/2/users/{id}/following'))