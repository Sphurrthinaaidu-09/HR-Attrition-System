from flask import Flask, render_template, request, send_file
import numpy as np
import joblib
import pandas as pd
import io
import os

app = Flask(__name__)

# Load Model Assets
try:
    model = joblib.load("attrition_model.pkl")
    feature_names = joblib.load("feature_names.pkl")
except FileNotFoundError:
    class DummyModel:
        def predict_proba(self, X): return np.array([[0.65, 0.35]])
    model = DummyModel()
    feature_names = ["Age", "MonthlyIncome", "PercentSalaryHike", "JobLevel", "YearsAtCompany", 
                     "YearsInCurrentRole", "DistanceFromHome", "JobSatisfaction", "EnvironmentSatisfaction", 
                     "WorkLifeBalance", "JobInvolvement", "StockOptionLevel", "TotalWorkingYears", 
                     "TrainingTimesLastYear", "Gender_Male", "MaritalStatus_Married", "MaritalStatus_Single", 
                     "OverTime_Yes", "BusinessTravel_Travel_Frequently", "BusinessTravel_Travel_Rarely", 
                     "Department_Research & Development", "Department_Sales"]

def process_input_row(row_dict):
    """ Helper to transform raw key-values to match model feature matrix shape """
    data = dict.fromkeys(feature_names, 0)
    for k in feature_names:
        if k in row_dict:
            try: data[k] = float(row_dict[k])
            except: pass
            
    # Process Categoricals 
    if row_dict.get("Gender") == "Male": data["Gender_Male"] = 1
    m_status = row_dict.get("MaritalStatus")
    if m_status == "Married": data["MaritalStatus_Married"] = 1
    elif m_status == "Single": data["MaritalStatus_Single"] = 1
    if row_dict.get("OverTime") == "Yes": data["OverTime_Yes"] = 1
    if row_dict.get("BusinessTravel") == "Frequently": data["BusinessTravel_Travel_Frequently"] = 1
    else: data["BusinessTravel_Travel_Rarely"] = 1
    if row_dict.get("Department") == "R&D" or row_dict.get("Department") == "Research & Development": 
        data["Department_Research & Development"] = 1
    else: 
        data["Department_Sales"] = 1
        
    return [data[col] for col in feature_names]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Single Employee Evaluation Mode
    if 'Age' in request.form:
        form_data = {k: request.form.get(k) for k in request.form}
        vector = process_input_row(form_data)
        prob = model.predict_proba(np.array([vector]).reshape(1, -1))[0][1] * 100
        
        alert_class = "success" if prob < 30 else "warning" if prob < 70 else "danger"
        risk_status = "Low Risk" if prob < 30 else "Moderate Risk" if prob < 70 else "High Risk"
        
        return render_template('result.html', mode='single', probability=round(prob, 2), 
                               risk_status=risk_status, alert_class=alert_class,
                               overtime=form_data.get('OverTime'), job_satisfaction=int(form_data.get('JobSatisfaction', 3)),
                               work_life=int(form_data.get('WorkLifeBalance', 3)))

    # 2. Bulk CSV Assessment Upload Mode
    if 'csv_file' in request.files:
        file = request.files['csv_file']
        if not file.filename.endswith('.csv'):
            return "Please upload a valid CSV file.", 400
            
        df = pd.read_csv(file)
        
        # Create vectors for each row and generate predictions
        vectors = []
        for _, row in df.iterrows():
            vectors.append(process_input_row(row.to_dict()))
            
        probabilities = model.predict_proba(np.array(vectors))[:, 1] * 100
        df['Attrition_Risk_Percentage'] = np.round(probabilities, 2)
        
        # Categorize text bands for visualization summaries
        df['Risk_Category'] = pd.cut(df['Attrition_Risk_Percentage'], 
                                     bins=[0, 30, 70, 100], 
                                     labels=['Low Risk', 'Moderate Risk', 'High Risk'], 
                                     include_lowest=True)

        # Calculate high-level aggregate KPI metrics for charts
        low_count = int((df['Risk_Category'] == 'Low Risk').sum())
        mod_count = int((df['Risk_Category'] == 'Moderate Risk').sum())
        high_count = int((df['Risk_Category'] == 'High Risk').sum())
        
        global cached_bulk_results
        cached_bulk_results = df.copy()

        # Render output records directly as an HTML data grid table view
        table_records = df.head(10).to_dict(orient='records')
        
        return render_template('result.html', mode='bulk', records=table_records, 
                               total=len(df), low=low_count, mod=mod_count, high=high_count)

@app.route('/export')
def export_results():
    global cached_bulk_results
    if cached_bulk_results is None or cached_bulk_results.empty:
        return "No prediction assets available for export.", 400
    
    buffer = io.BytesIO()
    cached_bulk_results.to_csv(buffer, index=False)
    buffer.seek(0)
    
    return send_file(buffer, mimetype='text/csv', as_attachment=True, download_name='Attrition_Risk_Report.csv')

if __name__ == '__main__':
    cached_bulk_results = pd.DataFrame()
    app.run(debug=True)