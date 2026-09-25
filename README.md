LoanLens AI — Loan Approval Prediction System

An end-to-end Machine Learning and Analytics project that predicts whether a loan application is likely to be Approved or Rejected using applicant financial information.

The project combines Python, Pandas, Scikit-learn, Random Forest, Logistic Regression, Jupyter Notebook, and Streamlit to build a complete loan approval prediction workflow with an interactive web application.

Project Objective

Loan approval depends on multiple applicant and financial factors such as:

CIBIL Score

Annual Income

Loan Amount

Loan Term

Employment Status

Education

Number of Dependents

Residential Assets

Commercial Assets

Luxury Assets

Bank Assets

The objective of this project is to:

Analyze loan application data

Clean and validate the dataset

Perform exploratory data analysis

Identify important factors associated with loan approval

Train classification models

Compare Logistic Regression and Random Forest

Select a suitable model for prediction

Build an interactive loan assessment application

Generate an applicant assessment report

Note: LoanLens AI is a machine-learning decision-support prototype. It is not intended to replace bank policies, regulatory checks, or human review.

Tech Stack

Python

Pandas

NumPy

Scikit-learn

Matplotlib

Seaborn

Joblib

Streamlit

ReportLab

Jupyter Notebook

Git & GitHub

Dataset

The project uses a loan approval dataset containing 4,269 loan applications and 13 original columns.

Main Features

Feature

Description

loan_id

Unique loan application identifier

no_of_dependents

Number of dependents

education

Graduate / Not Graduate

self_employed

Self-employment status

income_annum

Annual income

loan_amount

Requested loan amount

loan_term

Loan repayment term

cibil_score

Applicant CIBIL score

residential_assets_value

Value of residential assets

commercial_assets_value

Value of commercial assets

luxury_assets_value

Value of luxury assets

bank_asset_value

Value of bank assets

loan_status

Approved / Rejected

The dataset contains no missing values and no duplicate rows after initial validation.

The dataset is kept locally and excluded from Git using .gitignore.

Project Structure

Loan-Credit-Analytics/
│
├── dataset/
│   └── loan_approval_dataset.csv
│
├── models/
│   └── loan_approval_random_forest.pkl
│
├── python/
│   ├── 01_loadData.ipynb
│   ├── 02_eda_visualization.ipynb
│   └── 03_ML.ipynb
│
├── .gitignore
├── .env
├── app.py
├── README.md
└── requirements.txt

The dataset/ folder is ignored by Git because the dataset is maintained locally.

Data Preprocessing

The dataset was prepared using Pandas and Scikit-learn.

Steps performed

Loaded the CSV dataset

Removed whitespace from column names

Cleaned target values

Checked data types

Checked missing values

Checked duplicate records

Analyzed target distribution

Separated input features and target

Removed loan_id from model features

Encoded categorical variables

Standardized numerical variables

Performed stratified train-test splitting

Target Encoding

Approved → 1
Rejected → 0

Train-Test Split

Training Data: 80%
Testing Data: 20%
Random State: 42
Stratification: Enabled

Exploratory Data Analysis

The EDA focused on understanding the relationship between financial variables and loan approval.

Main analyses

Loan approval distribution

CIBIL Score vs Loan Approval

Loan Amount vs Loan Approval

Annual Income analysis

Distribution of financial attributes

Key EDA Finding

CIBIL Score showed a substantially stronger separation between approved and rejected applications than variables such as annual income and loan amount.

Approximate CIBIL statistics observed during analysis:

Loan Status

Mean CIBIL

Approved

703

Rejected

429

This helped explain why CIBIL Score became the dominant feature in the trained Random Forest model.

Machine Learning

Two classification algorithms were evaluated.

Models Used

1. Logistic Regression

A linear classification model used as a baseline.

2. Random Forest Classifier

An ensemble tree-based classification model used for the final application.

Model Evaluation

The models were evaluated using:

Accuracy

Precision

Recall

F1-Score

ROC-AUC

Confusion Matrix

Model Comparison

Metric

Logistic Regression

Random Forest

Accuracy

91.45%

98.13%

Precision

92.10%

98.49%

Recall

94.35%

98.49%

F1-Score

93.21%

98.49%

ROC-AUC

97.26%

99.86%

The Random Forest model produced higher test-set values across the reported evaluation metrics and was selected for deployment in the Streamlit application.

These are test-set results for this specific dataset. They should not be interpreted as real-world or bank-grade performance.

Random Forest Feature Importance

The trained Random Forest model identified the following top features:

Feature

Importance

CIBIL Score

79.55%

Loan Term

6.15%

Loan Amount

3.09%

Annual Income

1.95%

Luxury Assets Value

1.95%

Interpretation

CIBIL Score is the dominant feature in the trained Random Forest model.

Feature importance indicates model reliance, not causation.

The 79.55% value should therefore not be interpreted as saying that CIBIL Score alone determines 79.55% of loan approvals.

Streamlit Application — LoanLens AI

The project includes an interactive Streamlit frontend called LoanLens AI.

Application Features

Landing Page

Company-style fintech interface

Project overview

Model metrics

Key model factors

How the system works

Call-to-action for loan assessment

Loan Assessment

Users can enter:

Number of Dependents

Education

Self-Employment Status

Annual Income

Loan Amount

Loan Term

CIBIL Score

Residential Assets

Commercial Assets

Luxury Assets

Bank Assets

The trained Random Forest model then generates:

Approved / Rejected prediction

Approval probability

Explanation of the prediction

Key applicant inputs

Model Performance Dashboard

The application also provides:

Logistic Regression vs Random Forest comparison

Accuracy

Precision

Recall

F1-Score

ROC-AUC

Confusion matrices

Random Forest feature importance

Assessment PDF

Users can download a PDF containing:

Applicant information

Prediction

Approval probability

Prediction explanation

Model information

Decision-support disclaimer

Running the Application

1. Clone the repository

git clone <your-repository-url>
cd Loan-Credit-Analytics

2. Create a virtual environment

Windows

python -m venv .venv

Activate it:

.\.venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Ensure the model exists

The trained model should be located at:

models/loan_approval_random_forest.pkl

5. Run LoanLens AI

streamlit run app.py

The application will open in your browser.

Prediction Workflow

Loan Application
       ↓
Data Preprocessing
       ↓
Feature Encoding & Scaling
       ↓
Train/Test Split
       ↓
Model Training
       ↓
Logistic Regression
       +
Random Forest
       ↓
Model Evaluation
       ↓
Random Forest Selection
       ↓
New Applicant
       ↓
LoanLens AI
       ↓
Approved / Rejected
       +
Approval Probability
       +
Prediction Explanation

Key Project Insights

The dataset contains 4,269 loan applications.

The target contains two classes: Approved and Rejected.

CIBIL Score showed the strongest separation between the two target classes during EDA.

Random Forest achieved 98.13% test accuracy and 99.86% ROC-AUC on this dataset.

CIBIL Score had the highest Random Forest feature importance.

The model considers the combined pattern of all input features rather than applying a single manually defined approval rule.

The application provides probability-based model output to support interpretation.

Limitations

This project has several limitations:

The model is trained and evaluated on a single dataset.

Test-set performance does not guarantee the same performance on new real-world banking data.

Feature importance does not establish causation.

The project does not include regulatory lending checks.

The prediction should not be treated as an automatic final loan decision.

Human review and institutional lending policies would still be required in a real lending environment.

Further validation on independent and representative datasets would be required before production use.

Future Improvements

Potential future enhancements include:

Hyperparameter tuning

Cross-validation and independent validation

Permutation importance analysis

Model calibration

More extensive fairness and bias evaluation

Live SQL database integration

Automated data pipelines

Cloud deployment

API-based model serving

Authentication and user management

Monitoring model performance after deployment

Skills Demonstrated

Data Cleaning

Exploratory Data Analysis

Statistical Analysis

Data Visualization

Feature Engineering

Classification

Model Evaluation

Random Forest

Logistic Regression

Pandas

NumPy

Scikit-learn

Streamlit

PDF Report Generation

Git & GitHub

Author

Tanay Chaturvedi

B.Tech — Artificial Intelligence & Machine Learning
CMR Institute of Technology, Bengaluru

Disclaimer

LoanLens AI is an academic machine-learning project developed for educational and demonstration purposes.

The predictions are model-generated estimates and should not be considered financial advice, a guaranteed loan decision, or a replacement for professional, regulatory, or institutional lending review.