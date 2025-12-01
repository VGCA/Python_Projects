import pandas as pandas
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"

df = pandas.read_csv(url)

# Inspect data

print(df.info())
print(df.describe())

# Handle missing values

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove duplicates

df = df.drop_duplicates()

# Filter data: Passengers in first class

first_class = df[df["Pclass"]==1]
print("First class passengers: \n",first_class.head())

# End of the task 1: perform data cleaning, aggregation and filtering

# Bar chart: Survival rate by class

survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar", color="skyblue")
plt.title("Survival rate by class")
plt.ylabel("Survival rate")
plt.show()

# Histogram: age distribution

sns.histplot(df["Age"], kde=True, bins=20, color="purple")
plt.title("Age Dsitribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Scatter plot: Age vs Fare

plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="green")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

# End of the task 2: generate visualizations to illustrate key insights

 

# End of task 3: identify and interpret patterns or anomalies