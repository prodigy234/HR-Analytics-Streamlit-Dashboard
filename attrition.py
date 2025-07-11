import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io

def load_data():
    return pd.read_csv("IBM-HR-Employee-Attrition.csv")

def download_button(dataframe, filename, label):
    csv = dataframe.to_csv(index=False).encode('utf-8')
    st.download_button(label=label, data=csv, file_name=filename, mime='text/csv')

def plot_to_streamlit(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    st.image(buf)


def overview_dashboard(df):
    st.subheader("1. Attrition Overview")

    # Attrition Count
    fig1, ax1 = plt.subplots(figsize=(10, 6))  # wider plot
    sns.countplot(data=df, x='Attrition', palette='Set2', ax=ax1)
    ax1.set_title('Overall Attrition Count')
    ax1.set_xlabel("Attrition")
    ax1.set_ylabel("Their Count")
    plt.xticks(rotation=30, ha='right')  # rotate for readability
    fig1.tight_layout()
    plot_to_streamlit(fig1)

    # Attrition by Department -
    fig2, ax2 = plt.subplots(figsize=(10, 6))  # wider plot
    sns.countplot(data=df, x='Department', hue='Attrition', palette='Set1', ax=ax2)
    ax2.set_title('Attrition by Department')
    ax2.set_xlabel("Department")
    ax2.set_ylabel("Their Count")
    plt.xticks(rotation=30, ha='right')  # rotate for readability
    fig2.tight_layout()
    plot_to_streamlit(fig2)

    # Attrition by Gender
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df, x='Gender', hue='Attrition', palette='coolwarm', ax=ax3)
    ax3.set_title('Attrition by Gender')
    ax3.set_xlabel("Gender")
    ax3.set_ylabel("Their Count")
    plt.xticks(rotation=30, ha='right')  # rotate for readability
    fig3.tight_layout()
    plot_to_streamlit(fig3)

    # Attrition by Job Role
    fig4, ax4 = plt.subplots(figsize=(12, 8))  # Bigger for clarity
    sns.countplot(data=df, y='JobRole', hue='Attrition', palette='viridis', ax=ax4)
    ax4.set_title('Attrition by Job Role')
    ax4.set_xlabel("Count")
    ax4.set_ylabel("Job Role")
    fig4.tight_layout()
    plot_to_streamlit(fig4)

    # Age Distribution with Attrition Overlay
    fig5, ax5 = plt.subplots(figsize=(10, 6))  # wider plot
    sns.histplot(data=df, x='Age', hue='Attrition', multiple='stack', bins=20, palette='Set2', ax=ax5)
    ax5.set_title('Age Distribution with Attrition Overlay')
    plt.xticks(rotation=30, ha='right')  # rotate for readability
    fig5.tight_layout()
    plot_to_streamlit(fig5)


def training_dashboard(df):
    st.subheader("2. Training & Development")

    # Training Times vs Attrition
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='Attrition', y='TrainingTimesLastYear', palette='coolwarm', ax=ax)
    ax.set_title('Training Times Last Year vs Attrition')
    ax.set_xlabel("Attribution")
    ax.set_ylabel("Training Times Last Year")
    plt.xticks(rotation=30, ha='right')  # rotate for readability
    fig.tight_layout()
    plot_to_streamlit(fig)

    # Training by Department
    fig2, ax2 = plt.subplots(figsize=(10, 6))  # wider plot
    sns.boxplot(data=df, x='Department', y='TrainingTimesLastYear', palette='Set2', ax=ax2)
    ax2.set_title('Training by Department')
    ax2.set_xlabel("Department")
    ax2.set_ylabel("Training Hours Last Year")
    plt.xticks(rotation=30, ha='right')  # rotate for readability
    fig2.tight_layout()
    plot_to_streamlit(fig2)


def compensation_dashboard(df):
    st.subheader("3. Compensation Analysis")

    # Monthly Income by Attrition
    fig, ax = plt.subplots(figsize=(10, 6))  # wider plot
    sns.boxplot(data=df, x='Attrition', y='MonthlyIncome', palette='coolwarm', ax=ax)
    ax.set_title('Monthly Income vs Attrition')
    ax.set_xlabel("Attrition")
    ax.set_ylabel("Monthly Income")
    plt.xticks(rotation=30, ha='right')  # rotate for readability
    fig.tight_layout()
    plot_to_streamlit(fig)

    # Monthly Income by Department
    fig2, ax2 = plt.subplots(figsize=(10, 6))  # wider plot
    sns.boxplot(data=df, x='Department', y='MonthlyIncome', palette='Set3', ax=ax2)
    ax2.set_title('Monthly Income by Department')
    ax2.set_xlabel("Department")
    ax2.set_ylabel("Their Monthly Income")
    plt.xticks(rotation=30, ha='right')  # rotate for readability
    fig2.tight_layout()
    plot_to_streamlit(fig2)

    # PercentSalaryHike by Attrition
    fig3, ax3 = plt.subplots(figsize=(10, 6))  # wider plot
    sns.boxplot(data=df, x='Attrition', y='PercentSalaryHike', palette='Set1', ax=ax3)
    ax3.set_title('Percent Salary Hike vs Attrition')
    ax3.set_xlabel("Attrition")
    ax3.set_ylabel("Percent Salary Hike")
    plt.xticks(rotation=30, ha='right')  # rotate for readability
    fig3.tight_layout()
    plot_to_streamlit(fig3)

# def satisfaction_dashboard(df):
#     st.subheader("4. Job Satisfaction & Work-Life Balance")

#     metrics = ['JobSatisfaction', 'EnvironmentSatisfaction', 'WorkLifeBalance', 'RelationshipSatisfaction']
#     for metric in metrics:
#         fig, ax = plt.subplots(figsize=(10, 6))  # wider plot
#         sns.boxplot(data=df, x='Attrition', y=metric, palette='Set2', ax=ax)
#         ax.set_title(f'{metric} vs Attrition')
#         plt.xticks(rotation=30, ha='right')  # rotate for readability
#         fig.tight_layout()
#         plot_to_streamlit(fig)


    
def satisfaction_dashboard(df):
    st.subheader("4. Job Satisfaction & Work-Life Balance")

    # Mapping from technical column names to readable labels
    metric_labels = {
            'JobSatisfaction': 'Job Satisfaction',
            'EnvironmentSatisfaction': 'Environment Satisfaction',
            'WorkLifeBalance': 'Work-Life Balance',
            'RelationshipSatisfaction': 'Relationship Satisfaction'
    }

    for metric, label in metric_labels.items():
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=df, x='Attrition', y=metric, palette='Set2', ax=ax)
        ax.set_title(f'{label} vs Attrition')
        ax.set_xlabel("Attrition")
        ax.set_ylabel(label)
        plt.xticks(rotation=30, ha='right')
        fig.tight_layout()
        plot_to_streamlit(fig)



def key_drivers_dashboard(df):
    st.subheader("5. Key Drivers of Attrition")

    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import LabelEncoder

    df_encoded = df.copy()
    le = LabelEncoder()
    for col in df_encoded.select_dtypes(include='object').columns:
        df_encoded[col] = le.fit_transform(df_encoded[col])

    X = df_encoded.drop(['Attrition', 'EmployeeNumber', 'Over18', 'StandardHours', 'EmployeeCount'], axis=1)
    y = df_encoded['Attrition']

    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    importances = pd.DataFrame({'Feature': X.columns, 'Importance': model.feature_importances_})
    importances = importances.sort_values(by='Importance', ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=importances, y='Feature', x='Importance', palette='crest', ax=ax)
    ax.set_title('Top 10 Features Influencing Attrition')
    fig.tight_layout()
    plot_to_streamlit(fig)

    download_button(importances, 'key_attrition_drivers.csv', 'Download Key Drivers Data')


def main():
    st.title("IBM HR Employee Attrition Dashboard")
    df = load_data()

    with st.sidebar:
        section = st.radio("Select Dashboard Section", [
            "Overview", "Training & Development", "Compensation", "Satisfaction", "Key Drivers"
        ])

    if section == "Overview":
        overview_dashboard(df)
    elif section == "Training & Development":
        training_dashboard(df)
    elif section == "Compensation":
        compensation_dashboard(df)
    elif section == "Satisfaction":
        satisfaction_dashboard(df)
    elif section == "Key Drivers":
        key_drivers_dashboard(df)

    st.markdown("---")
    download_button(df, "full_hr_data.csv", "Download Full Dataset")
    
    # Footer
    st.markdown("---")
    st.markdown("# About the Developer")
    # Display developer image
    st.image("my_image.jpg", width=150)
    st.markdown("## **Kajola Gbenga**")

    st.markdown(
        """
    📇 Certified Data Analyst | Certified Data Scientist | Certified SQL Programmer | Mobile App Developer | AI/ML Engineer

    🔗 [LinkedIn](https://www.linkedin.com/in/kajolagbenga)  
    📜 [View My Certifications & Licences](https://www.datacamp.com/portfolio/kgbenga234)  
    💻 [GitHub](https://github.com/prodigy234)  
    🌐 [Portfolio](https://kajolagbenga.netlify.app/)  
    📧 k.gbenga234@gmail.com
    """
    )


    st.markdown("✅ Created using Python and Streamlit")


if __name__ == '__main__':
    main()