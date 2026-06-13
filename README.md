# 📊 Employee Attrition Risk Prediction & Workforce Analytics System

An end-to-end HR Analytics and Machine Learning application designed to identify employee attrition risks before they occur. The system transforms raw workforce data into actionable business intelligence, enabling HR teams to proactively improve employee retention and workforce stability.

Live Demo: https://sphurrthi09-hr-attrition-system.hf.space

---

## 🚀 Project Overview

Employee attrition is one of the most expensive challenges faced by modern organizations. Replacing experienced employees increases recruitment costs, reduces productivity, and impacts team performance.

This project combines Machine Learning, Workforce Analytics, and Interactive Dashboards to help organizations:
- Predict employee attrition risk.
- Identify high-priority retention cases.
- Analyze workforce-wide risk patterns.
- Generate actionable HR recommendations.
- Support data-driven retention strategies.

The application functions as a complete HR Analytics Data Product rather than a standalone machine learning model.

---

## 🎯 Business Problem

Most organizations only react after employees resign.

This system helps HR teams shift from reactive workforce management to proactive retention planning by identifying employees who are likely to leave before attrition occurs.

---

## ⚙️ System Workflow

### 📥 Step 1: Data Ingestion
The platform supports two modes of analysis.

#### 👤 Individual Employee Assessment
HR managers can manually enter employee information such as:
- Age
- Monthly Income
- Overtime Status
- Job Satisfaction
- Work-Life Balance
- Years at Company
- Environment Satisfaction

The system instantly evaluates the employee's attrition risk profile.

#### 📁 Bulk Workforce Analysis
HR teams can upload an entire workforce dataset through a CSV file.

The application automatically processes all employee records and generates organization-wide risk intelligence.

---

### 🤖 Step 2: Machine Learning Prediction Engine
After data submission:
- Employee records are validated and transformed.
- Features are encoded and scaled.
- The trained Balanced Logistic Regression model performs prediction.
- Attrition probabilities are generated for every employee.

**Output:**
- Risk Probability (0–100%)
- Risk Category
- Workforce Risk Metrics

---

### 📊 Step 3: Executive Intelligence Dashboard
The prediction results are converted into business-friendly insights.

#### Risk Classification
Employees are automatically classified into:
- 🟢 Low Risk
- 🟡 Medium Risk
- 🔴 High Risk

#### Top 10 High-Risk Employee Watchlist
The system automatically identifies employees with the highest attrition probabilities. This allows HR teams to prioritize:
- Stay Interviews
- Retention Discussions
- Manager Interventions

#### Department-Level Risk Analysis
The application identifies:
- Departments with elevated attrition risk
- Workforce concentration of high-risk employees
- Organizational hotspots requiring attention

#### Workforce Risk Distribution
Interactive dashboards provide:
- Risk Distribution Charts
- Employee Count by Risk Category
- Organization-Wide Risk Metrics

---

### 💡 Step 4: Actionable Recommendations
The application does not stop at prediction. Based on identified risk factors, the system generates HR recommendations such as:
- Reduce excessive overtime
- Improve work-life balance
- Increase employee engagement
- Review compensation structures
- Strengthen career growth opportunities

This helps transform predictive insights into practical business actions.

---

### 📤 Step 5: Report Export
After analysis, users can:
- Export prediction results
- Download workforce risk reports
- Share findings with HR leadership

The exported report includes:
- Risk Scores
- Risk Categories
- Attrition Predictions

---

## 📂 Dataset

IBM HR Analytics Employee Attrition Dataset

### Dataset Statistics:
- **Employees:** 1,470
- **Original Features:** 35
- **Engineered Features:** 44+
- **Target Variable:** Attrition (Yes / No)

### Key Features
- Age
- Department
- Job Role
- Monthly Income
- Job Satisfaction
- Environment Satisfaction
- Work-Life Balance
- Overtime
- Marital Status
- Total Working Years
- Years at Company

---

## 🔍 Exploratory Data Analysis

Several workforce patterns were discovered.

### Key Insights
- ✅ Employees working overtime were significantly more likely to leave.
- ✅ Employees with low job satisfaction demonstrated higher attrition rates.
- ✅ Single employees showed higher attrition tendencies.
- ✅ Certain departments exhibited elevated workforce risk.

### Visualizations
- Employee Attrition Distribution
- Department vs Attrition
- Overtime vs Attrition
- Job Satisfaction vs Attrition
- Feature Importance Analysis

---

## ⚙️ Data Preprocessing

### Data Cleaning
Removed:
- `EmployeeCount`
- `EmployeeNumber`
- `Over18`
- `StandardHours`

### Feature Engineering
- One-Hot Encoding
- Binary Target Encoding
- Feature Scaling using `StandardScaler`

### Final Dataset
- 44+ machine-learning-ready features

---

## 🤖 Machine Learning Models Evaluated

The following classification models were trained and compared:

1. **Logistic Regression:** Baseline classification model.
2. **Balanced Logistic Regression:** Implemented using `class_weight = "balanced"` to address class imbalance.
3. **Decision Tree Classifier:** Tree-based interpretable model.
4. **Random Forest Classifier:** Ensemble learning model.

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

Although Random Forest achieved higher accuracy, Balanced Logistic Regression provided better identification of attrition cases and offered greater explainability for HR decision-making.

---

## 🔑 Top Drivers of Attrition

The model identified several significant attrition drivers:
- Overtime
- Marital Status
- Business Travel Frequency
- Job Role
- Job Satisfaction
- Environment Satisfaction
- Performance Rating
- Technical Education Background
- Years in Current Role

---

## 🛠️ Technology Stack

- **Programming Language:** Python
- **Data Analytics:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn
- **Visualization:** Matplotlib
- **Model Persistence:** Joblib
- **Web Application:** Streamlit

---

## 📸 Application Screenshots

<img width="1763" height="1325" alt="Screenshot_13-6-2026_161754_sphurrthi09-hr-attrition-system hf space" src="https://github.com/user-attachments/assets/4a4db3d6-d75c-4f7e-987d-82eab7e7f50e" />

<img width="1763" height="844" alt="Screenshot_13-6-2026_161850_sphurrthi09-hr-attrition-system hf space" src="https://github.com/user-attachments/assets/33fd88af-97c8-4bc4-bde3-a4aef38c2ef9" />

<img width="1763" height="1661" alt="Screenshot_13-6-2026_161923_sphurrthi09-hr-attrition-system hf space" src="https://github.com/user-attachments/assets/ea0efd79-cca6-43a9-9a7c-f764ce938383" />

---

## 📁 Project Structure

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

## 🎓 Skills Demonstrated

Through this project, I gained and applied practical experience in:

- **Data Cleaning:** Identifying and removing non-informative tracking attributes to optimize baseline computational overhead.
- **Exploratory Data Analysis (EDA):** Extracting underlying workforce behavioral patterns and statistical retention trends across varied employee demographics.
- **Feature Engineering:** Building systematic data transformations, including categorical One-Hot Encoding and feature scaling via `StandardScaler`.
- **Machine Learning & Classification Modeling:** Implementing, optimizing, and evaluating multiple classification algorithms to successfully handle skewed class distributions.
- **Explainable AI:** Interpreting statistical model coefficients to unlock transparent, transparently auditable feature importances for operational safety.
- **Business & Workforce Analytics:** Translating abstract data metrics into core key performance indicators (KPIs) that direct organizational talent retention strategies.
- **Dashboard Development & Streamlit Deployment:** Designing an interactive, production-ready web workspace that surfaces complex models into intuitive software toolkits for business administrators.

---

## 🔮 Future Enhancements

- **SHAP-Based Explainability:** Integrating fine-grained SHAP (SHapley Additive exPlanations) visual plots for real-time, individual parameter impact breakdowns.
- **PDF Report Generation:** Engineering automated script utilities allowing HR executives to export comprehensive workforce risk summaries as local PDF documents.
- **Real-Time Workforce Monitoring:** Scaling continuous ingestion pipelines to capture day-to-day employee feedback signals for live risk recalculation.
- **Department-Level Attrition Forecasting:** Applying predictive time-series models to anticipate macro-level resignation numbers across upcoming business quarters.
- **Enterprise Cloud Deployment:** Migrating local application runtimes to secure, scalable, and isolated enterprise cloud platform environments.

---

## 👨‍💻 Author

**Sphurthhi Pudupakam** *Aspiring Data Analyst | Machine Learning Enthusiast* 
- **GitHub:** [https://github.com/Sphurrthinaaidu-09]
  
---

⭐ If you found this project useful, consider giving the repository a star!
