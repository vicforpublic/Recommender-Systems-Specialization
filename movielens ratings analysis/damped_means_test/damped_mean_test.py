import pandas as pd
import numpy as np
Ratings=pd.read_csv("ratings.csv")
Movies=pd.read_csv("movies.csv")
Tags=pd.read_csv("tags.csv")
Ratings_mean=Ratings.groupby(['movieId'])[['rating']].mean().rename(columns = {'rating': 'Mean_rating'}).reset_index()
# Calculating damped mean using alpha = 5
Ratings_sum=Ratings.groupby(['movieId'])[['rating']].sum().rename(columns = {'rating': 'sum_rating'}).reset_index()
Ratings_sum['sum_rating_factor']=Ratings_sum['sum_rating']+5*(Ratings["rating"].mean())
Ratings_count=Ratings.groupby(['movieId'])[['rating']].count().rename(columns = {'rating': 'count_rating'}).reset_index()
Ratings_count['count_rating_factor']=Ratings_count['count_rating']+5
Ratings_damped=pd.merge(Ratings_sum,Ratings_count[['movieId','count_rating','count_rating_factor']],on=['movieId'],how='left')
Ratings_damped['damped_mean']=Ratings_damped['sum_rating_factor']/Ratings_damped['count_rating_factor']
Ratings_mean_dampmean=pd.merge(Ratings_mean[['movieId','Mean_rating']],Ratings_damped[['movieId','damped_mean']],on=['movieId'],how='left')
# Sorting to get top rated movies
Ratings_mean_dampmean = Ratings_mean_dampmean.sort(['Mean_rating'], ascending=False)