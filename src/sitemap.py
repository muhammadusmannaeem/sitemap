"""sitemap.py: functions File."""
__author__ = "Muhammad Usman Naeem"
__license__ = "GPL-3"
__version__ = "1.0.0"
__administrator__ = "Muhammad Usman Naeem"
__developers__ = "Muhammad Usman Naeem"
__email__ = "usman.naeem2212@gmail.com"
__status__ = "Production"

from src.parser import Parser
import re

class sitemap(Parser):

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
        return sitemap

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
        html = sitemap.get_html(url)
        if what == "url" :
            urls = sitemap.get_links(html)
            xml = "<?xml version='1.0' encoding='UTF-8'?><urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>"
            for i in range(len(urls)) :
                xml += "<url><loc>" + url + str(urls[i]) + "</loc><lastmod>" + sitemap.today_date() + "</lastmod></url>"
            xml += "</urlset>"
            return xml
        elif what == "image" :
            urls = sitemap.get_image_links(html)
            xml = "<?xml version='1.0' encoding='UTF-8'?><urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'><url>"
            for i in range(len(urls)) :
                xml += "<image:image><image:loc>" + url + str(urls[i]) + "</image:loc></image:image>"
            xml += "</url></urlset>"
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
        html = sitemap.get_html(url)
        urls = sitemap.get_image_links(html)
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

    @staticmethod
    def validate(x, type) :
        '''
        validates xml
        Args:
            xml: xml
        Returns:
            Type of Error (If Any)
        Raises:
            None.
        '''
        xml = str(x)
        if type == "url" :
            if re.search("^<.*xml version='.+' encoding='UTF-8'", xml) :
                if re.search(".+<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/...'>", xml) :
                    w = xml.split("<urlset")
                    if not w[1].endswith("</urlset>") : return "Error in </urlset> end tag"
                    w = w[1]
                    x = w[:(len(w)-9)].split("<url>")
                    y = []
                    for value in x :
                        if value == x[0] : continue
                        if value.endswith("</url>"):
                            y.append(value[:(len(value)-6)])
                        else : return "missing </url> end tag"
                    for value in y :
                        x = value.split("</loc>")
                        if not x[0].startswith("<loc>") : return "Error in </loc> end tag"
                        x = value.split("<lastmod>")
                        if not x[1].endswith("</lastmod>") : return "Error in </lastmod> end tag"
                else : return "Error in <urlset...> tag"
            else : return "Error in <?xml...> tag"
            return "Validated xml Successfully. No Errors"
        elif type == "image" :
            if re.search("^<.*xml version='.+' encoding='UTF-8'", xml) :
                if re.search(".+<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/...'>", xml) :
                    w = xml.split("<urlset")
                    if w[1].endswith("</urlset>") :
                        w = w[1]
                    else : return "Error in </urlset> end tag"
                    x = w[:(len(w)-9)].split("<url>")
                    if x[1].endswith("</url>") :
                        y = x[1][:(len(x[1])-6)].split("<image:image>")
                    else : return "Error in </url> end tag"
                    z = []
                    for value in y :
                        if value == y[0] : continue
                        if value.endswith("</image:image>") :
                            z.append(value[:(len(value)-14)])
                        else : return "Error in </image:image> end tag"
                    for value in z :
                        x = value.split("<image:loc>")
                        for a in x :
                            if a == x[0] : continue
                            if not a.endswith("</image:loc>") : return "Error in </image:loc> end tag"
                else : return "Error in <urlset...> tag"
            else : return "Error in <?xml...> tag"
            return "Validated xml Successfully. No Errors"

    @staticmethod
    def sitemap_submitter() :
        '''
        Submits sitemap to google
        Args:
            xml: xml
        Returns:
            Type of Error (If Any)
        Raises:
            None.

        Put url : PUT https://www.googleapis.com/webmasters/v3/sites/siteUrl/sitemaps/feedpath
        code : (Copied from StackOverflow) Below
        '''
        pass
        # ToDo
        '''
        CLIENT_ID = 'xxxxx'
        CLIENT_SECRET = 'yyyyyy'

        OAUTH_SCOPE = 'https://www.googleapis.com/auth/webmasters'

        # Redirect URI for installed apps
        REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

        # Run through the OAuth flow and retrieve credentials
        flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
        authorize_url = flow.step1_get_authorize_url()
        print ('Go to the following link in your browser: ' + authorize_url)
        code = input('Enter verification code: ').strip()
        credentials = flow.step2_exchange(code)

        # Create an httplib2.Http object and authorize it with our credentials
        http = httplib2.Http()
        http = credentials.authorize(http)

        webmasters_service = build('webmasters', 'v3', http=http)

        WEBSITE = 'http://www.mywebsite.com'
        SITEMAP_PATH = 'http://www.mywebsite.com/sitemaps/'
        SITEMAPS_LIST = ['sitemap1.xml','sitemap2.xml','sitemap3.xml']

        print ('Adding sitemaps to website ' + WEBSITE)
        for sitemap in SITEMAPS_LIST:
            print ('  '+SITEMAP_PATH + sitemap)
            webmasters_service.sitemaps().submit(siteUrl=WEBSITE, feedpath=SITEMAP_PATH + sitemap)   # .execute()        # If error comes
        '''
