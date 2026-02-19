import pandas as pd

#SDK software development kit 
#leaves aws and talk with another service
import boto3 

#Middleman between data and pandas
#boto get the file instead of downloading on ur hardrive
#download a raw bytes on ur computer and pandas cannot read 
import io

s3 = boto3.client('s3')
#remote control and choose s3
#o= <botocore.client.S3 object at 0x7f4957648f10>

BUCKET = 'data-project-manucem'
#assign the bucket

# 1. Get the list of CSVs
resp = s3.list_objects_v2(Bucket=BUCKET, Prefix='data/')
#list of the s3 of that bucket inside the data folder
#a lot of data nto only names also sizes, last time modified,key,etc

files=[]
for obj in resp['Contents']:
	file_path = obj['Key']
	if file_path.endswith('.csv'):
		files.append(file_path)

#filter of the long list
#resp["contents"] is the size key and last modified of the long list
#obj[key] is get only the key of the variable obj


# 2. Use the "Bridge" (io) to let Pandas read the Boto3 data
df_list = []
for f in files:
    raw_bytes = s3.get_object(Bucket=BUCKET, Key=f)['Body'].read()
    df_list.append(pd.read_csv(io.BytesIO(raw_bytes)))

#grab the content and translator
#s3.getobject get the file
#select each object of each bucket
#body where the content leave and read pull the data as raw binary 01
#pd.read_csv pandas reaad the fake file
#io.BytesIO grab teh 01 and translate to looks like real for pandas


# 3. Combine and save
pd.concat(df_list, ignore_index=True).to_csv('final.csv', index=False)
print("Done!")

# 4. Upload the final file back to S3

output_key = 'clean/final_laptops.csv'
s3.upload_file('final.csv', BUCKET, output_key)
print(f"File uploaded to S3: {output_key}")
