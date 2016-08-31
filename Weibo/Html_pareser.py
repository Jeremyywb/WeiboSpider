from bs4 import BeautifulSoup
import re

class HtmlPare(object):
    def getfenlist(self, data):
        souprep = BeautifulSoup(data,"html.parser")
        print("find fans elements.....")
        getnodes = re.findall(r"<script>+.*</script>+",str(souprep),re.I|re.M)
        for item in getnodes:
            if re.match(r'.*粉丝列表.*', str(item)):
                return item

	
        
            


