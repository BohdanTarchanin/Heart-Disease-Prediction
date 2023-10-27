
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
st.write(data.head())

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
st.subheader("Distribution of Target Variable (Heart Disease Presence)")
fig, ax = plt.subplots()
sns.countplot(data=data, x="target", ax=ax)
st.pyplot(fig)

## Histogram for age
st.subheader("Age Distribution")
fig, ax = plt.subplots()
sns.histplot(data=data, x="age", kde=True, ax=ax)
st.pyplot(fig)

## Pie chart for gender distribution
st.subheader("Gender Distribution")
fig, ax = plt.subplots()
data['sex'].value_counts().plot.pie(explode=[0,0.1], labels=['Male', 'Female'], autopct='%1.1f%%', ax=ax)
st.pyplot(fig)


## Gender Distribution with respect to Heart Disease
st.subheader("Gender Distribution with respect to Heart Disease")
fig, ax = plt.subplots()
sns.countplot(data=data, x="sex", hue="target", ax=ax)
ax.set_xticklabels(['Female', 'Male'])
st.pyplot(fig)

## Distribution of Chest Pain Types
st.subheader("Distribution of Chest Pain Types")
fig, ax = plt.subplots()
sns.countplot(data=data, x="cp", ax=ax)
st.pyplot(fig)

## Correlation Heatmap
st.subheader("Correlation Heatmap")
correlation = data.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

## Resting Blood Pressure vs. Age
st.subheader("Resting Blood Pressure vs. Age")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x="age", y="trestbps", hue="target", ax=ax)
st.pyplot(fig)

## Maximum Heart Rate Achieved vs. Age
st.subheader("Maximum Heart Rate Achieved vs. Age")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x="age", y="thalach", hue="target", ax=ax)
st.pyplot(fig)


if __name__ == "__main__":
    st.write("Streamlit app is running!")

