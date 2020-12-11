#!/usr/bin/python3

# Currently working on building out
# Will condense into single execution

import requests
import sys
import getopt

from time import sleep

USAGE = f'Usage: python {sys.argv[0]} [--help] | [-w <workspace>] & [-t <token>]'

class Slack():
    def __init__(self, workspace, token):
        self.domain = f'{workspace}.slack.com'
        self.baseURL = f'https://{self.domain}'
        self.token = token

    def upload_emoji(self, name, image):
        apiURL = f'{self.baseURL}/api/emoji.add'
        body = {
            'token': self.token,
            'mode': 'data',
            'name': name,
            'image': image
        }

        req = requests.post(url=apiURL, data=body)

        if req.status_code == 429:
            # Handle rate limiting
            sleep(4)

def parse_args():
    workspace = ""
    token = ""
    options, arguments = getopt.getopt(sys.argv[1:], 'hwt:', ["help", "workspace=", "token="])
    for opt, arg in options:
        if opt in ("-h", "--help"):
            print(USAGE)
            sys.exit()
        if opt in ("-w", "workspace="):
            workspace = arg
        if opt in ("-t", "token="):
            token = arg
        if not opt in ("-w", "workspace=", "-t", "token="):
            print(USAGE)
            sys.exit()
            
    return workspace, token

def main():
    workspace, token = parse_args()
    slack_connect = Slack(workspace=workspace, token=token)

if __name__ == '__main__':
    main()