#coding:utf-8  
temp = []
txt = open('1.txt', 'r')
context = txt.read()
temp = context.split("\n")
txt.close()
#ȡ������
txt = open('2.txt', 'w')
txt.truncate()
txt.write("    ")
#����ļ�
b = len(temp)
#ȡ��Ԫ�ظ���
para = []

for i in range(0, b):
	para.append(temp[i].strip())

c = len(para)	
	
for i in range(0, c):
	if len(para[i]):
		txt.write(para[i] + "\n" + "    ")

txt.close()