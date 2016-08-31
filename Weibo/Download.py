from urllib import request
import time

class Downloader(object):
    def __init__(self):
        self.header = {
				"Connection":"keep-alive",
				"Cookie":"自己加",
				"Host":"weibo.com",
				# "Referer":"http://weibo.com/u/2349336003?from=usercardnew&refer_flag=0000020001_&is_all=1",
				"Upgrade-Insecure-Requests":"1",
				"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36"
				}  

    def geturl(self, url):
        print("\ndownload url%s......\n"%url)
        if url is None:
            return None
        res = request.Request(url, headers = self.header)
        response = request.urlopen(res)
        if response.getcode() != 200:
            return None
        time.sleep(1)

        return response.read().decode("utf-8")
		
