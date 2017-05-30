class one:
	def __init__(self):
		self.active=True

	def writeit(self,fname,lx,lot=False):
		of=open(fname,'w')
		if lot:
			for el in lx:
				of.write(el[0]+"	"+el[1]+'\n')
		else:
			for el in lx:
				of.write(str(el)+'\n')

	def crossprod(self,f1,f2,ofile,reject=None):
		inf1=open(f1,'r')
		inf2=open(f2,'r')
		of=open(ofile,'w')
		
		intext1=inf1.read()
		intext2=inf2.read()
		itx1=intext1.split()
		itx2=intext2.split()
		
		revlist=[]
		if reject:
			in3=open(reject,'r')
			inlines=in3.readlines()
			for line in inlines:
				lx=line.split()
				lx0=lx[0].strip()
				lx1=lx[1].strip()
				tupx=(lx0,lx1)
				revlist.append(tupx)
		print(len(revlist))

		crossed=[(a,b) for a in itx1 for b in itx2]
		print(len(crossed))
		remained=[x for x in crossed if x not in revlist]
		print(len(remained))
		self.writeit('userssubreddits_targets.txt',remained)

onex=one()
onex.crossprod('users_obs.txt','subreddits_obs.txt','all_users_subreddits.txt','userssubreddits_obs.txt')