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


# Choose useful columns

useful_columns = [
    'brand', 
    'model_name', 
    'cpu_model', 
    'ram', 
    'hard_disk_size', 
    'os', 
    'price',
    'screen_size',
    'rating'
]
# Select them and make a fresh copy
df_clean = df[useful_columns].copy()

#Clean the data


# 1. Price: Kill commas and dots, then turn into numbers
# We remove them so '1.30.054,00' or '1,30,054' both become '130054'
df_clean['price'] = df_clean['price'].str.replace(',', '').str.replace('.', '')
df_clean['price'] = pd.to_numeric(df_clean['price'], errors='coerce')
#errors="coerce" is simple if pandas find a no number dont crash instead turn into N/A

# 2. RAM & Storage: Just grab the numbers and ignore "GB" or "SSD"
df_clean['ram'] = df_clean['ram'].str.extract('(\d+)').astype(float)
df_clean['hard_disk_size'] = df_clean['hard_disk_size'].str.extract('(\d+)').astype(float)
#(\d+)   16GB RAM OR 512GB SSD
#tells python to keep grabbing numbers until it see a non number
# if you type d goes to keyboard \d command
#d=digit grab characters between 0 and 9
# + without the + grab only the first one with that one keep until you see a non digit



# 3. Screen Size: Simple conversion
# First, extract the number
df_clean['screen_size'] = df_clean['screen_size'].str.extract('(\d+\.?\d*)').astype(float)
#\d is nto strong enough cuz decimals 15.6 is 15
#\d+ \.? \d* 
#\d+ find digits and grab it unitl you see something that is not a digit
#\.? is the next character a job if yes grab it if not go to final step
#\d* same as d+ but if it doesnt find any digit=empty the +d error

#15.=== 15.   astype(float) converts
#15.6 == 15.6
#.6 === Fail (if the gate d+ fails is over)

# If the number is > 25, it's definitely CM, so divide by 2.54
df_clean.loc[df_clean['screen_size'] > 25, 'screen_size'] = df_clean['screen_size'] / 2.54
#loc look at the rows that have > 25 and select the columns 
#df.loc[0, 'price'] (Row named 0, Column named 'price') names
#df.iloc[0, 1] (Row 0, Column 1) positions index

df_clean['screen_size'] = df_clean['screen_size'].round(1)
#round(1) 14.709423 to 14.70

# 4. Fill the gaps
# Fill numbers with 0 and text with 'N/A'
df_clean = df_clean.fillna({
    'price': 0, 'ram': 0, 'hard_disk_size': 0, 
    'screen_size': 0, 'rating': 0,
    'brand': 'N/A', 'model_name': 'N/A', 'cpu_model': 'N/A', 'os': 'N/A'
})
# 5. Brand capitalize
df_clean['brand'] = df_clean['brand'].str.capitalize()


#send to s3
# 1. Save the 'brain' data to a physical file on the disk
df_clean.to_csv('final.csv', index=False)

# 2. Now the mailman can find 'final.csv' and upload it
output_key = 'clean/final_laptops.csv'
s3.upload_file('final.csv', BUCKET, output_key)


