import boto3
import pandas as pd
import s3fs

client = boto3.client('s3')
path = 's3://cricketdataa/ODI data.csv'
df = pd.read_csv(path)
print(pd.options.display.max_rows)
#print(df.info())
#print(df.head())
hsgt80 = df[df['50'] > '50']
print(hsgt80)
