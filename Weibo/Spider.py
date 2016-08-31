import Download,FeeDExport,Html_pareser,Pipeline,URLSchedul
import sys 
sys.path.append('E:/ProjectCT/Kaggle/Weibo/Spider.py') 



class SpiderMain(object):
    def __init__(self):
        self.UrlAndIDContr = URLSchedul.UrlManager()
        self.downloader = Download.Downloader()
        self.parser = Html_pareser.HtmlPare()
        self.ProceClean = Pipeline.pinline
        self.outjson = FeeDExport.FeedExp()
        self.CollectAllData=[]


    def craw(self):
        count = 1
        ###opts  为1时判断是否还有待爬用户对象，2时判断是否还有待爬URL
        while self.UrlAndIDContr.HasNew_IdOrUrl(opts = 1):
            print("preparing craw pages.....\n\n ")
            newid = self.UrlAndIDContr.GetNew_IdOrurl(opts = 1)
            
            for options in range(1,3):
                self.UrlAndIDContr.urlgenerate(options, newid)
                while self.UrlAndIDContr.HasNew_IdOrUrl(opts = 2):
                    print("--------------------\n now %d page.....\n\n----------------\n "%count)
                    count+=1
                    newurl = self.UrlAndIDContr.GetNew_IdOrurl(opts = 2)
                    responses = self.downloader.geturl(newurl)
                    if responses is None:
                        pass
                    else:
                        ##这里数据可能是空,容易出现问题，注意
                        GetpartHtml = self.parser.getfenlist(responses)
                        newdata = self.ProceClean.getdata(GetpartHtml = GetpartHtml,ownner_id = newid,opts = options)
                        # print("\n--------------------new------------------------\n"
                        #     ,newdata
                        #     ,"\n--------------------new------------------------\n")
                        self.CollectAllData=self.CollectAllData + newdata
                        # print("\n--------------------self------------------------\n",
                        #     self.CollectAllData,
                        #     "\n--------------------self------------------------\n")
        self.outjson.tojson(self.CollectAllData)
        print("||done||")


if __name__ == '__main__':
    obj_spider = SpiderMain()
    obj_spider.craw()


