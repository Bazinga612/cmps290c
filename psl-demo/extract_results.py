class hello:
	def __init__(self):
		self.targetfile=None

	def extract_targets(self,fname):
		self.real_targets=[]
		inf=open(fname,'r')
		inl=inf.readlines()
		for el in inl:
			el=el.split()
			a=el[0].strip()
			b=el[1].strip()
			c=a+' '+b
			#print(c)
			self.real_targets.append(c)

	def extract_results(self,fname):
		self.extracted_results=[]
		inf=open(fname,'r')
		inl=inf.readlines()
		of=open('extracted_positive_results.txt','w')
		#USERSSUBREDDITS(liberal_one, t5_vf2) = 9.22337203685478E-45
		for el in inl:
			el=el.split('(')
			if len(el)>0:
				if el[0]=='USERSSUBREDDITS':
					aaa=el[1].split(')')
					bbb=aaa[0]
					both=bbb.split(',')
					first=both[0].strip()	
					second=both[1].strip()
					combined=first+" "+second
					
					ddd=aaa[1]
					eee=ddd.split('=')
					fff=eee[1].strip()
					scr=float(fff)
					if scr>0.1 and scr!=1:
						#print(combined,scr)
						self.extracted_results.append(combined)
			else:
				continue;

	def compare(self):	
		correctly_extracted=[x for x in self.real_targets if x in self.extracted_results]
		print(len(correctly_extracted),"correctly extracted! out of ",len(self.real_targets))

h=hello()
h.extract_targets('real_targets.txt')
h.extract_results('result_nehal.txt')
h.compare()