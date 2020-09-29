"""sitemap.py: functions File."""
__author__ = "Muhammad Usman Naeem"
__license__ = "GPL-3"
__version__ = "1.0.0"
__administrator__ = "Muhammad Usman Naeem"
__developers__ = "Muhammad Usman Naeem"
__email__ = "usman.naeem2212@gmail.com"
__status__ = "Production"

from src.parser import Parser
p = Parser()
con = p.conn()

class SiteMap:

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
        return SiteMap

    @staticmethod
    def get_xml(url, what) :
        '''
        Generates xml of the links from html of the url
        Args:
            url: url of the webpage
            what: get xml of images, or xml of urls
        Returns:
            xml: xml Generated
        Raises:
            None.
        '''
        html = con.get_html(url)
        if what == "url" :
            urls = con.get_links(html)
            xml = '''<?xml version='1.0' encoding='UTF-8'?>\n<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>
            '''
            for i in range(len(urls)) :
                xml += "\n  <url>\n    <loc>" + url + str(urls[i]) + "</loc>\n    <lastmod>" + con.today_date() + "</lastmod>\n  </url>"
            xml += "\n</urlset>"
            return xml
        elif what == "image" :
            urls = con.get_image_links(html)
            xml = '''<?xml version='1.0' encoding='UTF-8'?>\n<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>\n  <url>
            '''
            for i in range(len(urls)) :
                xml += "\n    <image:image>\n      <image:loc>" + url + str(urls[i]) + "</image:loc>\n    </image:image>"
            xml += "\n  </url>\n<urlset>"
            return xml

    @staticmethod
    def is_image(url) :
        '''
        Checks if there are any images in the webpage
        Args:
            url: url of the webpage
        Returns:
            Bool: True/False
        Raises:
            None.
        '''
        html = con.get_html(url)
        urls = con.get_image_links(html)
        if len(urls) == 0 :
            return False
        else : return True

    @staticmethod
    def write_on_file(xml, name) :
        '''
        Writes xml on file
        Args:
            xml: xml to be written
            name: name of file to be written on
        Returns:
            None
        Raises:
            None.
        '''
        with open(name, 'w') as file:
            file.write(xml)
