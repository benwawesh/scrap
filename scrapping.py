import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url ="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"
uclient=uReq(my_url)
page_html= uclient.read()
uclient.close()
page_soup=soup(page_html, "html.parser")
print(page_soup.h1)
containers=page_soup.findAll('div',{"class":"item-container"})
print(len(containers))
prcontainers[0])