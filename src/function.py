"""function.py: functions File."""
__author__ = "Muhammad Usman Naeem"
__license__ = "GPL-3"
__version__ = "1.0.0"
__administrator__ = "Muhammad Usman Naeem"
__developers__ = "Muhammad Usman Naeem"
__email__ = "usman.naeem2212@gmail.com"
__status__ = "Production"

import requests
from datetime import date
from bs4 import BeautifulSoup

class Map:

    @staticmethod
    def conn():
        '''
        Establishes Connection with class
        Args:
            None
        Returns:
            class
        Raises:
            None.
        '''
        return Map

    @staticmethod
    def today_date():
        '''
        Returns Today's Date
        Args:
            None
        Returns:
            current Date
        Raises:
            None.
        '''

        Date = str(date.today().strftime("%Y-%m-%d"))
        return Date

    @staticmethod
    def get_html(url) :
        '''
        Gets Html from a webpage
        Args:
            url: url of the page to be opened
        Returns:
            BeautifulSoup version of html parsed from webpage
        Raises:
            None.
        '''
        html = requests.get(url)
        soup = BeautifulSoup(html.content, "lxml")
        return soup

    @staticmethod
    def get_links(html) :
        '''
        Gets links from tab in html
        Args:
            html: html of the webpage
        Returns:
            list: list of links (ignores links of images)
        Raises:
            None.
        '''
        urls = []
        links = html.find_all('link')
        for link in links :
            url = link.get('href')
            if url.endswith("/") :
                if url.endswith("png/") or url.endswith("ico/") or url.endswith("jpg/") :
                    continue
                else : urls.append(url)
            else :
                if url.endswith("png") or url.endswith("ico") or url.endswith("jpg") :
                    continue
                else : urls.append(url + "/")
        return urls

    @staticmethod
    def get_image_links(html) :
        '''
        Gets links of images from tab in html
        Args:
            html: html of the webpage
        Returns:
            list: list of links of images
        Raises:
            None.
        '''
        image_urls = []
        links = html.find_all('link')
        for link in links :
            url = link.get('href')
            if url.endswith("/") :
                if url.endswith("png/") or url.endswith("ico/") or url.endswith("jpg/") :
                    image_urls.append(url)
            else :
                if url.endswith("png") or url.endswith("ico") or url.endswith("jpg") :
                    image_urls.append(url + "/")
        return image_urls

    @staticmethod
    def get_xml(req_url, urls, image_urls, date) :
        xml = '''<?xml version='1.0' encoding='UTF-8'?>
        <urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>
        '''

        for i in range(len(urls)) :
            xml += "\n  <url>\n    <loc>" + str(urls[i]) + "</loc>\n    <lastmod>" + date + "</lastmod>\n  </url>"

        xml += "\n  <url>\n    <loc>" + req_url + "</loc>"
        for i in range(len(image_urls)) :
            xml += "\n    <image:image>\n      <image:loc>" + str(image_urls[i]) + "</image:loc>\n    </image:image>"

        xml += "\n  </url>\n</urlset>"
        return xml
