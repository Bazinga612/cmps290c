from nltk.corpus import sentiwordnet as swn
import csv,sys,os  
import re
import string
import sentiment_average_fast as saf
import numpy as np

class sentiment:
	def __init__(self):
		self.hello=True
		self.exclude = set(string.punctuation)
		self.exclude.discard('.')
		self.ofile=open('sentiments.txt','w')
		self.ofile1=open('positive_sentiments.txt','w')
		self.ofile2=open('negative_sentiments.txt','w')

	def strip_punct(self,s):			#removes the functions
		s = s.replace('-',' ')
		s = s.replace('\n',' ')
		s1 = ''.join(ch for ch in s if ch not in self.exclude)
		s1=s1.lower()
		return s1

	def drawProgressBar(self,percent, barLen = 50):			#just a progress bar so that you dont lose patience
	    sys.stdout.write("\r")
	    progress = ""
	    for i in range(barLen):
	        if i<int(barLen * percent):
	            progress += "="
	        else:
	            progress += " "
	    sys.stdout.write("[ %s ] %.2f%%" % (progress, percent * 100))
	    sys.stdout.flush()

	def readall(self):
		with open("allcomments.csv","r", encoding='utf8',errors='ignore') as f:
			reader = csv.reader(f)			#reading using CSV reader coz numpy doesn't read text 
			senticlass=saf.sentiment()
			for j in range(5045):
				row=next(reader)
				texts1=row[2]			#.split(',')
				texts2=self.strip_punct(texts1)	
				spx=texts2.split('.')
				tpos=[]
				tneg=[]
				for line in spx:
					senti=senticlass.makesense_sent(line)
					if senti[0]!=0:
						tpos.append(senti[0])
					if senti[1]!=0:
						tneg.append(senti[1])
				avgpos=np.mean(tpos)
				avgneg=np.mean(tneg)
				if np.isnan(avgpos)==False:
					strx1=row[0]+','+row[1]+','+str(avgpos)+'\n'
					self.ofile1.write(strx1)
				if np.isnan(avgneg)==False:
					strx2=row[0]+','+row[1]+','+str(avgneg)+'\n'				
					self.ofile2.write(strx2)
				self.drawProgressBar(j/5045)

sent = sentiment()
sent.readall()