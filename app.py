import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
import io

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & ENTERPRISE THEMING
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Workforce Analytics & Attrition Intelligence System",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS injection for sleek corporate cards, responsive tables, and status highlights
st.markdown("""
<style>
    div[data-testid="stMetricValue"] { font-size: 28px; font-weight: 700; color: #1E3A8A; }
    .metric-card { background-color: #F8FAFC; padding: 20px; border-radius: 10px; border-left: 5px solid #3B82F6; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .recommendation-card { background-color: #FFFFFF; padding: 20px; border-radius: 8px; border: 1px solid #E2E8F0; border-top: 4px solid #10B981; margin-bottom: 15px; }
    .driver-card { background-color: #FFFBEB; padding: 15px; border-radius: 8px; border-left: 4px solid #F59E0B; margin-bottom: 10px; }
    .stButton>button { width: 100%; border-radius: 6px; }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. CORE MACHINE LEARNING CORE (YOUR EXACT BUSINESS LOGIC PIPELINE)
# -----------------------------------------------------------------------------
class AttritionFallbackModel:
    def predict_deterministic(self, row_dict):
        """Generates a realistic, reactive risk score based on telemetry markers"""
        base_risk = 15.0
        
        # Standardizing keys to safely handle both form inputs and CSV column names
        ot_val = str(row_dict.get('OverTime', row_dict.get('overtime', 'No'))).strip().lower()
        if ot_val == 'yes' or row_dict.get('OverTime_Yes') == 1:
            base_risk += 35.0
            
        if float(row_dict.get('JobSatisfaction', row_dict.get('jobsatisfaction', 3))) <= 2:
            base_risk += 20.0
            
        if float(row_dict.get('WorkLifeBalance', row_dict.get('worklifebalance', 3))) <= 2:
            base_risk += 15.0
            
        if float(row_dict.get('YearsInCurrentRole', row_dict.get('yearsincurrentrole', 3))) < 1:
            base_risk += 10.0
            
        if float(row_dict.get('MonthlyIncome', row_dict.get('monthlyincome', 6000))) < 4000:
            base_risk += 12.0
            
        # Add slight structural variance and clip between baseline boundaries
        age_seed = str(row_dict.get('Age', row_dict.get('age', '30'))).strip()
        try:
            np.random.seed(int(float(age_seed)))
        except ValueError:
            np.random.seed(30)
            
        base_risk += np.random.uniform(-4, 4)
        return float(np.clip(base_risk, 5.0, 98.5))

model = AttritionFallbackModel()

# -----------------------------------------------------------------------------
# 3. INITIALIZING SYSTEM STATE STORAGE
# -----------------------------------------------------------------------------
if "dataset" not in st.session_state:
    st.session_state.dataset = pd.DataFrame() # Holds processed CSV inputs
if "is_analyzed" not in st.session_state:
    st.session_state.is_analyzed = False
if "uploaded_file_cache" not in st.session_state:
    st.session_state.uploaded_file_cache = None

# -----------------------------------------------------------------------------
# 4. SIDEBAR SELECTION SYSTEM
# -----------------------------------------------------------------------------
st.sidebar.title("🏢 Workforce Analytics")
st.sidebar.markdown("---")

# Dynamic navigation management based on whether data has been compiled
nav_options = ["🏠 Executive Dashboard", "📂 Data Upload Center"]
if st.session_state.is_analyzed and not st.session_state.dataset.empty:
    nav_options.extend([
        "📊 Workforce Analytics",
        "🎯 Attrition Drivers",
        "👥 Employee Explorer",
        "💡 HR Action Plan",
        "📤 Export Center"
    ])
nav_options.append("🔮 Scenario Simulator") # Always accessible for test cases

navigation = st.sidebar.radio("Application Modules", nav_options)

st.sidebar.markdown("---")
st.sidebar.info(
    "**System Status:** Operational\n\n"
    "**Model Engine:** Balanced Deterministic Pipeline\n\n"
    f"**Data Hydrated:** {'Yes' if st.session_state.is_analyzed else 'No (Waiting for CSV)'}"
)

# -----------------------------------------------------------------------------
# MODULE 1: EXECUTIVE DASHBOARD
# -----------------------------------------------------------------------------
if navigation == "🏠 Executive Dashboard":
    st.title("📊 Employee Attrition Risk Prediction & Workforce Analytics")
    st.markdown("Transforming raw organizational workforce matrices into structured, proactive retention insights.")
    
    if st.session_state.is_analyzed and not st.session_state.dataset.empty:
        df = st.session_state.dataset
        
        # Primary Business KPIs
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Total Workforce Tracked", f"{len(df)} Headcount")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            high_risk_count = len(df[df["Risk_Category"] == "High Risk"])
            st.markdown('<div class="metric-card" style="border-left-color: #EF4444;">', unsafe_allow_html=True)
            st.metric("High-Risk Watchlist", f"{high_risk_count} Employees", f"{(high_risk_count/len(df))*100:.1f}% Share")
            st.markdown('</div>', unsafe_allow_html=True)
        with col3:
            avg_risk = df["Attrition_Risk_Percentage"].mean()
            st.markdown('<div class="metric-card" style="border-left-color: #F59E0B;">', unsafe_allow_html=True)
            st.metric("Average Attrition Risk", f"{avg_risk:.1f}%")
            st.markdown('</div>', unsafe_allow_html=True)
        with col4:
            if 'OverTime' in df.columns:
                ot_pct = (len(df[df["OverTime"].astype(str).str.lower() == 'yes']) / len(df)) * 100
                lbl = "Overtime Utilization"
            else:
                ot_pct = 0.0
                lbl = "Overtime Column Missing"
            st.markdown('<div class="metric-card" style="border-left-color: #8B5CF6;">', unsafe_allow_html=True)
            st.metric(lbl, f"{ot_pct:.1f}%")
            st.markdown('</div>', unsafe_allow_html=True)
            
        st.markdown("### 🔍 Automated Core Insights")
        
        # Evaluating processing rules directly from your original Flask logic
        insights = []
        if 'Department' in df.columns:
            dept_stats = df.groupby('Department')['Attrition_Risk_Percentage'].mean().to_dict()
            max_dept = max(dept_stats, key=dept_stats.get)
            if dept_stats[max_dept] > 25:
                insights.append(f"🏢 **{max_dept}** department shows higher relative attrition risk parameters ({dept_stats[max_dept]:.1f}%). Consider monitoring operational metrics closely.")
        
        if 'OverTime' in df.columns:
            ot_high = df[df['OverTime'].astype(str).str.lower() == 'yes']['Attrition_Risk_Percentage'].mean()
            ot_low = df[df['OverTime'].astype(str).str.lower() == 'no']['Attrition_Risk_Percentage'].mean()
            if ot_high > (ot_low * 1.3):
                insights.append("🔥 **Overtime Impact Identified:** Employees assigned to structured OverTime metrics demonstrate a significantly higher overall baseline attrition probability.")
                
        if not insights:
            st.success("✅ Workforce parameters show stable trends across default tracks. Continue regular monitoring intervals.")
        else:
            for insight in insights:
                st.warning(insight)
                
        if 'Department' in df.columns:
            st.markdown("### Department Risk Velocity Matrix")
            fig_dept = px.bar(df.groupby('Department')['Attrition_Risk_Percentage'].mean().reset_index(), 
                              x='Department', y='Attrition_Risk_Percentage', color='Department',
                              title="Mean Attrition Risk Percentage Across Departments",
                              labels={'Attrition_Risk_Percentage': 'Mean Risk Score (%)'})
            st.plotly_chart(fig_dept, use_container_width=True)
            
    else:
        st.info("💡 Welcome to the Workforce Analytics Dashboard. To visualize system metrics, please navigate to the **📂 Data Upload Center** on the sidebar and submit an active CSV asset.")

# -----------------------------------------------------------------------------
# MODULE 2: DATA UPLOAD CENTER
# -----------------------------------------------------------------------------
elif navigation == "📂 Data Upload Center":
    st.title("📂 Enterprise Data Ingestion Gateway")
    st.markdown("Submit raw transactional organizational spreadsheets to run global cohort evaluations.")
    
    uploaded_file = st.file_uploader("Ingest Workforce Dataset Ledger", type=["csv"])
    
    if uploaded_file is not None:
        st.session_state.uploaded_file_cache = uploaded_file
        
        # Previewing structural dataframe assets
        try:
            df_preview = pd.read_csv(uploaded_file)
            st.success("✔ Document structural signature identified successfully.")
            
            # 3. Data Validation Center block layout
            st.markdown("### 🧹 Structural Integrity Check")
            v_col1, v_col2 = st.columns(2)
            with v_col1:
                st.markdown(f"- **Total Rows Detected:** `{len(df_preview)}` records")
                st.markdown(f"- **Missing Value Inclusions:** `{df_preview.isnull().sum().sum()}` data blocks")
            with v_col2:
                has_emp_id = 'EmployeeID' in df_preview.columns or 'employeeid' in df_preview.columns
                st.markdown(f"- **EmployeeID Token Column Found:** `{'Yes' if has_emp_id else 'No (Will automatically generate)'}`")
                
            st.markdown("### Preview Submissions File Matrix")
            st.dataframe(df_preview.head(5), use_container_width=True)
            
            # Execution button maps back into your processing loops
            if st.button("Initialize Transformation Engine", type="primary"):
                st.markdown("---")
                st.markdown("### 🤖 ML Inference Runtime Pipelines")
                
                # Executing automated steps layout
                progress_bar = st.progress(0)
                status_text = st.empty()
                steps = [
                    "Parsing validation checkpoints...", 
                    "Mapping row parameters into input schemas...", 
                    "Calculating localized coefficient distributions...", 
                    "Hydrating core dashboard visualization assets..."
                ]
                for idx, text in enumerate(steps):
                    status_text.text(f"⚙️ Running Phase {idx+1}/4: {text}")
                    progress_bar.progress((idx + 1) * 25)
                    time.sleep(0.4)
                
                # Running your exact looping predictive core logic
                df_processed = df_preview.copy()
                if 'EmployeeID' not in df_processed.columns:
                    df_processed['EmployeeID'] = [f"EMP-{1000 + i}" for i in range(len(df_processed))]
                
                probabilities = []
                for _, row in df_processed.iterrows():
                    probabilities.append(model.predict_deterministic(row.to_dict()))
                    
                df_processed['Attrition_Risk_Percentage'] = np.round(probabilities, 2)
                df_processed['Risk_Category'] = pd.cut(df_processed['Attrition_Risk_Percentage'], 
                                             bins=[0, 30, 70, 100], 
                                             labels=['Low Risk', 'Moderate Risk', 'High Risk'], 
                                             include_lowest=True)
                
                st.session_state.dataset = df_processed
                st.session_state.is_analyzed = True
                status_text.empty()
                st.success("🚀 System computations completed. Analytics modules are fully unlocked on the sidebar navigation loop.")
                
        except Exception as e:
            st.error(f"Error parsing data configuration asset: {str(e)}")
            
    else:
        st.info("System is waiting for a local `.csv` transaction file asset target.")

# -----------------------------------------------------------------------------
# MODULE 3: WORKFORCE ANALYTICS
# -----------------------------------------------------------------------------
elif navigation == "📊 Workforce Analytics":
    st.title("📊 Workforce Risk Spread Distributions")
    df = st.session_state.dataset
    
    col1, col2 = st.columns([4, 6])
    with col1:
        st.markdown("### Risk Tier Metrics Breakdown")
        low_c = int((df['Risk_Category'] == 'Low Risk').sum())
        med_c = int((df['Risk_Category'] == 'Moderate Risk').sum())
        high_c = int((df['Risk_Category'] == 'High Risk').sum())
        
        st.markdown(f"""
        - 🟢 **Low Risk Profiles:** `{low_c}` Employees
        - 🟡 **Moderate Risk Profiles:** `{med_c}` Employees
        - 🔴 **High Risk Profiles:** `{high_c}` Employees
        """)
        
        risk_counts = df["Risk_Category"].value_counts().reset_index()
        risk_counts.columns = ["Risk Tier", "Headcount"]
        fig_pie = px.pie(risk_counts, values="Headcount", names="Risk Tier",
                         color="Risk Tier",
                         color_discrete_map={"Low Risk":"#10B981", "Moderate Risk":"#F59E0B", "High Risk":"#EF4444"},
                         hole=0.45)
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col2:
        st.markdown("### Continuous Risk Curve Density")
        fig_hist = px.histogram(df, x="Attrition_Risk_Percentage", nbins=20,
                                title="Frequency of Employee Profiles across Risk Spectrum Metrics",
                                color_discrete_sequence=["#1E3A8A"])
        st.plotly_chart(fig_hist, use_container_width=True)

# -----------------------------------------------------------------------------
# MODULE 4: ATTRITION DRIVERS
# -----------------------------------------------------------------------------
elif navigation == "🎯 Attrition Drivers":
    st.title("🎯 Statistical Structural Drivers Matrix")
    st.markdown("Identified parameters matching the logic bounds of your deterministic modeling architecture.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="driver-card">
            <strong>🔥 Overtime Assignments</strong><br>
            Injects an immediate <strong>+35.0% risk index jump</strong> directly into profile tracking parameters.
        </div>
        <div class="driver-card" style="border-left-color: #EF4444;">
            <strong>📉 Weak Job Satisfaction Logs</strong><br>
            Satisfaction records scored &le; 2 introduce an additional <strong>+20.0% probability value</strong>.
        </div>
        <div class="driver-card" style="border-left-color: #10B981;">
            <strong>⚖ Restricted Work-Life Balance Indexes</strong><br>
            Balance scores falling &le; 2 scale risk outputs up by a fixed <strong>+15.0% margin</strong>.
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="driver-card" style="border-left-color: #8B5CF6;">
            <strong>💼 Tenure Vulnerabilities</strong><br>
            Staff with less than 1 single year in their current position add a <strong>+10.0% variance step</strong>.
        </div>
        <div class="driver-card" style="border-left-color: #3B82F6;">
            <strong>💰 Entry-Level Financial Bands</strong><br>
            Monthly earnings failing to meet a $4,000 baseline threshold flag a <strong>+12.0% evaluation check</strong>.
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# MODULE 5: EMPLOYEE EXPLORER
# -----------------------------------------------------------------------------
elif navigation == "👥 Employee Explorer":
    st.title("👥 High-Risk Watchlist Database Center")
    df = st.session_state.dataset
    
    st.markdown("### Top 10 High Priority Retention Priority Tracking Rows")
    top_ten = df.sort_values(by='Attrition_Risk_Percentage', ascending=False).head(10)
    
    # Building out dynamic views based on column availabilities
    core_cols = ['EmployeeID', 'Attrition_Risk_Percentage', 'Risk_Category']
    for extra in ['Department', 'JobRole', 'OverTime', 'MonthlyIncome']:
        if extra in df.columns:
            core_cols.append(extra)
            
    st.dataframe(top_ten[core_cols], use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### Global Profile Database Registry")
    st.dataframe(df[core_cols], use_container_width=True, hide_index=True)

# -----------------------------------------------------------------------------
# MODULE 6: HR ACTION PLAN
# -----------------------------------------------------------------------------
elif navigation == "💡 HR Action Plan":
    st.title("💡 Strategic AI HR Interventions & Action Blueprints")
    
    st.markdown("""
    <div class="recommendation-card">
        <h4>💡 Remediation Blueprint #1: Mitigate Critical Overtime Risk Paths</h4>
        <strong>Trigger Core:</strong> Active OverTime flag inputs.<br>
        <strong>Operational Mandate:</strong> Establish automated management thresholds to limit excessive overtime tracking items. Restructure shift logs to minimize attrition escalations.
    </div>
    
    <div class="recommendation-card" style="border-top-color: #F59E0B;">
        <h4>💡 Remediation Blueprint #2: Target Satisfaction Drop-off Zones</h4>
        <strong>Trigger Core:</strong> Engagement evaluations scored &le; 2.<br>
        <strong>Operational Mandate:</strong> Initiate structured environmental wellness checks and role alignments to intercept operational drops before resignation milestones.
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# MODULE 7: EXPORT CENTER
# -----------------------------------------------------------------------------
elif navigation == "📤 Export Center":
    st.title("📤 Data Asset Report Generation Hub")
    df = st.session_state.dataset
    
    buffer = io.BytesIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)
    
    st.markdown("### Final Document Matrix Summary Compilation")
    st.write("Extract complete validated predictions containing calculated risk factors, classification tags, and organizational parameters.")
    
    st.download_button(
        label="⬇ Download Comprehensive Attrition Risk Report (.CSV)",
        data=buffer,
        file_name="Attrition_Risk_Report.csv",
        mime="text/csv"
    )

# -----------------------------------------------------------------------------
# MODULE 8: SCENARIO SIMULATOR (YOUR SINGLE LOGIC FLASK REPLICA)
# -----------------------------------------------------------------------------
elif navigation == "🔮 Scenario Simulator":
    st.title("🔮 Individual Employee Scenario Simulator Tracker")
    st.markdown("Simulates risk velocity markers for unique profile assessments using your fallback algorithmic logic rules.")
    
    sim_col1, sim_col2 = st.columns([4, 6])
    with sim_col1:
        st.markdown("### Employee Attributes Simulation Panel")
        s_id = st.text_input("Employee Tracking Identity", value="EMP-0842")
        s_age = st.slider("Employee Age Interval", 18, 65, 30)
        s_ot = st.radio("Overtime Shift Allocations", ["Yes", "No"], index=1)
        s_satisfaction = st.slider("Job Satisfaction Rating Index", 1, 4, 3)
        s_wlb = st.slider("Work-Life Balance Index", 1, 4, 3)
        s_role_years = st.slider("Years in Current Functional Role", 0, 15, 3)
        s_income = st.slider("Monthly Income Yield ($)", 2000, 15000, 6000)
        
    with sim_col2:
        st.markdown("### Risk Probability Pipeline Computations")
        
        # Creating dictionary to exactly mimic Flask form entries
        sim_payload = {
            'EmployeeID': s_id,
            'Age': s_age,
            'OverTime': s_ot,
            'JobSatisfaction': s_satisfaction,
            'WorkLifeBalance': s_wlb,
            'YearsInCurrentRole': s_role_years,
            'MonthlyIncome': s_income
        }
        
        prob = model.predict_deterministic(sim_payload)
        
        if prob < 30:
            status_text = "Low Risk"
            color_theme = "#10B981"
            st.success(f"🟢 Profile Verified: Employee classified as **{status_text}**")
        elif prob < 70:
            status_text = "Moderate Risk"
            color_theme = "#F59E0B"
            st.warning(f"🟡 Profile Verified: Employee classified as **{status_text}**")
        else:
            status_text = "High Risk"
            color_theme = "#EF4444"
            st.error(f"🔴 Profile Verified: Employee classified as **{status_text}**")
            
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = round(prob, 2),
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': f"Attrition Probability Gauge for {s_id}"},
            gauge = {
                'axis': {'range': [0, 100]},
                'bar': {'color': "#1E3A8A"},
                'steps': [
                    {'range': [0, 30], 'color': "#A7F3D0"},
                    {'range': [30, 70], 'color': "#FDE68A"},
                    {'range': [70, 100], 'color': "#FCA5A5"}
                ]
            }
        ))
        st.plotly_chart(fig_gauge, use_container_width=True)
