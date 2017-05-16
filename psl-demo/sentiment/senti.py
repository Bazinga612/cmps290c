from nltk.corpus import sentiwordnet as swn
import csv
import re

class sentiment:
	def __init__(self):
		self.hello=True

	def readall(self):
		with open("allcomments.csv","r") as f:
			reader = csv.reader(f)			#reading using CSV reader coz numpy doesn't read text 
			for j in range(20):
				row=next(reader)
				try:
					#print(len(row[2]))
					texts1=row[2]
					texts2=texts1[2:-2]
					'''mega=[]
					elx=texts2.split('\', \'')
					for simp in elx:
						sx=simp.split('", "')
						if len(sx)==1:
							mega.append(simp)
						else:
							mega.extend(sx)'''
					re.split(r'["\'], ["\']', ''this is what', "is called life"')		
					if j==17:
						for el in mega:
							print(el)
					print(j+1,':',len(elx))
				except:
					print(j+1,": couldn't print")
					continue;

sent = sentiment()
sent.readall()