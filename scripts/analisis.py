import pandas as pd
import io
import boto3

s3 = boto3.client('s3')
BUCKET = 'data-project-manucem'
resp = s3.list_objects_v2(Bucket=BUCKET, Prefix='clean/')


files=[]
for obj in resp['Contents']:
        file_path = obj['Key']
        if file_path.endswith('.csv'):
                files.append(file_path)

df_list = []
for f in files:
    raw_bytes = s3.get_object(Bucket=BUCKET, Key=f)['Body'].read()
    df_list.append(pd.read_csv(io.BytesIO(raw_bytes)))

#Pandas

df = pd.concat(df_list, ignore_index=True)


print("top 5 mejor valoracion",df.sort_values(by='rating', ascending=False).head(5))
