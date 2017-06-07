from scipy.stats import pearsonr
import numpy as np
import math,os,sys

class neighborhood:
	def __init__(self):
		self.data=np.loadtxt('../rating_measure/allratings.txt',delimiter=',')
		self.shp=self.data.shape
		self.find_average_rating()

	def getusers(self):
		self.userlist=[]
		with open('../rating_measure/allratings2.csv','r') as f:
			reader=csv.reader(f)
			headerrow=next(reader)
			for j in range(3610):
				rowx=next(reader)
				self.userlist.append(row[0])

	def find_deviation_user(self,u):
		lx=[]
		consider=self.data[u,:]
		for el in consider:
			if el!=0:
				lx.append(el)
		avgx=np.mean(lx)
		return (avgx-self.avgrating)

	def find_deviation_item(self,i):
		lx=[]
		consider=self.data[:,i]
		for el in consider:
			if el!=0:
				lx.append(el)
		avgx=np.mean(lx)
		return (avgx-self.avgrating)

	def find_average_rating(self):
		allratings=[]
		for j in range(self.shp[0]):
			vect=self.data[j,:]
			for k in range(len(vect)):
				if vect[k]!=0:
					allratings.append(vect[k])
		self.avgrating=np.mean(allratings)

	def find_base_rating(self,p,q):
		base=self.avgrating+self.find_deviation_user(p)+self.find_deviation_item(q)
		return base

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

	def find_k_similar_items(self,u,i,k):
		#finding out which items the user has rated
		lx=self.data[u,:]
		finalx=[]
		userrated=[]
		for j in range(len(lx)):
			if lx[j]!=0 and j!=i:
				userrated.append((j,self.compute_pearson_item(i,j)))
		userrated.sort(key=lambda tup: tup[1],reverse=True)
		if len(userrated)<k:
			k=len(userrated)
		for i in range(k):
			finalx.append(userrated[i][0])
		return finalx

	def predict_rating(self,p,q):
		bias=self.find_base_rating(p,q)
		similaritems=self.find_k_similar_items(p,q,3)
		numerator=0
		denominator=0
		for g in range(len(similaritems)):
			r=similaritems[g]
			numerator+=self.shrunk_correlation(q,r)*(self.data[p,r]-self.find_base_rating(p,r))
			denominator+=self.shrunk_correlation(q,r)
		if denominator!=0:
			return bias+numerator/denominator
		else:
			return 0

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
		
	def predict_all_ratings(self):
		diff=[]
		sqdiff=[]
		count=0
		total=self.shp[0]*self.shp[1]
		for i in range(self.shp[0]):
			for j in range(self.shp[1]):
				if self.data[i,j]!=0:
					count+=1
					real=self.data[i,j]
					predicted=self.predict_rating(i,j)
					diffx=abs(real-predicted)
					sqdiffx=diffx*diffx
			self.drawProgressBar(i/self.shp[0])
		avgerr=np.mean(diff)
		mse=np.mean(sqdiff)
		rmse=math.sqrt(mse)
		print("avgerr/mse/rmse",avgerr,mse,rmse)

	#def predict_rating_names(self,userid,subredditid):

		
nhood=neighborhood()
#nhood.compute_pearson_item(2,16)
#nhood.check_item_similarity()
#print(nhood.find_k_similar_items(1413,1,5))
#print(nhood.predict_rating(3605,4))
nhood.predict_all_ratings()