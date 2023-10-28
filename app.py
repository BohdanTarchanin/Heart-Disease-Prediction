
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('heart.csv')

# App title and description
st.title("Heart Disease Dataset Analysis")
st.write(
    "This app provides an analysis of a dataset related to heart disease. "
    "You can view the dataset, its description, and some exploratory data analysis visuals below."
)

# Display part of the dataset
st.subheader("Sample Data")
st.write(data.head(10))

# Dataset information
st.subheader("Dataset Information")
st.write(
    "The dataset contains various medical metrics related to heart health, and the target variable suggests whether a patient has heart disease. "
    "Here's a description of the columns:"
)
column_descriptions = {
    "age": "Age of the patient.",
    "sex": "Gender of the patient (1 = male, 0 = female).",
    "cp": "Chest pain type.",
    "trestbps": "Resting blood pressure (in mm Hg).",
    "chol": "Serum cholesterol in mg/dl.",
    "fbs": "Fasting blood sugar (> 120 mg/dl, 1 = true; 0 = false).",
    "restecg": "Resting electrocardiographic results.",
    "thalach": "Maximum heart rate achieved.",
    "exang": "Exercise induced angina (1 = yes; 0 = no).",
    "oldpeak": "ST depression induced by exercise relative to rest.",
    "slope": "The slope of the peak exercise ST segment.",
    "ca": "Number of major vessels colored by fluoroscopy.",
    "thal": "Thalassemia (a blood disorder type).",
    "target": "Presence (1) or absence (0) of heart disease."
}
for column, desc in column_descriptions.items():
    st.write(f"- **{column}**: {desc}")

# Exploratory Data Analysis (EDA)

## Bar plot for target variable

# Setting up columns for plots
col1, col2 = st.columns(2)

col1.subheader("Heart Disease Presence")
col1.write("This plot shows the number of patients with and without heart disease.")
fig, ax = plt.subplots()
sns.countplot(data=data, x="target", ax=ax)
col1.pyplot(fig)

## Histogram for age
col2.subheader("Age Distribution")
col2.write("Histogram displaying the distribution of ages among patients.")
fig, ax = plt.subplots()
sns.histplot(data=data, x="age", kde=True, ax=ax)
col2.pyplot(fig)

## Pie chart for gender distribution
col1.subheader("Gender Distribution")
fig, ax = plt.subplots()
data['sex'].value_counts().plot.pie(explode=[0,0.1], labels=['Male', 'Female'], autopct='%1.1f%%', ax=ax)
col1.pyplot(fig)

## Gender Distribution with respect to Heart Disease"

col2.subheader("Gender Distribution with respect to Heart Disease")
col2.write("Comparison of heart disease presence between males and females.")
fig, ax = plt.subplots()
sns.countplot(data=data, x="sex", hue="target", ax=ax)
ax.set_xticklabels(['Female', 'Male'])
col2.pyplot(fig)

## Distribution of Chest Pain Types"

col1.subheader("Distribution of Chest Pain Types")
col1.write("Different types of chest pain experienced by patients.")
fig, ax = plt.subplots()
sns.countplot(data=data, x="cp", ax=ax)
col1.pyplot(fig)

## Correlation Heatmap"

col2.subheader("Correlation Heatmap")
col2.write("Heatmap showing correlations between numerical variables. Darker shades represent stronger correlations.")
correlation = data.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax)
col2.pyplot(fig)

## Resting Blood Pressure vs. Age"

col1.subheader("Resting Blood Pressure vs. Age")
col1.write("Scatter plot visualizing any trends between age and resting blood pressure.")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x="age", y="trestbps", hue="target", ax=ax)
col1.pyplot(fig)

## Maximum Heart Rate Achieved vs. Age"

col2.subheader("Maximum Heart Rate Achieved vs. Age")
col2.write("Scatter plot showing the relationship between age and maximum heart rate during a test.")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x="age", y="thalach", hue="target", ax=ax)
col2.pyplot(fig)

st.subheader("Conclusion")
st.write(
    "From the exploratory data analysis of the heart disease dataset, we can infer the following:"
    "\n- A significant number of patients in the dataset have been diagnosed with heart disease."
    "\n- Age distribution indicates a wide range of ages, but a majority seem to be middle-aged or older."
    "\n- There's a notable difference in heart disease presence between males and females."
    "\n- Different types of chest pain are observed among the patients, with some types being more prevalent."
    "\n- Some variables like resting blood pressure and maximum heart rate achieved show variations with age."
    "\n- Correlation heatmap provides insights on how certain variables might be related to each other."
    "\n\nFurther analysis and modeling can provide deeper insights and predictions based on these factors."
)
