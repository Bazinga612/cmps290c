import pandas as pd
d2 = json.load(codecs.open("2008_01.txt", "r",encoding='utf-8', errors='ignore'))
for line in d2:
    print line
ff1=pd.DataFrame(d2)    
ff1 = ff1.drop(['archived','author_flair_css_class','gilded','name','subreddit','body','author_flair_text','controversiality','created_utc','distinguished','edited','retrieved_on','score','score_hidden'], axis=1)
ff1
ff3=ff1.groupby(by=['author'])['id'].count()
ff3.sort('id', ascending=False)
ff3=ff3.drop(['[deleted]'])