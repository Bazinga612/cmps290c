'''
This code takes the extracted text from the result and compares the extracted results with the observations and targets to find the precision, recall and f-measure.
'''

class test:
	def __init__(self,obsfname,targetfname,extracted):
		self.obsfname=obsfname
		self.target=targetfname
		self.extracted=extracted
		self.obsdx={}
		self.tardx={}
		tarinf=open(targetfname,'r')
		tarlines=tarinf.readlines()
		for line in tarlines:
			line=line.strip()
			a,b=line.split()
			tardx[(a,b)]=1

	def testit(self):		
		
			#if b==self.attr:


ex=extract('../userssubreddits_obs.txt','../userssubreddits_targets.txt','refined.txt')
ex.extractit()
