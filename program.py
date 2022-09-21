from bs4 import BeautifulSoup
import codecs
import requests

#url = "http://www.dodear.com//en/movie"
#response = requests.get(url)
#htmlcontent = response.content

file = codecs.open("dodear-portal.html", "r", "utf-8")
htmlcontent = file.read()

soup = BeautifulSoup(htmlcontent, 'html.parser')
#print(soup.prettify())

filename = "result.csv"
f= open(filename, "w")
headers="Movie Title, Image Link, Views, Downloads, Release Date\n"
f.write(headers)

for d in soup.find_all('div', attrs={'class':'list-box col-xs-4 col-sm-3 col-md-3 col-lg-2'}):
 
 title = d.find('a', attrs={'class':'list-anc'})
 titlea = title.string
 #print(titlea)
 
 image = d.find('img', attrs={'class':'ar-img check-img'})
 imagesrc = image.get('src')
 #print(imagesrc)
 
 v = d.find('div', attrs={'class':'list-meta-right'})
 view = v.find('div', attrs={'class':'list-meta-item'})
 viewcount = view.text.split()[0]
 #print(viewcount)
 
 v = d.find('div', attrs={'class':'list-meta-right'})
 ds = v.text.split("Views")[1]
 downloads = ds.split("Download")[0]
 #print(downloads)
 
 r = d.find('div', attrs={'class':'list-meta-left'})
 RD = r.text.split("PD")[1]
 date = RD.split("RD")[1]
 #print(date)
 
 print(titlea + "," + imagesrc + "," + viewcount.replace(",","") + ","+ date.replace(",","")+"\n")
 
 
 
 
 f.write(titlea.replace(",","") + "," + imagesrc + "," + viewcount.replace(",","") + "," + downloads.replace(",","") + ","+ date.replace(",","")+"\n")

f.close()