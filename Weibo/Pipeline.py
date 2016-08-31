import re

class pinline(object):
	def getdata(GetpartHtml,ownner_id,opts):
		print("processing cleaning....")
		initial = []
		allitems =re.split(r"follow_item S_line2",GetpartHtml)
	
		for item_idex in range(1,len(allitems)):
			A = {}
			data = {}
			A["UserId"] = re.findall(r"uid=(\d+)&fnick=\w+\s*\w*&sex=\w",allitems[item_idex])
			A["UserName"] = re.findall(r"uid=\d+&fnick=(\w+\s*\w*)&sex=\w",allitems[item_idex])
			A["Sex"] = re.findall(r"uid=\d+&fnick=\w+\s*\w*&sex=(\w)",allitems[item_idex])
			A["FromDevice"] = re.findall(r'class=\\"from\\" >(\w+\s*\w*)<\\/a>关注',allitems[item_idex])
			A["Adress"] = re.findall(r"地址<\\/em><span>(\w+\s*\w*)<\\/span>",allitems[item_idex])
			A["follow"] = re.findall(r'follow\\" >(\d+)<\\/a><\\/em><\\/span>',allitems[item_idex])
			A["CurrentFans"] = re.findall(r'current=fans\\" >(\d+)<\\/a>',allitems[item_idex])
			A["weibo_cnt"] = re.findall(r'微博<em class=.*count.*<a.*\d*\\" >(\d+)<\\/a>.{10}',allitems[item_idex],re.S) 
			for keys in A:
				if len(A[keys])==0:
					data[keys] = None
				else:
					data[keys] = A[keys][0]
			if opts==1:
				data["FansOrFol"] = "fans"
			else:
				data["FansOrFol"] = "follow"
			data["ownner"] = ownner_id

			initial.append(data)
		return initial
		


   


