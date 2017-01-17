#coding:utf-8  
temp = []
txt = open('1.txt', 'r')
context = txt.read()
temp = context.split("\n")
txt.close()
#取出段落
txt = open('2.txt', 'w')
txt.truncate()
txt.write("    ")
#清空文件
b = len(temp)
#取出元素个数
para = []

for i in range(0, b):
	para.append(temp[i].strip())

c = len(para)	
	
for i in range(0, c):
	if len(para[i]):
		txt.write(para[i] + "\n" + "    ")

txt.close()