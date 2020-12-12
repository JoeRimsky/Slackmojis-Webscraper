#!/usr/bin/python3
import argparse
import os
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import rmtree
from slack_emoji_upload import Slack
from urllib.parse import urlparse

class Webscraper():
    def __init__(self, chromedriver_path):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        self.destination = os.path.dirname(os.path.realpath(__file__)) + '\\GIFs\\'
        self.current_emojis = []
    
    def start(self, links, slack):
        def scrape():
            for element in gif_elements:
                url = element.get_attribute('src')

                response = requests.get(url=url)
                full_path = urlparse(url)
                base_path = os.path.basename(full_path.path)
                emoji_name = os.path.splitext(base_path)[0]

                if emoji_name not in self.current_emojis:
                    with open((self.destination+emoji_name+'.gif'), 'wb') as gif_out:
                        gif_out.write(response.content)

                    with open((self.destination+emoji_name+'.gif'), 'rb') as gif_up:
                        image = {'image': gif_up}
                        slack.upload_emoji(name=emoji_name, image=image)

        if not os.path.exists(self.destination):
            os.makedirs(self.destination)

        if links:
            self.driver.get(links.pop(0))

            gif_elements = self.driver.find_elements_by_css_selector('img[loading="lazy"]')

            if gif_elements:
                scrape()
            elif links:
                self.start(links, slack)

    # Can be used to remove emojis
    # Currently set to remove all current workspace emojis
    def remove_emojis(self, slack):
        for emoji in self.current_emojis:
            slack.remove_emoji(emoji)

    def cleanup(self):
        self.driver.quit()
        rmtree(self.destination)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest='driver_path', help='Path to chromedriver.exe', required=True)
    parser.add_argument('-w', dest='workspace', help='Slack workspace/team', required=True)
    parser.add_argument('-t', dest='token', help='Slack token', required=True)

    args = parser.parse_args()

    return args.driver_path, args.workspace, args.token

def main():
    chromedriver_path, workspace, token = parse_args()
    scraper = Webscraper(chromedriver_path)
    slack = Slack(workspace=workspace, token=token)
    scraper.current_emojis = slack.get_current_list()
    see_more_elements = scraper.driver.find_elements_by_class_name('seemore')
    links = ['https://slackmojis.com/',]
    for element in see_more_elements:
        links.append(element.get_attribute('href'))
    scraper.start(links, slack)
    scraper.cleanup()

if __name__ == '__main__':
    main()