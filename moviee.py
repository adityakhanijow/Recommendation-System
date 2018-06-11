import pandas as pd
r_cols=['user_id','movie_id','rating']
ratings=pd.read_csv('u.data.csv',sep='\t',names=r_cols,usecols=range(3))
m_cols=['movie_id','title']
movies=pd.read_csv('u.item.csv',sep='|',names=m_cols,usecols=range(2))
ratings=pd.merge(movies,ratings)
ratings.head()
