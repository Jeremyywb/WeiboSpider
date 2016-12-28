
import os
from bs4 import BeautifulSoup

class HTMLEXAX(object):
    def __init__(self):
        self.path = "D:/MYCODES"

	@staticmethod
	def has_class(obj):
        try:
		   print(obj['class'])
		   return True
        except:
		   return False

    def mian(self):
    	os.chdir("./DATA")
        files = os.lisdir()
        for filename in files:
            htmlfile = open(filename, 'r',encoding="utf-8")
            htmlpage = htmlfile.read()
            soup = BeautifulSoup(htmlpage, 'html.parser', from_encoding='utf-8')
            table_obj = soup.find_all('table', class_="grace-grid-body")
            table_head = table_obj[0].find("thead").find_all("td")
            table_head = [x.extract().get_text()  for  x  in  table_head]
            table_body = table_obj[0].find("tbody").find_all("tr")
            coll_tb = []
            for trdata in table_body:
            if has_class(trdata):
                each_row = [tdf.extract().get_text()  for  tdf  in  trdata.find_all("td")]
                print(each_row)
                trfirst = each_row[0]
                print("----first-----",trfirst)
            else:
                print("doing else......")
                each_row = [trfirst] + [tdf.extract().get_text()  for  tdf  in  trdata.find_all("td")]
            coll_tb.append(tuple(each_row))
            print(coll_tb)
            import csv
            csvname = filename + ".csv"
            with open(csvname, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(coll_tb)
