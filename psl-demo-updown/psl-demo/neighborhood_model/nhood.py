from scipy.stats import pearsonr
import numpy as np

class neighborhood:
	def __init__(self):
		self.data=np.loadtxt('../rating_measure/allratings.txt',delimiter=',')
		print(self.data.shape)


	def getusers(self):
		self.userlist=[]
		with open('../rating_measure/allratings2.csv','r') as f:
			reader=csv.reader(f)
			headerrow=next(reader)
			for j in range(3610):
				rowx=next(reader)
				self.userlist.append(row[0])

	#def shrunk_correlation(self):

	def users_rated_both(self):
		

	def compute_pearson(self,p,q):	
		#print(pearsonr(arrx,arry))
		lolx=pearsonr(self.data[p,:],self.data[q,:])
		return lolx[0]
		#print(pearsonr(arrx,arrz))

nhood=neighborhood()
nhood.compute_pearson(45,78)