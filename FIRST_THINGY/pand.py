import matplotlib.pyplot as plt
import pandas as pd
datas=pd.read_csv("hello.csv")
#print(datas.columns)
def mean(column):
    return column.mean()
#y=datas.sort_values(['bedrooms','price','sqft_living'],ascending=[False,False,False])
#print(datas[['bedrooms','price','sqft_living']])
datas['RATIOD']=(datas['price']/(datas['bedrooms']*datas['sqft_living'])) 
#print(datas['RATIOD'])
hello=datas['city'].isin(['Kent'])
gello=datas['bedrooms'] > 3
#print(datas.columns)
#datas[gello & hello]
#print(datas[gello])
datas=datas.sort_values('bedrooms',ascending=False)
print(datas)
t=datas.drop_duplicates(subset='city')
#t.to_csv('hell_t.csv',index=True)
#datas['city'].value_counts(sort=True,normalize=True).to_csv('frfr.csv',index=True)
#z=datas.groupby('city')['price'].agg([min, max,mean]).sort_values(['mean'])
z=datas.groupby(['city','bedrooms'])[['price','yr_built']].agg([min,max])
#plt.plot(z)
#plt.show()
z.to_csv('3.csv')