#!/usr/bin/python


import matplotlib.pyplot as plt
import numpy as np


import seaborn as sns
import pandas as pd

#code;province;year;cereals;beet;sunflower;soybean;rapeseed;potato;vegetable;fruit
foods=["Зернові та зернобобові","Буряк цукровий фабричний","Соняшник","Соя","Ріпак озимий та кольза ","Картопля","Овочеві","Плодові та ягідні"]

Data=pd.read_csv('data.csv',sep=';')
Data.head(1)

print(Data)



#Data.plot()"agriculture";"industrial";"building";"services";"goverment"

ax=sns.barplot(y='province',x='cereals',hue='year',data=Data)
ax.set(xlabel='ВДВ.',ylabel='Регіон')
ax.legend(loc=1)
plt.title('Площа з якої зібрано врожай зернових та зернобобових.')
plt.show()

ax=sns.barplot(y='province',x='beet',hue='year',data=Data)
ax.set(xlabel='ВДВ.',ylabel='Регіон')
ax.legend(loc=1)
plt.title('Площа з якої зібрано врожай буряку цукрового.')
plt.show()

sns.barplot(y='province',x='sunflower',hue='year',data=Data)
ax.set(xlabel='ВДВ.',ylabel='Регіон')
ax.legend(loc=1)
plt.title('Площа з якої зібрано врожай соняшнику.')
plt.show()

sns.barplot(y='province',x='soybean',hue='year',data=Data)
ax.set(xlabel='ВДВ.',ylabel='Регіон')
ax.legend(loc=1)
plt.title('Площа з якої зібрано врожай сої.')
plt.show()

sns.barplot(y='province',x='rapeseed',hue='year',data=Data)
ax.set(xlabel='ВДВ.',ylabel='Регіон')
ax.legend(loc=1)
plt.title('Площа з якої зібрано врожай ріпака.')
plt.show()

sns.barplot(y='province',x='potato',hue='years',data=Data)
ax.set(xlabel='ВДВ.',ylabel='Регіон')
ax.legend(loc=1)
plt.title('Площа з якої зібрано врожай картоплі.')
plt.show()

sns.barplot(y='province',x='vegetable',hue='year',data=Data)
ax.set(xlabel='ВДВ.',ylabel='Регіон')
ax.legend(loc=1)
plt.title('Площа з якої зібрано врожай овочів.')
plt.show()

sns.barplot(y='province',x='fruit',hue='year',data=Data)
ax.set(xlabel='ВДВ.',ylabel='Регіон')
ax.legend(loc=1)
plt.title('Площа з якої зібрано врожай плодових та ягідних.')
plt.show()

