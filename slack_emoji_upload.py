#!/usr/bin/python3
import requests

from time import sleep

class Slack():
    def __init__(self, workspace, token):
        self.domain = f'{workspace}.slack.com'
        self.base_url = f'https://{self.domain}'
        self.token = token

    def upload_emoji(self, name, image):
        api_add_url = f'{self.base_url}/api/emoji.add'

        body = {
            'token': self.token,
            'mode': 'data',
            'name': name,
        }

        req = requests.post(url=api_add_url, data=body, files=image)
        resp = req.json()

        if req.status_code == 429:
            print('Error code 429: Too many requests. Sleeping for 4 seconds.')
            sleep(4)
            self.upload_emoji(name, image)
        
        if resp["ok"]:
            print(f'Successful upload: {name}')
        else:
            print(f'Failed upload: {name} Error: {resp["error"]}')

    def get_current_list(self):
        api_list_url = f'{self.base_url}/api/emoji.list'
        page = 1
        emoji_list = []

        body = {
            'query': '',
            'page': page,
            'count': 1000,
            'token': self.token
        }
        
        req = requests.post(api_list_url, data=body)
        req.raise_for_status()
        response_json = req.json()
        emoji_list.extend(response_json["emoji"])

        return emoji_list

    def remove_emoji(self, name):
        api_remove_url = f'{self.base_url}/api/emoji.remove'

        body = {
            'token': self.token,
            'name': name
        }

        req = requests.post(url=api_remove_url, data=body)

        if req.status_code == 429:
            sleep(4)
            self.remove_emoji(name)