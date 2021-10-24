import requests
from bs4 import BeautifulSoup

def tshirts(page):
    url=f'https://www.flipkart.com/mens-tshirts/pr?sid=clo,ash,ank,edy&fm=neo%2Fmerchandising&iid=M_d8bce6d9-577a-4e06-b827-a617c5bfc970_1_372UD5BXDFYS_MC.IF56C41VGEYS&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Fashion~Men%2527s%2BTop%2BWear~Men%2527s%2BT-Shirts_IF56C41VGEYS&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&cid=IF56C41VGEYS=(page)'

    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')

    return soup

def extract(soup):
    divs=soup.finf_all('div', class_ = 'IIdQZO')

    for items in divs:
        title = items.find('a',class_='2myIT6').text
        print(title)

        company=items.find('a',class_='_2B_pmu').text

        try:
            pack_of=items.find('a',class_='zU9Df8').text

        except
            pack_of=''
            print(pack_of)

        
    return


c=tshirts(1)
extract(c)
