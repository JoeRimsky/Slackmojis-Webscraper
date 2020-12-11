#!/usr/bin/python3
import requests
import os
import sys
import getopt

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = r'E:\\Chromedriver\\chromedriver.exe'
GIFS_DIR = os.path.dirname(os.path.realpath(__file__)) + '\\GIFs\\'
USAGE = f'Usage: python {sys.argv[0]} [--help] | [-d <destination_path>]'

class Webscraper():
    def __init__(self, destination):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
        self.destination = destination
    
    def start(self, links):
        def scrape():
            for element in gif_elements:
                url = element.get_attribute('src')
                name = element.get_attribute('alt')

                response = requests.get(url=url)

                filename = name.replace(" ", "_") + '.gif'
                with open((self.destination+filename), 'wb') as gif_out:
                    gif_out.write(response.content)

        if not os.path.exists(self.destination):
            os.makedirs(self.destination)

        if links:
            self.driver.get(links.pop(0))

            gif_elements = self.driver.find_elements_by_css_selector('img[loading="lazy"]')

            if gif_elements:
                scrape()
            elif links:
                self.start(links)

    def end(self):
        self.driver.quit()

def parse_args():
    options, arguments = getopt.getopt(sys.argv[1:], 'hd:', ["help", "destination="])
    destination = GIFS_DIR
    for opt, arg in options:
        if opt in ("-h", "--help"):
            print(USAGE)
            sys.exit()
        if opt in ("-d", "--destination"):
            destination = arg
            
    return destination

def main():
    dest_folder = parse_args()
    scraper = Webscraper(dest_folder)
    see_more_elements = scraper.driver.find_elements_by_class_name('seemore')
    links = ['https://slackmojis.com/',]
    for element in see_more_elements:
        links.append(element.get_attribute('href'))
    scraper.start(links)
    scraper.end()

if __name__ == '__main__':
    main()