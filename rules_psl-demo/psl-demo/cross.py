import itertools
import pickle
users = []
subreddits =[]
list1=[]
usersfile = open("users_obs.txt", 'r')
for line in usersfile.readlines():
    users.append([line])
subfile = open("subreddits_obs.txt", 'r')
for line in subfile.readlines():
    subreddits.append([line])
list1=itertools.product(users,subreddits)

thefile = open('newtest2.txt', 'w+')

#with open("test2.txt", "wb") as fp:   #Pickling
	#pickle.dump(list1, fp)
#for item in thefile:
  	#print>>thefile, item
	#print item
for item in list1:
  print>>thefile, item
