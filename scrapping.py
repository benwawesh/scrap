import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url ="https://www.tenders.go.ke/website/tenders/Index"
uclient=uReq(my_url)
page_html= uclient.read()
uclient.close()
page_soup=soup(page_html, "html.parser")
print(page_soup.table)
containers=page_soup.findAll('div',{"class":"item-container"})
print(len(containers))
