import requests
import re

# Constants
menu_pattern = re.compile('class="gdtm".*?href="(.*?)"')


def getMenu(page_url, headers, page) -> str:
    if page != 0:
        page_url += "?p={}".format(page)
    response = requests.get(page_url, headers=headers).text
    return response
