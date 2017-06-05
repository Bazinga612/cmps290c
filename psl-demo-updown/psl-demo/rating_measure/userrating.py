import csv

class userrating:
	def __init__(self):
		self.attrs={}
		self.huge={}		#stores the number of comments
		self.updowns={}

	def loadnoc(self):
		commentsfile='refined_all.csv'
		with open(commentsfile,'r') as f:
			reader = csv.reader(f)			#reading using CSV reader coz numpy doesn't read text 
			headerrow=next(reader)
			for k in range(len(headerrow)):
				elll=headerrow[k].strip()
				elll=elll[1:-1]
				self.attrs[elll]=k
			#print(self.attrs)
			for j in range(3673):
				row=next(reader)
				user=row[0]
				user=user[1:-1]
				row.pop(0)
				row.insert(0,user)
				self.huge[user]=row

	def loadupdowns(self):
		updownfile='ups.csv'
		with open(updownfile,'r') as f:
			reader=csv.reader(f)
			headerrow=next(reader)
			for j in range(5045):
				row=next(reader)
				self.updowns[(row[0],row[1])]=row[2]
				#print(row['author'],row['subreddit_id'],row['ups'])

	

	def lookupdown(self,userid,subredditid):
		return self.updowns[(userid,subredditid)]	

	def retrieve_noc(self,userid,subredditid):			#retrieve the number of comments
		temp=self.huge[userid]
		return temp[self.attrs[subredditid]]




uu=userrating()
uu.loadnoc()
print(uu.retrieve_noc('10-Dec','t5_6'))
uu.loadupdowns()
print(uu.lookupdown('25462y7asdfh','t5_6'))