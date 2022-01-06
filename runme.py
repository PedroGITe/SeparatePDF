import numpy as np
f = open("run2.sh", "a")

list1=np.linspace(1, 81, num=81)
list2=[]
for i in list1:
	list2.append(int(i))
print (list2)
i=0

for i in list2:
	
	string1="pdftk full-pdf.pdf cat "
	string2=str(i)
	string3=" output "
	string4="out_"+str(i)+".pdf\n" 
	string=string1 +string2 +string3+string4
	print (string)
	f.write(string)
	i=i+1


f.close()
