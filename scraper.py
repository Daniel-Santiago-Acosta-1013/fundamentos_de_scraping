import requests
import lxml.html as html


HOME_URL = 'https://www.larepublica.co/'

XPATH_LINK_TO_ATICLE = '//h2/a/@href'
XPATH_TITLE = '//h2[@class=""]/span/text()'
XPATH_SUMMARY = '//div[@class = "lead"]/p/text()'
XPATH_BODY = '//div[@class = "html-content"]/p[not (@class)]/text()'

def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)

            links_to_notices = parsed.xpath(XPATH_LINK_TO_ATICLE)
            print(len(links_to_notices))
            print(links_to_notices)
        else:
            raise valueError(f"Error:{response.status_code}")
    except valueError as ve:
        print(ve)

def main():
    parse_home()

if __name__ =='__main__':
    main()
