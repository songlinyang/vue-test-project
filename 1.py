# 1.       给一个数组，统计每个字母出现次数，并按照出现次数排序（不限制语言）；
# EG:
# [a,a,c,b,d,c,c,c,d,d]
# {c:4,d:3,a:2,b:1}


#  2.  常用的Linux命令是什么，如何查看日志？使用shell命令过滤出日志中的ERROR出现的次数；


# 1题
arry_list = ["a","a","c","b","d","c","c","c","d","d"]
def programFun(arry_list):
	
	set_result = set(arry_list)
	results = {}
	for str in set_result:
		#strs = []
		nums = 0
		for ele in arry_list:
			if str == ele:
				nums+=1
		results[str] = nums
	

def programFun2(arry_list):
	results2 = {}
	count = 1
	for i in arry_list:
		if i not in results2.keys:
			results2[i] = 1
		else:
			results2[i] = int(results2[i])+1
			

programFun2(arry_list)



# 写在白纸上，完成之后拍照








# 2题
# ps -ef | grep 
# sed -i "1,2p" nohup.log
# grep 
# tail -f 
# netstat
# top
# mv
# cp
# ssh
# scp 

# 查看日志
# tail -f nohup.out
# tail -f nohup.log |grep "ERROR" | wc 忘记了