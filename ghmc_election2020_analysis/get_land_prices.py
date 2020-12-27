import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

url_template = "https://www.makaan.com/price-trends/property-rates-for-buy-in-hyderabad?page={page_no}"
dfs = pd.DataFrame()

for i in range(61):

    the_url = url_template.format(page_no=i+1)
    url_object = urllib.request.urlopen(the_url)
    file_contents = url_object.read().decode("utf-8")
    # soup = BeautifulSoup(file_contents, 'html.parser')

    # table = soup.find_all('table').find_all('tr')

    dfs = dfs.append(pd.read_html(file_contents))
    sleep(2)
    print(i)

dfs.to_csv('land_prices.csv')
