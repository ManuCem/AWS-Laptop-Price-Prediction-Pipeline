AWS Laptop Price Prediction Pipeline
This project demonstrates a production-grade ML pipeline that transforms "awful" raw data into accurate laptop price predictions.

🏗️ Architecture
EventBridge: Scheduled the pipeline triggers.

EC2: Preprocessed messy laptop data via Python.

S3: Centralized data lake storage.

Glue: Mapped the data schema.

Athena: Validated data using SQL.

QuickSight: Visualized price trends and metrics.

SageMaker: Trained and deployed the XGBoost model.

IAM: Managed secure service access.

CloudWatch: Monitored logs and pipeline health.

SNS: Alerted via email on failures.

🧹 The "Awful Data" Challenge
The raw data was unusable due to inconsistent types and missing values. I used an EC2-hosted Python environment to clean and standardize the data before it entered the AWS ecosystem.

(Insert your "EC2 Proof" capture here)

🤖 Model Results
The XGBoost model provides price predictions with an average error of approximately $80, handling complex hardware features efficiently.

(Insert your "SageMaker Result" capture here)

🚀 Step-by-Step Upload Instructions
When you get to your other PC:

Initialize: git init

Add Files: Put your notebook, script, and images in the folder.

Stage: git add .

Commit: git commit -m "Complete AWS Data Pipeline with XGBoost"

Connect: git remote add origin [Your-Repo-URL]

Push: git push -u origin main
