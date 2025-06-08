
# 🧠 IBM HR Employee Attrition Dashboard

An interactive and explainable HR analytics dashboard built with **Python**, **Streamlit**, **Seaborn**, and **Scikit-learn**, using the IBM HR Employee Attrition dataset.

This app helps visualize, analyze, and understand the **patterns behind employee attrition**, training gaps, compensation trends, and satisfaction scores — complete with a machine learning-based **feature importance breakdown** for identifying key attrition drivers.

---

## 📬 Author

**Gbenga Kajola**

[LinkedIn](https://www.linkedin.com/in/kajolagbenga)

[Certified_Data_Scientist](https://www.datacamp.com/certificate/DSA0012312825030)

[Certified_Data_Analyst](https://www.datacamp.com/certificate/DAA0018583322187)

[Certified_SQL_Database_Programmer](https://www.datacamp.com/certificate/SQA0019722049554)

---

## 📌 Key Features

### 📊 Visual Dashboards
- **Overview Section**
  - Attrition count by department, gender, and job role
  - Age distribution comparison with attrition overlay

- **Training & Development**
  - Training hours comparison by department and attrition status

- **Compensation Analysis**
  - Monthly income and salary hikes vs. attrition
  - Department-level compensation comparison

- **Job Satisfaction & Work-Life**
  - Insightful boxplots comparing satisfaction metrics with attrition

- **Key Drivers of Attrition**
  - ML-powered (Random Forest) analysis of top 10 features influencing attrition

---

## 🧰 Technologies Used

| Tool | Role |
|------|------|
| **Python** | Core programming |
| **Pandas** | Data manipulation |
| **Streamlit** | Interactive web UI |
| **Seaborn / Matplotlib** | Visualizations |
| **Scikit-learn** | ML model for feature importance |
| **LabelEncoder** | Encoding categorical variables |

---

## 🗂 File Overview

```
📁 IBM HR Attrition Analytics Streamlit Dashboard/
├── IBM-HR-Employee-Attrition.csv     # Dataset used
├── attrition.py                   # Main Streamlit app script
├── insights.py                   # Jupyter Notebook
├── requirements.txt                   # Installation of Dependencies
├── README.md                         # Project documentation
```

---

## ▶️ How to Run

1. **Install dependencies**:

```bash
pip install streamlit pandas matplotlib seaborn scikit-learn
```

2. **Run the app**:

```bash
streamlit run attrition.py
```

---

## 📤 Downloadable Reports

- Users can download:
  - The full HR dataset
  - The top 10 attrition feature importances (CSV)

---

## 💡 Insights Enabled

- Which departments or job roles are most prone to attrition?
- How do salary and training influence resignation?
- What workplace satisfaction metrics correlate with attrition?
- What features (age, income, training, etc.) are key attrition drivers?

---

## 📬 Author

**Gbenga Kajola**  
Certified Data Scientist & HR Analytics Practitioner  
[LinkedIn →](https://www.linkedin.com/in/kajolagbenga)

---

## 📜 License

This project is open source and free to use under the MIT License.
