import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '2024Populations.csv'
df = pd.read_csv(file_path)

# Descriptive Statistics
print("Descriptive Statistics:")
print(df.describe())

# Correlation Matrix
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
corr_matrix = df[numeric_columns].corr()
print("\nCorrelation Matrix:")
print(corr_matrix)

# Function to plot Line Plot: Population trends for India
def plot_population_trends_for_india(df):
    india_data = df[df['country'] == 'India']
    years = ['1980', '2000', '2010', '2023', '2024', '2030', '2050']
    india_population = india_data[['pop1980', 'pop2000', 'pop2010', 'pop2023', 'pop2024', 'pop2030', 'pop2050']].values.flatten()

    plt.figure(figsize=(10, 6))
    plt.plot(years, india_population, marker='o', linestyle='-', color='b')
    plt.xlabel('Year', fontweight='bold')
    plt.ylabel('Population', fontweight='bold')
    plt.title('Population Trends (1980 - 2050) for India', fontweight='bold')
    plt.grid(True)
    plt.show()

# Function to plot Pie Chart: Population distribution for the top 5 countries in 2024
def plot_population_distribution_top_5(df):
    top_5_pop_2024 = df.nlargest(5, 'pop2024')
    plt.figure(figsize=(10, 6))
    plt.pie(top_5_pop_2024['pop2024'], labels=top_5_pop_2024['country'], autopct='%1.1f%%', startangle=140)
    plt.title('Population Distribution for Top 5 Countries in 2024', fontweight='bold')
    plt.axis('equal')
    plt.show()

# Function to plot Bar Chart: Population density of the top 10 countries in 2024
def plot_population_density_top_10(df):
    top_10_density_2024 = df.nlargest(10, 'Density_2024')
    plt.figure(figsize=(12, 8))
    plt.bar(top_10_density_2024['country'], top_10_density_2024['Density_2024'], color='orange')
    plt.xlabel('Country', fontweight='bold')
    plt.ylabel('Population Density (2024)', fontweight='bold')
    plt.title('Population Density of Top 10 Countries in 2024', fontweight='bold')
    plt.xticks(rotation=45)
    plt.show()

# Function to plot Heatmap: Correlation matrix
def plot_correlation_matrix(corr_matrix):
    plt.figure(figsize=(14, 10))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix', fontweight='bold')
    plt.show()

# Plot the charts
plot_population_trends_for_india(df)
plot_population_distribution_top_5(df)
plot_population_density_top_10(df)
plot_correlation_matrix(corr_matrix)
