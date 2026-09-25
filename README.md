# LoanLens AI — Loan Approval Prediction System

An end-to-end Machine Learning and Analytics project that predicts whether a loan application is likely to be **Approved** or **Rejected** using applicant financial information.

The project combines **Python, Pandas, Scikit-learn, Logistic Regression, Random Forest, Jupyter Notebook, and Streamlit** to build a complete loan approval prediction workflow with an interactive web application.

---

## 🎯 Project Objective

The objective of this project is to build a machine learning system that predicts loan approval based on applicant and financial characteristics.

The project focuses on factors such as:

- CIBIL Score
- Annual Income
- Loan Amount
- Loan Term
- Education
- Self-Employment Status
- Number of Dependents
- Residential Assets
- Commercial Assets
- Luxury Assets
- Bank Assets

The project compares **Logistic Regression** and **Random Forest Classifier** and evaluates their performance using multiple classification metrics.

---

## 📊 Dataset

The project uses the **Loan Approval Prediction Dataset** containing:

| Property | Details |
|---|---|
| Records | 4,269 |
| Original Columns | 13 |
| Input Features | 11 |
| Target | Loan Status |
| Target Classes | Approved / Rejected |

### Dataset Features

| Feature | Description |
|---|---|
| `loan_id` | Unique loan application ID |
| `no_of_dependents` | Number of dependents |
| `education` | Graduate / Not Graduate |
| `self_employed` | Yes / No |
| `income_annum` | Annual income |
| `loan_amount` | Requested loan amount |
| `loan_term` | Loan term |
| `cibil_score` | Applicant CIBIL score |
| `residential_assets_value` | Value of residential assets |
| `commercial_assets_value` | Value of commercial assets |
| `luxury_assets_value` | Value of luxury assets |
| `bank_asset_value` | Value of bank assets |
| `loan_status` | Approved / Rejected |

> **Note:** The dataset is kept locally and is excluded from GitHub using `.gitignore`.

---

## 🔄 Machine Learning Workflow

```text
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
Data Preprocessing
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
Best Model Selection
     ↓
Loan Approval Prediction
     ↓
Streamlit Application
```

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Removed whitespace from column names.
2. Cleaned target values.
3. Checked for missing values.
4. Checked for duplicate records.
5. Removed `loan_id` from model features.
6. Encoded the target:
   - `Approved → 1`
   - `Rejected → 0`
7. Applied `StandardScaler` to numerical features.
8. Applied `OneHotEncoder` to categorical features.
9. Used a stratified 80/20 train-test split.

### Dataset Validation

- **Missing Values:** 0
- **Duplicate Rows:** 0
- **Training Records:** 3,415
- **Testing Records:** 854

---

## 📈 Exploratory Data Analysis

The EDA focuses on understanding the relationship between loan approval and important applicant characteristics.

The analysis includes:

- CIBIL Score vs Loan Approval
- Annual Income vs Loan Approval
- Loan Amount vs Loan Approval
- Loan Term vs Loan Approval
- Education vs Loan Approval
- Self-Employment Status vs Loan Approval
- Asset Values vs Loan Approval
- Loan Status Distribution
- Correlation between numerical features

---

## 🤖 Machine Learning Models

Two classification algorithms were trained and evaluated.

### 1. Logistic Regression

Logistic Regression was used as the baseline classification model.

### 2. Random Forest Classifier

Random Forest was used as the ensemble classification model.

```python
RandomForestClassifier(
    n_estimators=200,
    random_state=42
)
```

---

## 📊 Model Performance

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix

### Model Comparison

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 91.45% | **98.13%** |
| Precision | 92.10% | **98.49%** |
| Recall | 94.35% | **98.49%** |
| F1-Score | 93.21% | **98.49%** |
| ROC-AUC | 97.26% | **99.86%** |

Based on the test-set metrics, **Random Forest was selected for the LoanLens AI prediction workflow**.

### Random Forest Confusion Matrix

```text
                 Predicted
                 Rejected  Approved

Actual Rejected     315       8
Actual Approved       8     523
```

Where:

- **TN = 315**
- **FP = 8**
- **FN = 8**
- **TP = 523**

---

## 🔍 Feature Importance

The Random Forest model identified the following as the top five features:

| Rank | Feature | Importance |
|---|---|---:|
| 1 | CIBIL Score | 79.55% |
| 2 | Loan Term | 6.15% |
| 3 | Loan Amount | 3.09% |
| 4 | Annual Income | 1.95% |
| 5 | Luxury Assets Value | 1.95% |

> **Important:** Feature importance represents the model's reliance on a feature for prediction. It does **not** establish causation.

---

## 🧪 Example Prediction

A sample applicant was tested using the following information:

| Input | Value |
|---|---:|
| Dependents | 2 |
| Education | Graduate |
| Self Employed | No |
| Annual Income | ₹80,00,000 |
| Loan Amount | ₹2,00,00,000 |
| Loan Term | 10 |
| CIBIL Score | 750 |
| Residential Assets | ₹1,00,00,000 |
| Commercial Assets | ₹50,00,000 |
| Luxury Assets | ₹1,50,00,000 |
| Bank Assets | ₹70,00,000 |

### Prediction Result

**Approved**

**Approval Probability: 97.5%**

The application can be evaluated directly through the LoanLens AI Streamlit interface.

---

## 🖥️ LoanLens AI — Streamlit Application

The project includes an interactive web application built using **Streamlit**.

### Application Features

- Professional fintech-style landing page
- Loan application assessment form
- Approved / Rejected prediction
- Approval probability
- Applicant input summary
- Prediction explanation
- Model performance comparison
- Confusion matrix visualization
- Feature importance visualization
- Downloadable assessment report
- Decision-support disclaimer

---

## 📁 Project Structure

```text
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
```

> `dataset/` and `models/` are intentionally excluded from GitHub.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd Loan-Credit-Analytics
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Generate the Machine Learning Model

The trained model is **not stored in GitHub**.

To generate the model:

1. Open:

```text
python/03_ML.ipynb
```

2. Run the notebook.
3. Train the Random Forest model.
4. Save the trained model as:

```text
models/loan_approval_random_forest.pkl
```

The Streamlit application loads the model from this location.

---

## ▶️ Run the Application

From the project root directory:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🔮 Prediction Workflow

The user enters applicant information through the Streamlit interface.

```text
Applicant Information
        ↓
Preprocessing Pipeline
        ↓
Random Forest Model
        ↓
Prediction Probability
        ↓
Approved / Rejected
```

The application also displays the applicant information and prediction details in a downloadable assessment report.

---

## 💡 Key Insights

- CIBIL Score is the dominant feature used by the trained Random Forest model.
- Random Forest achieved **98.13% test accuracy**.
- Random Forest achieved **99.86% ROC-AUC**.
- The model processes both numerical and categorical applicant information.
- The Streamlit interface provides an interactive loan decision-support workflow.

---

## ⚠️ Limitations

- The model is intended for **educational and decision-support purposes**.
- Predictions should not be treated as final financial or lending decisions.
- Real-world loan approval involves additional factors, policies, regulatory requirements, verification, and human review.
- Feature importance indicates model behavior and should not be interpreted as causal evidence.
- The dataset may not represent every real-world lending scenario.

---

## 🚀 Future Improvements

Possible future enhancements include:

- Hyperparameter tuning
- Cross-validation
- Model calibration
- Additional real-world financial features
- Improved probability analysis
- Model monitoring
- Cloud deployment
- Explainable AI techniques

---

## 🛠️ Tech Stack

### Programming & Data

- Python
- Pandas
- NumPy

### Machine Learning

- Scikit-learn
- Logistic Regression
- Random Forest Classifier

### Visualization

- Matplotlib
- Seaborn

### Development

- Jupyter Notebook
- VS Code

### Application

- Streamlit

### Model Persistence

- Joblib

### Reporting

- ReportLab

---

## 📚 Skills Demonstrated

- Data preprocessing
- Exploratory Data Analysis
- Feature engineering
- Classification
- Model evaluation
- Model comparison
- Feature importance analysis
- Python and Pandas
- Scikit-learn pipelines
- Streamlit application development
- Git and GitHub
- Technical documentation

---

## 👨‍💻 Author

**Tanay Chaturvedi**

B.Tech — Artificial Intelligence & Machine Learning  
CMR Institute of Technology, Bengaluru

---

## ⚖️ Disclaimer

LoanLens AI is an academic machine learning project created for educational and analytical purposes.

Its predictions are **not a substitute for official financial assessment, regulatory verification, or human lending decisions**.