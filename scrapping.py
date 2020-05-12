import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import  requests
my_url ="https://www.tenders.go.ke/website/tenders/Index"
uclient=requests.get(my_url)
page_soup=soup(uclient.text, "html.parser")
print(page_soup.table)
tender_table=page_soup.findAll('tbody',{'class':'odd'})
print(tender_table)


# response=requests.get(my_url)
# soup= soup(response.text, 'html.parser')
# print(soup.table)
# tender_table = soup.find('table', {"class":"table table--football table--league-table table--responsive-font table--striped"}).tbody
# print(tender_table)
# for tender in tender_table.find_all('tbody'):
#     rows=tender.find_all('tr')
#     for row in rows:
#         tender_objects = row.find('td', class_="sorting_1")
#         print(tender_objects)