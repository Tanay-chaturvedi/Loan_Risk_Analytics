LoanLens AI — Loan Approval Prediction System
An end-to-end Machine Learning and Analytics project that predicts whether a loan application is likely to be Approved or Rejected using applicant financial information.

LoanLens AI combines Python, Pandas, Scikit-learn, Logistic Regression, Random Forest, Jupyter Notebook, and Streamlit to build a complete loan approval prediction workflow with an interactive web application.

🎯 Project Objective
The objective of this project is to build a machine learning system that can predict loan approval based on applicant and financial characteristics.

The project focuses on factors such as:

CIBIL Score

Annual Income

Loan Amount

Loan Term

Education

Self-Employment Status

Number of Dependents

Residential Assets

Commercial Assets

Luxury Assets

Bank Assets

The system compares Logistic Regression and Random Forest Classifier and selects the better-performing model for prediction.

📊 Dataset
The project uses the Loan Approval Prediction Dataset containing:

Property	Details
Records	4,269
Original Columns	13
Input Features	11
Target	Loan Status
Target Classes	Approved / Rejected
Dataset Features
Feature	Description
loan_id	Unique loan application ID
no_of_dependents	Number of dependents
education	Graduate / Not Graduate
self_employed	Yes / No
income_annum	Annual income
loan_amount	Requested loan amount
loan_term	Loan term
cibil_score	Applicant CIBIL score
residential_assets_value	Value of residential assets
commercial_assets_value	Value of commercial assets
luxury_assets_value	Value of luxury assets
bank_asset_value	Value of bank assets
loan_status	Approved / Rejected
Note: The dataset is kept locally and is excluded from GitHub using .gitignore.

🔄 Machine Learning Workflow
Loan Dataset
     ↓
Data Loading
     ↓
Data Cleaning & Validation
     ↓
Exploratory Data Analysis
     ↓
Feature Selection
     ↓
Train / Test Split
     ↓
Preprocessing
     ├── StandardScaler
     └── OneHotEncoder
     ↓
Model Training
     ├── Logistic Regression
     └── Random Forest
     ↓
Model Evaluation
     ↓
Model Comparison
     ↓
Random Forest Selection
     ↓
Loan Approval Prediction
     ↓
Streamlit Application
🧹 Data Preprocessing
The following preprocessing steps were performed:

Removed whitespace from column names.

Cleaned target values.

Checked for missing values.

Checked for duplicate records.

Removed loan_id from model features.

Encoded the target:

Approved → 1

Rejected → 0

Applied StandardScaler to numerical features.

Applied OneHotEncoder to categorical features.

Used a stratified 80/20 train-test split.

Dataset Validation
Missing values: 0

Duplicate rows: 0

Training records: 3,415

Testing records: 854

📈 Exploratory Data Analysis
The EDA focuses on understanding the relationship between loan approval and important applicant characteristics.

Key areas include:

CIBIL Score vs Loan Approval

Annual Income vs Loan Approval

Loan Amount vs Loan Approval

Loan Term vs Loan Approval

Education vs Loan Approval

Self-Employment Status vs Loan Approval

Asset values vs Loan Approval

Loan Status distribution

Correlation between numerical features

🤖 Machine Learning Models
Two classification algorithms were trained and evaluated.

1. Logistic Regression
Logistic Regression was used as the baseline classification model.

2. Random Forest Classifier
Random Forest was used as the primary ensemble classification model.

Configuration:

RandomForestClassifier(
    n_estimators=200,
    random_state=42
)
📊 Model Performance
Metric	Logistic Regression	Random Forest
Accuracy	91.45%	98.13%
Precision	92.10%	98.49%
Recall	94.35%	98.49%
F1-Score	93.21%	98.49%
ROC-AUC	97.26%	99.86%
The Random Forest model achieved the higher test-set metrics and was selected for the LoanLens AI prediction workflow.

Random Forest Confusion Matrix
                 Predicted
                 Rejected  Approved

Actual Rejected     315       8
Actual Approved       8     523
🔍 Feature Importance
The Random Forest model identified the following as the top five features:

Rank	Feature	Importance
1	CIBIL Score	79.55%
2	Loan Term	6.15%
3	Loan Amount	3.09%
4	Annual Income	1.95%
5	Luxury Assets Value	1.95%
Important: Feature importance represents the model's reliance on a feature for prediction. It does not establish causation.

🧪 Example Prediction
A sample applicant with the following profile was tested:

Input	Value
Dependents	2
Education	Graduate
Self Employed	No
Annual Income	₹80,00,000
Loan Amount	₹2,00,00,000
Loan Term	10
CIBIL Score	750
Residential Assets	₹1,00,00,000
Commercial Assets	₹50,00,000
Luxury Assets	₹1,50,00,000
Bank Assets	₹70,00,000
Prediction
Approved

Approval Probability: 97.5%

The application can be evaluated directly through the LoanLens AI Streamlit interface.

🖥️ LoanLens AI — Streamlit Application
The project includes an interactive web application built using Streamlit.

Application Features
Professional fintech-style landing page

Loan application assessment form

Approved / Rejected prediction

Approval probability

Applicant input summary

Prediction explanation

Model performance comparison

Confusion matrix visualization

Feature importance visualization

Downloadable assessment report

Decision-support disclaimer

📁 Project Structure
Loan-Credit-Analytics/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── python/
│   ├── 01_loadData.ipynb
│   ├── 02_eda_visualization.ipynb
│   └── 03_ML.ipynb
│
├── images/
│   └── project visualizations
│
├── dataset/
│   └── local dataset files
│
└── models/
    └── local trained model
dataset/ and models/ are intentionally excluded from GitHub. The trained model is generated locally through 03_ML.ipynb.

⚙️ Installation
1. Clone the repository
git clone <your-github-repository-url>
cd Loan-Credit-Analytics
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment
Windows:

.venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
🧠 Generate the Model
Because the trained .pkl model is intentionally not stored in GitHub:

Open:

python/03_ML.ipynb
Run the notebook.

Train the Random Forest model.

Save the model to:

models/loan_approval_random_forest.pkl
The Streamlit application loads the model from this location.

▶️ Run the Application
From the project root:

streamlit run app.py
The application will open in your browser.

🔮 Prediction Workflow
A user enters applicant information through the Streamlit interface.

Applicant Information
        ↓
Preprocessing Pipeline
        ↓
Random Forest Model
        ↓
Prediction Probability
        ↓
Approved / Rejected
The application also displays the applicant information and prediction details in a downloadable assessment report.

💡 Key Insights
CIBIL Score is the dominant feature used by the trained Random Forest model.

Random Forest achieved a 98.13% test accuracy on the dataset.

Random Forest achieved a 99.86% ROC-AUC.

The model can process both numerical and categorical applicant information.

The Streamlit interface provides an interactive decision-support workflow.

⚠️ Limitations
The model is intended for educational and decision-support purposes.

Predictions should not be treated as final financial or lending decisions.

Real-world loan approval involves additional factors, policies, regulatory requirements, verification, and human review.

Feature importance indicates model behavior and should not be interpreted as causal evidence.

The dataset may not represent every real-world lending scenario.

🚀 Future Improvements
Possible future enhancements include:

Hyperparameter tuning

Cross-validation

Model calibration

Additional real-world financial features

Improved probability analysis

Model monitoring

Deployment using a cloud platform

Explainable AI techniques

🛠️ Tech Stack
Programming & Data

Python

Pandas

NumPy

Machine Learning

Scikit-learn

Logistic Regression

Random Forest Classifier

Visualization

Matplotlib

Seaborn

Development

Jupyter Notebook

VS Code

Application

Streamlit

Model Persistence

Joblib

Reporting

ReportLab

📚 Skills Demonstrated
Data preprocessing

Exploratory Data Analysis

Feature engineering

Classification

Model evaluation

Model comparison

Feature importance analysis

Python and Pandas

Scikit-learn pipelines

Streamlit application development

Git and GitHub

Technical documentation

👨‍💻 Author
Tanay Chaturvedi

B.Tech — Artificial Intelligence & Machine Learning
CMR Institute of Technology, Bengaluru

⚖️ Disclaimer
LoanLens AI is an academic machine learning project created for educational and analytical purposes. Its predictions are not a substitute for official financial assessment, regulatory verification, or human lending decisions.