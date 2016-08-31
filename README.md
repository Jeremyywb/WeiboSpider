## **WeiboSpider**
This is first ed on webo scrape

---


![这里写图片描述](http://image.beekka.com/blog/201108/bg2011082507.jpg)


    本爬虫主要使用python BeautifulSoup、re、json、urllib编写，主要爬取给定微博名人其部分粉丝与关注对象列表数据，主要流程有：

 - urllib下载网页并解析
 - re模块匹配需求数据
 - 每个对象ID拆分为两个流向：一个是用户粉丝列表，一个是用户关注列表
 - 每个列表爬取5页数据
 - 每页数据通过re拆分成每个用户单元，并匹配需求数据，单页数据组装到python字典数据结构中
 - 通过list把类似json的数据结构合并最后把数据存储到json中


----------


>总结：这个爬虫存在一个非常大的缺陷，内存问题，由于写的比较急，基本上所有数据爬完存到内存中，最后IO；如果遇到大规模爬取可能会有问题，
当然本爬虫主要解决两个问题：
    1、微博登录问题→使用cookie 详细参看 http://www.crifan.com/note_about_website_crawl_and_emulate_login/
    2、第二个是解决了由JS生成并嵌套在网页中的数据解析问题，微博比较复杂的地方在于他的文档树下载后，比较难用平常的xpath,css之类来解析，所以此处用的re模块来解析
    
    

###**URL分析**

爬取对象仅仅4个，每个对象分裂成两类URL，粉丝类与关注类

```
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
```

###**主要模块**
   >主要有Download,FeeDExport,Html_pareser,Pipeline,URLSchedul,Spider 等6个模块，每个模块分别作用是
   下载网页，数据输出，网页解析，数据处理拼装，URL管理和主程序

