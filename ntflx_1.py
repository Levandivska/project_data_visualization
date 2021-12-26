#!/usr/bin/python

import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



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


#years=Data.release_year.dropna().drop_duplicates()
countries=[]
Countries=Data['country'].drop_duplicates().dropna()
for c in Countries.to_list():
	countries.extend(c.split(','))
COUNTRIES=[]
for c in countries:
	if (COUNTRIES.count(c)==0):
		COUNTRIES.append(c)
COUNTRY_RATES={}
for c in COUNTRIES:
	COUNTRY_RATES[c]=Data.rating.where(Data.country.str.find(c).dropna()>=0).dropna().to_list()

RATES=Data.rating.dropna().drop_duplicates().to_list()

MID_RATES_COUNTRY={}
for c in COUNTRIES:
	temp=[]
	for r in RATES:
		temp.append(COUNTRY_RATES[c].count(r))
	MID_RATES_COUNTRY[c]=temp
	

fig = go.Figure()

for c in COUNTRIES:
                
	fig.add_trace(go.Scattergeo(
                locationmode='country names',
                locations=[c],
                text=Rates2Text(MID_RATES_COUNTRY[c],RATES),
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




	
	
