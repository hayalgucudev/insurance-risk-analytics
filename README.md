# 📊 Insurance Risk Analytics Project

## Overview

This project focuses on analyzing an insurance portfolio to understand risk patterns, profitability drivers, and pricing implications. The goal is to move from raw insurance data to actionable insights that support **risk-based pricing, underwriting decisions, and portfolio optimization**.

The project combines:
- Exploratory Data Analysis (EDA)
- Statistical Hypothesis Testing
- Machine Learning Modeling
- Explainable AI (SHAP)
- Data Version Control (DVC)

The final outcome is a reproducible analytics pipeline that identifies key risk drivers and predicts claim severity for insurance pricing strategies.

---

## 🧭 Business Objective

Insurance pricing must reflect actual risk. Flat pricing leads to:
- Underpricing high-risk customers
- Overpricing low-risk customers
- Reduced profitability and competitive disadvantage

This project aims to:
- Identify where risk is concentrated
- Test statistical differences in claims behavior
- Build predictive models for claim severity
- Support risk-based premium recommendations

---

## 📁 Project Structure
insurance-risk-analytics/
│
├── data/ # Raw and processed datasets (DVC tracked)
├── notebooks/
│ ├── 01_eda.ipynb # Data exploration and visualization
│ ├── 02_hypothesis_testing.ipynb # Statistical testing of risk drivers
│ ├── 03_modeling.ipynb # Machine learning models and evaluation
│
├── src/
│ ├── modeling/
│ │ ├── data_prep.py # Data loading and preprocessing
│ │ ├── models.py # Model training functions
│ │ ├── evaluation.py # Model evaluation metrics
│ │
│ ├── hypothesis/
│ ├── metrics.py # KPI definitions (frequency, severity, margin)
│ ├── tests.py # Statistical tests (t-test, chi-square)
│ ├── segmentation.py # Data grouping logic
│
├── .dvc/ # DVC configuration
├── requirements.txt
├── .gitignore
└── README.md


---

## 📊 Task 1 — Exploratory Data Analysis (EDA)

### Key Steps
- Data inspection and type validation
- Missing value analysis
- Duplicate detection
- Feature engineering (Loss Ratio, Margin)
- Distribution analysis (histograms, boxplots)
- Correlation analysis
- Geographic and categorical comparisons

### Key Insights
- Loss ratio varies significantly across provinces
- Certain vehicle types show consistently higher claim severity
- Claims and premiums show weak linear relationships, suggesting non-linearity
- Outliers exist in financial variables and must be handled carefully

---

## 🧪 Task 2 — Data Version Control (DVC)

DVC was implemented to ensure reproducibility and auditability.

### Setup
- Initialized DVC in project
- Configured local remote storage
- Tracked dataset versions using `.dvc` files

### Benefits
- Full data versioning
- Reproducible experiments
- Separation of code and data
- Supports audit-ready analytics pipelines

---

## 📉 Task 3 — Hypothesis Testing

Statistical testing was used to validate differences in risk across segments.

### Hypotheses Tested

| Hypothesis | Test | Result |
|------------|------|--------|
| Province differences in risk | t-test | Fail to reject |
| Gender vs Claim Frequency | Chi-square | Reject H₀ |
| Vehicle Type vs Claim Severity | t-test | Fail to reject |
| Zip Code vs Margin | t-test | Fail to reject |

### Key Findings

- Gender shows statistically significant differences in claim frequency
- Province and vehicle type differences exist but are not statistically strong in this dataset
- Margin differences across zip codes are not significant

---

## 🧠 Task 4 — Machine Learning Modeling

### Objective
Predict claim severity (`TotalClaims`) using regression models.

### Models Used
- Linear Regression (baseline)
- Random Forest (non-linear relationships)
- XGBoost (final optimized model)

### Evaluation Metrics
- RMSE (Root Mean Squared Error)
- R² Score

### Results Summary
- XGBoost performed best overall
- Random Forest captured non-linear patterns effectively
- Linear Regression underperformed due to model simplicity

### Feature Engineering
- TotalPremium
- CustomValueEstimate
- CapitalOutstanding

---

## 🔍 Model Explainability (SHAP)

SHAP analysis was used to interpret model predictions.

### Insights
- A small number of features dominate prediction behavior
- Relationships between features and claim severity are non-linear
- Financial and vehicle-related variables are the strongest predictors

### Business Impact
- Supports targeted premium adjustments
- Helps identify high-risk policy segments
- Improves underwriting transparency

---

## 💰 Business Recommendations

- Introduce **risk-based pricing** instead of flat premium structures
- Adjust pricing based on vehicle type and financial exposure
- Use predictive models for underwriting decisions
- Monitor gender-based differences in claim frequency
- Focus on high-risk segments for portfolio optimization

---

## 🛠️ Tools & Technologies

- Python (Pandas, NumPy, Scikit-learn)
- XGBoost
- SHAP (model interpretability)
- Matplotlib & Seaborn
- DVC (Data Version Control)
- Git & GitHub


##  How to Run the Project

### 1. Install dependencies

pip install -r requirements.txt

### 2. Run notebooks in order

1. notebooks/01_eda.ipynb
2. notebooks/02_hypothesis_testing.ipynb
3. notebooks/03_modeling.ipynb

## 3. (Optional) Restore data via DVC
dvc pull

## Limitations
Some missing values were imputed or removed
Model assumes historical patterns remain stable
External macroeconomic factors not included
Dataset imbalance may influence results

## Future Improvements
Add real-time pricing engine
Deploy model as API service
Improve feature engineering (policy duration, claim history)
Use deep learning for advanced risk modeling
Integrate external risk indicators (inflation, region risk indices)
# Conclusion

This project demonstrates a full insurance analytics pipeline from raw data exploration to predictive modeling and explainability. The findings support the transition toward data-driven, risk-based insurance pricing strategies.
The final XGBoost model provides a strong foundation for estimating claim severity and improving underwriting decisions.

## Author

Insurance Risk Analytics Project
Built as part of a structured data science workflow focusing on reproducibility, statistical rigor, and machine learning application in insurance systems.