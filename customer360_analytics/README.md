# 📊 Customer 360 Analytics & Machine Learning Pipeline

An end-to-end Data Science and Machine Learning project focused on **Customer Segmentation (K-Means)**, **Churn Prediction (Random Forest)**, and **Customer Lifetime Value (CLV) Forecasting (Linear Regression)**. The project features an interactive **Customer 360 Analytics API Engine** and dynamic analytical dashboard visualizations.

---

## 🚀 Key Features

* **Customer Segmentation (K-Means Clustering):** Categorizes customers into distinct clusters using purchase history and account age (`Account_Age_Days`, `Total_Orders`, `Average_Order_Value`).
* **Churn Risk Prediction:** Predicts high-risk customers likely to churn using machine learning algorithms.
* **CLV Forecasting:** Forecasts expected Customer Lifetime Value for the upcoming year using regression techniques.
* **Customer 360 API Engine:** Master query function `get_customer_360_analytics()` to fetch customer profile, churn risk, and value predictions in real time.
* **Analytical Dashboard:** Multi-panel visual insights (Cluster distribution, spend status, age vs. CLV).

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Data Processing:** `pandas`, `numpy`
* **Machine Learning & Analytics:** `scikit-learn` (StandardScaler, KMeans, RandomForestClassifier, LinearRegression)
* **Visualization:** `matplotlib`, `seaborn`
* **Environment:** VS Code / Jupyter Notebook

---

## 📂 Project Structure

```text
├── customer_analytics.csv              # Raw Dataset
├── customer_segmentation_analysis.ipynb # Complete Analytics & ML Notebook
└── README_Customer360.md               # Project Documentation
---

## 💡 Customer 360 API Usage Example

Query any customer ID using the master engine function:

```python
# API Call
get_customer_360_analytics("CUST-10002")
{
    "Customer ID": "CUST-10002",
    "Assigned Cluster": 3,
    "Churn Prediction": "High Risk of Churn",
    "Forecasted Next Year CLV": "$311.53"
}
---

## 📈 Visual Insights & Dashboard Summary

The dynamic analytical dashboard generates the following key visualizations and insights:

1. Customer Volume by Cluster (Bar Chart):
   * Shows the distribution and count of customers across different segmented clusters (e.g., Cluster 0 to Cluster 3).
   * Helps visualize segment population density to identify core customer bases.

2. Total Spend vs. Churn Risk (Box Plot / Bar Comparison):
   * Compares customer spending behaviors between High-Risk and Low-Risk churn segments.
   * Identifies spend thresholds that indicate potential customer attrition.

3. Account Age vs. Forecasted CLV (Scatter Plot):
   * Plots customer account tenure against forecasted Customer Lifetime Value across clusters.
   * Demonstrates how customer loyalty and account age impact long-term revenue predictions.
   ![Customer 360 Dashboard Insights](OUTOUT.png)
   ---

## ⚙️ How to Run

1. Open `customer_segmentation_analysis.ipynb` in Jupyter Notebook or VS Code.
2. Install required libraries:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn
   ```
3. Run all cells in the notebook to execute clustering, ML predictions, API tests, and charts
