import PyPDF2, os
import numpy as np

while True:


    #Program to separate a pdf range, single page, or all pages


	while True:
		name = input('Write the name of the document (same folder as this script) [without .pdf] ')
		option = input('Select: single page (e.g. 2); range (2,6); all (0)')
		try:
			option=int(option)
			name=name+".pdf"
			pdfFileObject = open(name, 'rb')
			pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
			count = pdfReader.numPages
			pdfFileObject.close()

			list1=np.linspace(1, count, num=count)




			if option == 0:
				list2=[]
				for i in list1:
					list2.append(int(i))
				i=0

				for i in list2:

					string1="pdftk "
					string2= name
					string3=" cat "
					string4=str(i)
					string5=" output "
					string6="out_"+str(i)+".pdf\n"
					string=string1 +string2 +string3+string4+string5+string6
					print (string)
					os.system(string)
			if int(option) < count and int(option) != 0:
					string1="pdftk "
					string2= name
					string3=" cat "
					string4=str(option)
					string5=" output "
					string6="out_"+str(option)+".pdf\n"
					string=string1 +string2 +string3+string4+string5+string6
					os.system(string)

			break
		except ValueError:
					name=name+".pdf"
					pdfFileObject = open(name, 'rb')
					pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
					count = pdfReader.numPages
					pdfFileObject.close()
					s=list(str(option))
					i=0
					s2=[]
					for i in s:
						if i==",":
							x="-"
						else:
							 x=i
						s2.append(x)
					s2=''.join(s2)

					string1="pdftk "
					string2= name
					string3=" cat "
					string4=s2
					string5=" output "
					string6="out_"+s2+".pdf\n"
					string=string1 +string2 +string3+string4+string5+string6
					os.system(string)
					break
