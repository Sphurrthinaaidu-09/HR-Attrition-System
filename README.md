# 📊 HR Attrition Intelligence System

## 🚀 Project Overview

Employee attrition is one of the most significant challenges faced by organizations. High attrition rates increase recruitment costs, reduce productivity, and impact organizational stability.

The HR Attrition Intelligence System is an end-to-end Machine Learning application designed to predict employee attrition risk and provide actionable HR insights. The system analyzes employee-related factors and identifies individuals who are likely to leave the organization, enabling proactive retention strategies.

---

## 🎯 Problem Statement

Organizations often struggle to identify employees at risk of leaving before attrition occurs.

This project aims to:

- Predict employee attrition using Machine Learning.
- Identify key factors influencing employee turnover.
- Provide HR-friendly risk analysis and recommendations.
- Enable workforce-level attrition monitoring through bulk analysis.

---

## 📂 Dataset

**Dataset:** IBM HR Analytics Employee Attrition Dataset

- Total Records: 1,470 Employees
- Features: 35 Original Features
- Final Features After Encoding: 44+
- Target Variable: Attrition (Yes / No)

### Key Features:

- Age
- Department
- Job Role
- Monthly Income
- Job Satisfaction
- Environment Satisfaction
- Work Life Balance
- Overtime
- Years At Company
- Total Working Years
- Marital Status
- Education Field

---

## 🔍 Exploratory Data Analysis (EDA)

Performed detailed analysis to understand employee behavior and attrition trends.

### Key Insights

- Employees working overtime showed significantly higher attrition rates.
- Sales department experienced higher employee turnover.
- Low job satisfaction was strongly associated with attrition.
- Single employees showed higher attrition tendencies than married employees.

### Visualizations

- Employee Attrition Distribution
- Department-wise Attrition Analysis
- Overtime vs Attrition
- Job Satisfaction vs Attrition
- Feature Importance Analysis

---

## ⚙️ Data Preprocessing

### Data Cleaning

Removed non-informative columns:

- EmployeeCount
- EmployeeNumber
- Over18
- StandardHours

### Encoding

Applied One-Hot Encoding to categorical features.

### Feature Engineering

Generated 44+ machine-learning-ready features.

### Scaling

Applied StandardScaler for model optimization.

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

### 1. Logistic Regression
Used as a baseline classification model.

### 2. Balanced Logistic Regression
Addressed class imbalance using: `class_weight = "balanced"`

### 3. Decision Tree Classifier
Used for interpretable decision-based classification.

### 4. Random Forest Classifier
Used ensemble learning for improved prediction performance.

---

## 📈 Model Performance

| Model | Accuracy |
| :--- | :--- |
| Logistic Regression | 87% |
| Balanced Logistic Regression | 73% |
| Decision Tree | 76% |
| Random Forest | 88% |

### Selected Production Model
**Balanced Logistic Regression**

**Reason:**
Although Random Forest achieved higher accuracy, Balanced Logistic Regression demonstrated better identification of attrition cases and provided interpretable feature importance for HR decision-making.

---

## 🔑 Top Factors Influencing Attrition

The model identified the following important drivers:

- Overtime
- Marital Status
- Business Travel Frequency
- Job Role
- Performance Rating
- Technical Education Background
- Job Satisfaction
- Environment Satisfaction
- Years In Current Role

These insights help HR teams focus on retention strategies.

---

## 🖥️ Application Features

### Employee Risk Assessment
- Predict attrition risk for an individual employee.
- **Risk Score Generation:** Generate employee-specific attrition risk percentages.
- **Risk Classification:** Low Risk, Medium Risk, High Risk
- **Explainable Insights:** Displays key contributing factors affecting risk.
- **HR Recommendations:** Provides retention-oriented recommendations.

### Bulk Employee Analysis
- Analyze multiple employees simultaneously through CSV upload.
- **Workforce Intelligence Dashboard:** Workforce Risk Distribution, High-Risk Employee Identification, Organizational Attrition Trends

---

## 🛠️ Technology Stack

### Programming Language
- Python

### Data Analysis
- Pandas
- NumPy

### Visualization
- Matplotlib

### Machine Learning
- Scikit-Learn

### Deployment
- Streamlit

### Model Persistence
- Joblib

---

## 📸 Application Screenshots

*Add screenshots of:*
1. Home Dashboard
2. Employee Risk Assessment
3. Diagnostic Report
4. Bulk Workforce Analysis
5. Risk Distribution Charts

---

## 📁 Project Structure

```text
HR_Attrition_Intelligence_System/
├── dataset/
├── eda.py
├── preprocessing.py
├── encoding.py
├── train_model.py
├── streamlit_app.py
├── attrition_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- **Data Cleaning:** Handling missing attributes and removing non-informative tracking columns.
- **Exploratory Data Analysis (EDA):** Identifying underlying behavioral trends and turnover patterns across demographics.
- **Feature Engineering:** Implementing scaling pipelines and categorical encoding techniques.
- **Machine Learning Model Development:** Structuring classification models to handle target variable imbalances.
- **Model Evaluation:** Balancing structural accuracy with recall metrics for business-critical tracking.
- **Explainable AI Concepts:** Interpreting coefficient weight distribution to extract real-world feature importances.
- **Streamlit Deployment:** Building interactive user interfaces to bridge data models with non-technical stakeholders.
- **Business-Oriented Analytics:** Translating abstract statistical models into prescriptive operational directives.

---

## 🔮 Future Enhancements

- **PDF Report Generation:** Automated exporting of full-scale diagnostic slide decks and administrative reports.
- **Advanced Explainable AI (SHAP):** Integrating SHAP values for granular, feature-by-feature prediction explanations.
- **Real-Time Employee Monitoring Dashboard:** Continuous pipeline telemetry ingestion for real-time risk scoring.
- **Department-Level Attrition Forecasting:** Time-series analysis to model macro-level retention rates over seasonal quarters.
- **Cloud Deployment:** Migrating backend configurations to secure, containerized enterprise cloud environments.

---

## 👨‍💻 Author

*Sphurthhi Pudupakam* Aspiring Data Analyst | Machine Learning Enthusiast  

*GitHub:* [https://github.com/Sphurrthinaaidu-09](https://github.com/Sphurrthinaaidu-09)
