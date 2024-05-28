ncount=0
pcount=0
neutralc=0;
#The dictionary should contain all lower letters
emotional_words={'awesome':1,'but':0,'not':0,'good':1,'nice':1,'super':1,'fun':1,\
                 'delightful':1,'awful':0,'lame':0,'horrible':0,'bad':0,'tasty':1}
#Tweets:
#tweet='movie was boring but has good moral.
tweet= 'Studying New things is good and super fun.'
#tweet='movie was awesome; but characters was not good.'
#tweet='movie was super and the actions was not Good.'
#tweet='movie was awesome and the characters was also NICE.'
#preprocessing
#---Removing punctuations from the tweet----
tweet_processed=tweet.replace('!','').replace('.','').replace(',','').replace(';','')
#1. Splitting the tweet into list of words
words= tweet_processed.split(' ')
l=len(words)
#Converting words to lower for correct comparison using list comprehension
words=[x.lower() for x in words]
#2. Counting negative and positive words
for w,type in emotional_words.items():
    if w in words :
        if type==1:
            pcount+=1
        else:
            ncount+=1
            neutralc=l-(ncount+pcount)
        print('Given Tweet is:',tweet)
print('Positive word count:',pcount,' Negative word count:',ncount,' Neutral word count:',neutralc)
#3. Taking decision based on word counts
if(pcount>ncount):
    print('The tweet is positive...')
else:
    print('The tweet is negative...')
