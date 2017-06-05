import csv,sys,os

class userrating:
	def __init__(self):
		self.attrs={}
		self.huge={}		#stores the number of comments
		self.updowns={}
		self.sentiments={}

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

	def loadsentiments(self):
		sentimentfile='../sentiment/sentiments.csv'
		with open(sentimentfile,'r') as f:
			reader=csv.reader(f)
			for j in range(5045):
				row=next(reader)
				self.sentiments[(row[0],row[1])]=[row[2],row[3]]

	def lookupsentiment(self,userid,subredditid):
		return self.sentiments[(userid,subredditid)]

	def lookupdown(self,userid,subredditid):
		return self.updowns[(userid,subredditid)]	

	def retrieve_noc(self,userid,subredditid):			#retrieve the number of comments
		temp=self.huge[userid]
		return temp[self.attrs[subredditid]]

	def rating(self,user,subredditid):		#this function will compute the rating between a user and a subreddit
		possent,negsent=self.lookupsentiment(user,subredditid)
		possent=float(possent)
		negsent=float(negsent)
		updown=int(self.lookupdown(user,subredditid))
		nocs=int(self.retrieve_noc(user,subredditid))
		#rating from the comments
		#print("possent/negsent/updown/no.of.comments",possent,negsent,updown,nocs)
		if nocs>0:
			rating_comment=0.5+(nocs)*0.1			#bias of 0.5
		else:
			rating_comment=0
		rating_comment=min(1,rating_comment)

		#rating from the upvotes
		if updown==0:
			rating_votes=0
		else:
			if updown>0:
				rating_votes=0.5+updown*0.2			#the values of 20 should be the mean of all values, it will be replaced later
			else:
				rating_votes=0.5+updown*(-0.2)
		rating_votes=min(1,rating_votes)

		#rating from the sentiment
		if possent>negsent:
			rating_senti=1
		else:
			rating_senti=-1

		avgrating=(rating_comment+rating_votes+rating_senti)/3
		return avgrating
		#print("three ratings",rating_senti,rating_votes,rating_comment)
		#print(user,subredditid,avgrating)

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

	def findallratings(self):
		#outf=open('allratings.txt','w')
		csvfile1=open('allratings.csv', 'w',newline='')
		csvfile=csv.writer(csvfile1,delimiter=',')
		ofilex=open('pairsnotfound.txt','w')
		infile1=open('../users_obs.txt','r')
		infile2=open('../subreddits_obs.txt','r')
		inread1=infile1.read()
		inread2=infile2.read()
		allusers=inread1.split()
		allsubreddits=inread2.split()
		allpairs=[(a,b) for a in allusers for b in allsubreddits]
		lenx=len(allpairs)
		for j in range(lenx):
			el=allpairs[j]
			#print(el)
			try:
				rating=self.rating(el[0],el[1])
				temp=[el[0],el[1],rating]
				csvfile.writerow(temp)
			except:
				continue;
			self.drawProgressBar((j+1)/lenx)

uu=userrating()
uu.loadnoc()
uu.loadupdowns()
uu.loadsentiments()
print(uu.rating('911_was_an_insidejob','t5_6'))
uu.findallratings()