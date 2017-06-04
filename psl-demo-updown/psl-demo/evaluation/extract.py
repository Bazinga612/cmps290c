'''
This code extracts information from outputfile of the PSL cli. You have to provide the predicate
or relation that you want to extract.
'''

class extract:
	def __init__(self,infname,ofname,attr,startline):
		self.infname=infname
		self.attr=attr
		self.startline=startline
		self.ofile=open(ofname,'w')

	def extractit(self):
		infile=open(self.infname,'r')
		inlines=infile.readlines()
		for j in range(self.startline,len(inlines)):
			stripped=inlines[j].strip()
			a=stripped.split('(')
			b=a[0]
			if b==self.attr:
				c=a[1]
				d=c.split(')')
				users=d[0].split(',')
				#print(users)
				e=d[1]
				f=e.split('=')
				score=f[1]
				print(users[0],users[1],score)
				self.ofile.write(str(users[0])+'	'+str(users[1])+'	'+str(score)+'\n')
			#if b==self.attr:


ex=extract('../output9.txt','refined.txt','USERSSUBREDDITS',16)
ex.extractit()