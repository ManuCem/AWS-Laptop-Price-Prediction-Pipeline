# 💻 AWS Laptop Price Prediction: End-to-End Data Pipeline

This project shows a **professional AWS setup** designed to turn a messy dataset into a working machine learning model. It covers the whole process: **Automation**, **Data Engineering**, **Machine Learning**, and **Management**.

---

![Architecture Diagram](assets/diagram.drawio.png)

---

## 📊 Data Source
The raw data for this project came from **Kaggle**:

* **Dataset Link:** [Amazon Laptop Messy Dataset](https://www.kaggle.com/datasets/rudraprasadbhuyan/amazon-laptop-messy-dataset)
* **Original Format:** 10 separate CSV files that needed a lot of cleaning and joining.

---

## 🏗️ Architecture Overview
* **EventBridge**: Automatically starts the pipeline.
* **EC2**: Uses Python to clean and join the 10 messy CSV files.
* **S3**: Central storage (Data Lake) using **Parquet** to save space.
* **Glue**: Managed the data structure and the Data Catalog.
* **Athena**: Used SQL to check if the data was correct.
* **QuickSight**: Created charts to show laptop price trends.
* **SageMaker**: Trained an XGBoost model to predict prices.
* **IAM**: Managed security and access for all services.
* **CloudWatch**: Monitored the health of the model training.
* **SNS**: Sends an email alert if the pipeline fails.

---

## 🧹 The Data Challenge
The project started with 10 inconsistent CSV files. The data was difficult to use because of missing values, different units (GB vs TB), and text errors.

### 🛠️ The Solution (EC2 + Python)
I used an **Amazon EC2** instance to run a Python script that:
1.  **Joined** the 10 separate files into one master file.
2.  **Fixed** hardware specs using Regex (Regular Expressions).
3.  **Cleaned** the formatting errors to provide high-quality data for the model.

#### Raw Data Samples
![Raw Data 1](assets/raw_data1.png)
![Raw Data 2](assets/raw_data2.png)

#### Cleaned Output
![Clean Data](assets/clean_data.png)

---

## ⚡ Making it Faster: AWS Glue ETL
To make the pipeline cost-effective and ready for Machine Learning, I used **AWS Glue** for an ETL (Extract, Transform, Load) job.

### 🛠️ Data Change & Schema Mapping
Instead of just moving the files, I set up a Glue Job to:
* **Change Format**: Converted the CSV data into **Apache Parquet** to save space.
* **Fix Data Types**: Manually changed types (for example, turning "Price" from text into a number) to make sure SageMaker and Athena could use it correctly.

![AWS Glue ETL Job](assets/glue.png)

### 💰 Why this helps:
* **Save Space**: Parquet files are much smaller in S3 than the original CSVs.
* **Save Money**: Because Parquet is a better format, **Amazon Athena** scans 90% less data, making it faster and cheaper.

---
## 📊 Checking the Data: TAD
To check the new `.parquet` files, I used **TAD (Tabular Data Viewer)**. 

TAD allowed me to view the large datasets on my computer to:
* **Filter Data**: Quickly check millions of rows to see if the cleaning worked.
* **Check the Structure**: Make sure the data types from AWS Glue were correct in the final files.
* **Quick Charts**: Create fast charts to see price trends without using a heavy tool.

![TAD Visualization](assets/parquet.png)

---

## 🚀 Data Workflow
The data follows two paths after it reaches Amazon S3:

### 1. The Analytics Path (Validation)
**AWS Glue** organizes the data so **Amazon Athena** can run SQL queries to check it.

![Query Result 2](assets/query5.png)

### 2. The ML Path (Intelligence)
**Amazon SageMaker** uses the optimized Parquet data to train a model that predicts laptop prices.

![SageMaker Training](assets/sagemaker.png)

---

## 🛡️ Cleanup & Cost Control
To follow AWS best practices and save money, I used my custom tool:

* **Tool Used**: [AWS-Governance-Cleanup-Tool](https://github.com/ManuCem/AWS-Governance-Cleanup-Tool)
* **Action**: Automatically deleted unused resources (EC2, S3, SageMaker) to avoid unnecessary bills.

---

## 🌟 Key Skills
* **Cloud Architecture**: Designing automated pipelines.
* **Data Engineering**: Joining 10+ files and optimizing data with **Parquet**.
* **Machine Learning**: Implementing an XGBoost model.
* **Cost Management**: Cleaning up resources to save money.
