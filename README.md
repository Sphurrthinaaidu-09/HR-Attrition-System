# 📊 Employee Attrition Risk Prediction & Workforce Analytics System

An end-to-end HR Analytics and Machine Learning application designed to identify employee attrition risks before they occur. The system transforms raw workforce data into actionable business intelligence, enabling HR teams to proactively improve employee retention and workforce stability.

Live Demo: https://hr-attrition-system-yrornkdej7yze62bvyonpx.streamlit.app/

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

## 📸 Application Screenshots

<details>
<summary>📂 1. Enterprise Data Ingestion Gateway (Click to Expand)</summary>
<p align="center">
  <img src="https://github.com/user-attachments/assets/22689705-1e89-4251-866a-2cf6779b52ec" width="90%" alt="Enterprise Data Ingestion Gateway" style="border-radius: 8px;" />
</p>
<p align="justify">
  <strong>Data Upload Center:</strong> Supports raw transactional HR spreadsheet uploads with automated schema verification, data shape recognition, and structural integrity checks before pipeline ingestion.
</p>
</details>

<details>
<summary>📊 2. Employee Attrition Risk Prediction & Workforce Analytics (Click to Expand)</summary>
<p align="center">
  <img src="https://github.com/user-attachments/assets/68acf36b-8c50-4384-84b3-cec060a1b6c9" width="90%" alt="Employee Attrition Risk Prediction & Workforce Analytics" style="border-radius: 8px;" />
</p>
<p align="justify">
  <strong>Executive Dashboard:</strong> Serves as the central command center, aggregating high-level organizational matrices like total headcount, active high-risk watchlists, and overtime utilization metrics alongside automated core LLM insights.
</p>
</details>

<details>
<summary>📊 3. Workforce Risk Spread Distributions (Click to Expand)</summary>
<p align="center">
  <img src="https://github.com/user-attachments/assets/1de1d041-12c2-463b-9cb4-d6e060193ab7" width="90%" alt="Workforce Risk Spread Distributions" style="border-radius: 8px;" />
</p>
<p align="justify">
  <strong>Workforce Analytics Dashboard:</strong> Provides aggregate statistical visualizers charting risk tiers across low, moderate, and high risk populations alongside continuous attrition risk curve density charts.
</p>
</details>

<details>
<summary>🎯 4. Statistical Structural Drivers Matrix (Click to Expand)</summary>
<p align="center">
  <img src="https://github.com/user-attachments/assets/87228fe9-82ef-44a8-9059-b4397d31cd37" width="90%" alt="Statistical Structural Drivers Matrix" style="border-radius: 8px;" />
</p>
<p align="justify">
  <strong>Attrition Drivers Analysis:</strong> Exposes the underlying deterministic rules and logical weight bounds powering the risk evaluation engine (e.g., Overtime shifts, Job satisfaction limits, and tenure drop zones).
</p>
</details>

<details>
<summary>👥 5. High-Risk Watchlist Database Center (Click to Expand)</summary>
<p align="center">
  <img src="https://github.com/user-attachments/assets/4b877e12-22cc-44bc-956f-d0d24f063a70" width="90%" alt="High-Risk Watchlist Database Center" style="border-radius: 8px;" />
</p>
<p align="justify">
  <strong>Employee Explorer Matrix:</strong> A centralized granular tracking ledger highlighting the top priority high-risk retention targets filtered by risk percentage rankings and key organizational attributes.
</p>
</details>

<details>
<summary>💡 6. Strategic AI HR Interventions & Action Blueprints (Click to Expand)</summary>
<p align="center">
  <img src="https://github.com/user-attachments/assets/1ab1bfe7-ae67-420c-bc3a-dbd603531d42" width="90%" alt="Strategic AI HR Interventions & Action Blueprints" style="border-radius: 8px;" />
</p>
<p align="justify">
  <strong>HR Action Plan Panel:</strong> Generates context-triggered mitigation strategies and programmatic remediation paths responding directly to core active threat vectors like intense overtime demands or critical engagement dips.
</p>
</details>

<details>
<summary>💾 7. Data Asset Report Generation Hub (Click to Expand)</summary>
<p align="center">
  <img src="https://github.com/user-attachments/assets/e0671ce8-73cb-41c5-a17f-7687da5e7df7" width="90%" alt="Data Asset Report Generation Hub" style="border-radius: 8px;" />
</p>
<p align="justify">
  <strong>Export Center Terminal:</strong> Compiles calculated risk classification tags, priority rankings, and demographic indicators into structured, clean data matrices down-streamable via CSV format.
</p>
</details>

<details>
<summary>🔮 8. Individual Employee Scenario Simulator Tracker (Click to Expand)</summary>
<p align="center">
  <img src="https://github.com/user-attachments/assets/843b256e-81e5-49b9-8fef-914ef3fcf00f" width="90%" alt="Individual Employee Scenario Simulator Tracker" style="border-radius: 8px;" />
</p>
<p align="justify">
  <strong>What-If Scenario Simulator:</strong> Dynamic parameter interactive workbench with gauge metrics mapping out localized probability changes in real-time when testing alterations to age bands, overtime options, and balance levels.
</p>
</details>

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
