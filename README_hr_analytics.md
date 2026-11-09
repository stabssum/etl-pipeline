# HR Analytics & Employee Attrition Prediction

An end-to-end Machine Learning project to analyze employee turnover, evaluate retention policies using A/B testing, and predict employee attrition using advanced classification models.

## 📌 Project Overview
Employee retention is a critical challenge for organizations. This project leverages HR data to identify key factors driving employee attrition, evaluate the effectiveness of retention programs via statistical testing, and build predictive models to flag high-risk employees before they leave.

---

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-Learn, XGBoost, Imbalanced-Learn (SMOTE), Seaborn, Matplotlib
* **Environment:** Jupyter Notebook / Visual Studio Code

---

## 📊 Key Steps & Methodology

1. **Data Preprocessing & Cleaning:**
   * Handled missing values, encoded categorical features, and scaled numerical variables.
   * Addressed class imbalance using **SMOTE (Synthetic Minority Over-sampling Technique)**.

2. **Statistical Analysis (A/B Testing):**
   * Performed **Chi-Square Tests** to evaluate whether specific retention group treatments significantly impact employee attrition rates.

3. **Machine Learning Classification:**
   * Built and evaluated **Random Forest** and **XGBoost** classifiers.
   * Utilized evaluation metrics including Classification Report, Precision-Recall, and **ROC-AUC Score**.

4. **Feature Importance & Insights:**
   * Visualized the top features influencing employee turnover using XGBoost feature importance scores.

5. **Risk Identification:**
   * Successfully filtered and identified high-risk employees from the test set for targeted HR interventions.

---

## 📈 Results & Key Findings
* **Model Performance:** The XGBoost model effectively classified high-risk retention candidates with optimized thresholding and SMOTE balancing.
* **Top Drivers:** Key features impacting employee attrition include specific retention treatment groups, job roles, marital status, and job satisfaction levels.
* **Actionable Output:** Generated a prioritized list of 28 high-risk employees requiring immediate HR engagement.

---

## 🚀 How to Run the Project
1. Clone the repository or download the project files.
2. Install the required dependencies:
   ```bash
   pip install pandas numpy scikit-learn xgboost imbalanced-learn seaborn matplotlib