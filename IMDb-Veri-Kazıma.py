from bs4 import BeautifulSoup
import requests

link="https://www.imdb.com/chart/top/"

baglan=requests.get(link) #siteye talepte bulunduk

#json alanı almayacagımız ıcın content akanı kuruyoruz

#kodları alacagımız yapı:
kod=baglan.content #baglan üzerinden gelen degerleri çek, koda aktar dedik

parser=BeautifulSoup(kod,"html.parser") #html kodlarını parser edip parser degıskenıne atadık

#kodların tamamını tbody etıketınden alacagı ıcın:
tbody=parser.find("tbody",{"class":"lister-list"}) #tbody alanlarının tamamının icinden classı lister-list olanları cektık

#şimdi tbody ıcındeki tr alanlarına ulasmamız lazım:
tr=tbody.find_all("tr")


#şimdi tr ıcındeki td alanlarına ulasmamız lazım, td alanları ıcındende classı titleColumn olan bilgilere ulasmamız lazım
counter=1
for i in tr:
    td=i.find("td",{"class":"titleColumn"}).find("a").string #ulastıktan sonra titleColumnların ıcındeki a yapısı ıcınde bulunan string degerı yanı fılm ısımlerını aldık ve td degıskenıne attık
    tarih=i.find("td",{"class":"titleColumn"}).find("span",{"class":"secondaryInfo"}).string  #filmlerin yanına tarih ekleyip,başına da numarasını yazdırmak ıcın
    print(str(counter)+". "+td+" "+tarih)
    counter+=1
    

