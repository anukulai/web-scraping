from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import xlwt 
from xlwt import Workbook 
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')





url ='https://m.cartrade.com/'

const_c = uReq(url)

pager = const_c.read()
 
const_c.close()
  
page_soup = soup(pager, "html.parser")
  
container = page_soup.findAll("div", {"class":"siwper-inner"})

filename = "cartrade.csv"
f = open(filename, "w")

header="brand, link\n"

f.write(header)

brand1=[]
link1=[]
for contain in container:
	brand= contain.div.a["title"]
	
	contain_new= contain.findAll("div",{"class":"slid_block"})
	con= contain_new[0].ul.li.strong.a["href"]
	brand1.append(brand)
	link1.append(con)
	print("brand: " + brand)
	print("link: " + con)
#print(link1)
#print(brand1)
for i in range(0,len(link1)):
  sheet1.write(i,0,brand1[i]) 
  sheet1.write(i,1,link1[i])
  wb.save(r'C:\Users\dell\Desktop\example2.xls')	
  
print(len(link1))
print(len(brand1))