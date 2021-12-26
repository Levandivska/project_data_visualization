#!/usr/bin/python

import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



def Dict2Str(dic):
	s=" "
	for d in dic:
		if (dic[d]>0):
			s=s+";"+str(d)+"-"+str(dic[d])
	return s


def Rates2Text(count,rates):
	txt="Рейтинг:\n"
	print(count)
	for index,rate in enumerate(count):
		txt=txt+rates[index]+"-"+str(rate)+";"
	return txt

Data=pd.read_csv('netflix_titles.csv',sep=',')
Data.head(1)

print(Data)


#show_id,type,title,director,cast,country,date_added,release_year,rating,duration,listed_in,description

COUNTRIES_DIC={}
countries=[]
Countries=Data['country'].drop_duplicates().dropna()

for c in Countries.to_list():
	countries.extend(c.split(','))
COUNTRIES=[]
for c in countries:
	if (COUNTRIES.count(c)==0):
		COUNTRIES.append(c)

YEARS=Data.release_year.drop_duplicates().to_list()
		
YEARS_RATES={}
for yy in YEARS:
	YEARS_RATES[yy]=Data.where(Data.release_year==yy).dropna()

 
FILMS_PER_COUNTRY={}
for c in COUNTRIES:
	FILMS_PER_YEAR={}
	for yy in YEARS:
		count=0
		r=YEARS_RATES[yy]
		for cou in r.country.astype('str').str.split(','):
			for cntr in cou:
				if (cntr==c):
					count+=1
		FILMS_PER_YEAR[yy]=count
	FILMS_PER_COUNTRY[c]=FILMS_PER_YEAR

rez=pd.DataFrame(FILMS_PER_COUNTRY)




fig = go.Figure()

for c in COUNTRIES:
                
	fig.add_trace(go.Scattergeo(
                locationmode='country names',
                locations=[c],
                text=Dict2Str(FILMS_PER_COUNTRY[c]),
                 marker = dict(
            size = 5,

            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'),
                geo='geo2'))
                
fig.update_geos(
    visible=False, resolution=50,
    showcountries=True, countrycolor="RebeccaPurple"
)
fig.update_layout(height=800, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

