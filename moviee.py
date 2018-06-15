import pandas as pd
r_cols=['user_id','movie_id','rating']
ratings=pd.read_csv('u.data.csv',sep='\t',names=r_cols,usecols=range(3))
m_cols=['movie_id','title']
movies=pd.read_csv('u.item.csv',sep='|',names=m_cols,usecols=range(2))
ratings=pd.merge(movies,ratings)
ratings.head()
movieRatings=ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
movieRatings.head()
youngF=movieRatings['Young Frankenstein (1974)']
youngF.head()
similarMovies=movieRatings.corrwith(youngF)
similarMovies=similarMovies.dropna()
df=pd.DataFrame(similarMovies)
df.head(10)
similarMovies.sort_values(ascending=False) # redency coz many values are 1 resolved furthur
moviestats=ratings.groupby('title').agg({'rating':[np.size,np.mean]})
moviestats.head()
popularMovies=moviestats['rating']['size']>=100
moviestats[popularMovies].sort_values([('rating','mean')],ascending=False)[:15]
df=moviestats[popularMovies].join(pd.DataFrame(similarMovies,columns=['similarity']))
df.head()
df.sort_values(['similarity'],ascending=False)[0:15]
# fully build recommender system
import pandas as pd
r_cols=['user_id','movie_id','rating']
ratings=pd.read_csv('u.data.csv',sep='\t',names=r_cols,usecols=range(3))
m_cols=['movie_id','title']
movies=pd.read_csv('u.item.csv',sep='|',names=m_cols,usecols=range(2))
ratings=pd.merge(movies,ratings)
ratings.head()
userRatings=ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
userRatings.head()
corrMatrix=userRatings.corr()
corrMatrix.head()
corrMatrix=userRatings.corr(method='pearson',min_periods=100)
corrMatrix.head()
myRatings=userRatings.loc[0].dropna()
myRatings
simCandidates=pd.Series()
for i in range(0, len(myRatings.index));
	print "Adding similarities for" + myRatings.index[i]+ "..."
	sims= corrMatrix(myRatings.index(i).dropna())
	sims=sims.map(lambda x: x* myRatings(i))
	simCandidates=simCandidates.append(sims)
print "sorting..."
simCandidates.sort_values(inplace=True, ascending=False)
print simCandidates.head(10)	 
simCandidates=simCandidates.groupby(simCandidates.index).sum()
simCandidates.sort_values(inplace=True,ascending= False)
simCandidates.head(10)
filteredSims=simCandidates.drop(myRatings.index)
filteredSims.head(10)