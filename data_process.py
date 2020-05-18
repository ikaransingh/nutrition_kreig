import pandas as pd

filename='en.openfoodfacts.org.products.tsv'
data=pd.read_table(filename,sep='\t', low_memory=False)
#print(data.head(3))
#df=data.head(3)
# df.to_csv('3rows.csv')

df=data.dropna(how='all', axis=1)
# df.head().to_csv('head.csv')
# print(len(df.columns))
col1=['url',	'creator',	'created_t',	'created_datetime',	'last_modified_t',	'last_modified_datetime']
df=df.drop(columns=col1)
print(df['product_name'].count)
# print(data.columns)

