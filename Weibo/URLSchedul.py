
# structure of begining url :
# part1 : http://weibo.com/p/
# part2 : 1005052349336003
# part3 : {关注：/follow?page= 或者，粉丝：/follow?relate=fans&page=}
# part4 : 2
# part5 : #Pl_Official_HisRelation__64

# targetting ： {樊振东乒乓：1005052349336003， 
#                     丁宁：1003061814284757，
#                     周雨：1005051878678687，
#                     苦瓜檬：1005051232122234}

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.new_ids =set((1005052349336003,1003061814284757,1005051878678687,1005051232122234))
        self.old_ids = set()
        self.Domain = "http://weibo.com/p/"
        self.part1_fan = "/follow?relate=fans&page="
        self.part1_fol = "/follow?page="
        self.part2 = "#Pl_Official_HisRelation__64"


    def urlgenerate(self, opt, newid):
        if opt == 1:
            urls = set([self.Domain+str(newid)+self.part1_fan+str(x)+self.part2 for x in range(1,6)])
            for url in urls:
                self.new_urls.add(url)

        if opt == 2:
            urls = set([self.Domain+str(newid)+self.part1_fol+str(x)+self.part2 for x in range(1,6)])
            for url in urls:
                self.new_urls.add(url)

                

    def HasNew_IdOrUrl(self,opts):
        if opts ==2:
            return len(self.new_urls) != 0
        if opts ==1:
            return len(self.new_ids) != 0


    def GetNew_IdOrurl(self, opts):
        if opts == 2:
            new_url = self.new_urls.pop()
            self.old_urls.add(new_url)
            return new_url
        if opts == 1:
            new_id = self.new_ids.pop()
            self.old_ids.add(new_id)
            return new_id













 
