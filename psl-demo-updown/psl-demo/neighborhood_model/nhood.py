from scipy.stats import pearsonr
import numpy as np

class neighborhood:
	def __init__(self):
		self.data=np.loadtxt('../rating_measure/allratings.txt',delimiter=',')
		self.shp=self.data.shape

	def getusers(self):
		self.userlist=[]
		with open('../rating_measure/allratings2.csv','r') as f:
			reader=csv.reader(f)
			headerrow=next(reader)
			for j in range(3610):
				rowx=next(reader)
				self.userlist.append(row[0])

	def shrunk_correlation(self,p,q):		#for item similarity between items p and q
		npq=self.users_rated_both(p,q)
		coeff=npq/(npq+100)*self.compute_pearson_item(p,q)*100
		return coeff

	def users_rated_both(self,p,q):
		count=0
		for j in range(self.shp[0]):
			if self.data[j,p]!=0 and self.data[j,q]!=0:
				count+=1
		return count

	def compute_pearson_user(self,p,q):	
		#print(pearsonr(arrx,arry))
		lolx=pearsonr(self.data[p,:],self.data[q,:])
		return lolx[0]
		#print(pearsonr(arrx,arrz))

	def compute_pearson_item(self,p,q):
		x=self.data[:,p]
		y=self.data[:,q]
		lolx=pearsonr(x,y)
		#print(lolx[0])
		return lolx[0]

	def check_item_similarity(self):
		lx=[]
		for i in range(20):
			for j in range(i+1,20):
				#commscore=nhood.users_rated_both(i,j)
				#commscore=nhood.compute_pearson_item(i,j)
				commscore=nhood.shrunk_correlation(i,j)
				#print(i,j,'=',commscore)
				if not np.isnan(commscore) and i!=j:
					lx.append((i,j,commscore))
				#if commscore!=0:
				#	notzero+=1
		lx.sort(key=lambda tup: tup[2],reverse=True)
		for l in range(25):
			print(lx[l])

	def find_neighborhood(self):
		
		
nhood=neighborhood()
#nhood.compute_pearson_item(2,16)
nhood.check_item_similarity()