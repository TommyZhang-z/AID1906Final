from getMenu import *
from getPic import *
from multiprocessing import Pool

# Constants
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}

page_url = "https://e-hentai.org/g/1916815/00af533068/"

save_directory = "zwt_img/"

total_page = 1

process_amount = 10


# Functions
def main() -> None:
    pool = Pool(process_amount)
    for page in range(0, total_page):
        menu = getMenu(page_url, headers, page)
        links = re.findall(menu_pattern, menu)
        c = MyRequest(links, headers, save_directory, page)
        pool.map(c.main, range(len(links)))