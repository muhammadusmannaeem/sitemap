"""index.py: Main File."""
__author__ = "Muhammad Usman Naeem"
__license__ = "GPL-3"
__version__ = "1.0.0"
__administrator__ = "Muhammad Usman Naeem"
__developers__ = "Muhammad Usman Naeem"
__email__ = "usman.naeem2212@gmail.com"
__status__ = "Production"

from src.function import Map

m = Map()
conn = m.conn()

req_url = "https://www.muhammadumerfarooq.me"
soup = conn.get_html(req_url)
urls = conn.get_links(soup)
image_urls = conn.get_image_links(soup)
xml = conn.get_xml(req_url, urls, image_urls, conn.today_date())

print(xml)
quit()

with open('sitemap.xml', 'w') as file:
    file.write(xml)
