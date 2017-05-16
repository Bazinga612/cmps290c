inf1=open('users_obs.txt','r')
inf2=open('subreddits_obs.txt','r')
of=open('users_subreddits.txt','w')
intext1=inf1.read()
intext2=inf2.read()
itx1=intext1.split()
itx2=intext2.split()
crossed=[(a,b) for a in itx1 for b in itx2]
for el in crossed:
	of.write(el[0]+"	"+el[1]+'\n')
of.close()