import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('StudentGradesAndPrograms.csv')


# Data Cleaning
# Convert `classPeriod` to numeric format and handle errors
data['classPeriod'] = pd.to_numeric(data['classPeriod'], errors='coerce')

# Remove outliers in `gradePercentage`
data = data[data['gradePercentage'].between(0, 100)]

# Exploratory Data Analysis (EDA)

# Set plot aesthetics
sns.set_theme(style="whitegrid")

# 1. Distribution of `gradePercentage`
plt.figure(figsize=(8, 5))
sns.histplot(data['gradePercentage'], bins=20, kde=True, color='blue')
plt.title('Distribution of Grade Percentages', fontsize=14)
plt.xlabel('Grade Percentage')
plt.ylabel('Frequency')
plt.show()

# 2. Boxplot of `gradePercentage` by `gradeLevel`
plt.figure(figsize=(12, 6))
sns.boxplot(x='gradeLevel', y='gradePercentage', data=data, palette='Set3', order=sorted(data['gradeLevel'].unique()))
plt.title('Grade Percentages by Grade Level', fontsize=14)
plt.xlabel('Grade Level')
plt.ylabel('Grade Percentage')
plt.xticks(rotation=45)
plt.show()

# 3. Participation in AVID program and its impact on grades
plt.figure(figsize=(8, 5))
sns.boxplot(x='avid', y='gradePercentage', data=data, palette='muted')
plt.title('Grade Percentages: AVID vs. Non-AVID', fontsize=14)
plt.xlabel('AVID Program Participation')
plt.ylabel('Grade Percentage')
plt.show()
