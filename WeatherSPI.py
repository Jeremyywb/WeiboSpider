
import urllib
from urllib import request
from  urllib.request import urlopen
from bs4 import BeautifulSoup
import time

#return object to insert into database 

class Craw_wea(object):
    def __init__(self):
        self.areas = [
            ("广州",101280101),
            ("深圳",101280601),
            ("厦门",101230201),
            ("福州",101230101),
            ("南宁",101300101),
            ("柳州",101300301),
            ("海口",101310101),
            ("三亚",101310201)
            ]

    @staticmethod
    def makeurl(ids):
        return "http://www.weather.com.cn/weather/"+str(ids)+".shtml"
    @staticmethod
    def make_soup(url):
        res = request.Request(url)
        response = request.urlopen(res)
        decoderes = response.read().decode("utf-8")
        return BeautifulSoup(decoderes, "html.parser")
    @staticmethod
    def reshpe_wea(strs):
        rep_slah = strs.replace("\n")
        mid_proc = rep_slah.split("/")
        return "~".join(mid_proc)
    @staticmethod
    def get_data(soupOBJ, tag, classname):
        return soupOBJ.find(tag = tag,class_ =classname ).extract().get_text()

    def Main(self):
        Outvar = []
        currDate = time.strftime("%m-%d", time.localtime(time.time()))
        for city, codes in self.areas:
            url = Craw_wea.makeurl(codes)
            soup = Craw_wea.make_soup(url)
            weather = soup.find(tag ="p",class_ ="wea" ).extract().get_text()
            # weather = Craw_wea.get_data(soup, tag="p", classname="wea")
            print("\n\n\n\n-------------------------weather\n\n\n\n",weather,"\n\n\n\n")
            templtu = Craw_wea.get_data(soup, tag="p", classname="tem")
            print("\n\n\n\n-------------------------templtu\n\n\n\n",templtu,"\n\n\n\n")
            retempl = Craw_wea.reshpe_wea(templtu)
            print("\n\n\n\n-------------------------retempl\n\n\n\n",retempl,"\n\n\n\n")
            Outvar.append(tuple([currDate,city,retempl, weather]))
        return Outvar

if __name__ == '__main__':
    g = Craw_wea()
    k = g.Main()
    print(k)




