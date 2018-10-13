from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import xlwt 
from xlwt import Workbook 
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')

my_url ='https://www.fossil.com/us/en/women/watches/view-all.html'

uClient = uReq(my_url)

page_html = uClient.read()
 
uClient.close()
  
page_soup = soup(page_html, "html.parser")
  
container = page_soup.findAll("article", {"class":"product-result col-xs-6 col-sm-4 col-md-3"})

brand1=[]
image1=[]

for contain in container:
			brand=contain.div.div.a["href"]
			image=contain.div.div.a.img["alt"]
			brand1.append(brand)
			image1.append(image)
			print("brand: " + brand)
			print("image: " + image)
	
for i in range(0,len(image1)):
           sheet1.write(i,0,brand1[i]) 
           sheet1.write(i,1,image1[i])
           wb.save(r'C:\Users\dell\Desktop\newegg6.xls')