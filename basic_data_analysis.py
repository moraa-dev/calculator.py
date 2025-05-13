# Data Analysis and Visualization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set styling for better visualizations
plt.style.use('seaborn-v0_8-whitegrid')
sns.set(font_scale=1.1)

# Task 1: Load and Explore the Dataset
print("------ TASK 1: LOADING AND EXPLORING THE DATASET ------")

# Try loading the Iris dataset
try:
    # Load the Iris dataset from sklearn
    iris = load_iris()

    # Create a pandas DataFrame from the dataset
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

    # Add the target column (species)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    print("Dataset loaded successfully!\n")

    # Display the first few rows of the dataset
    print("First 5 rows of the dataset:")
    print(df.head())
    print("\n")

    # Display the structure of the dataset
    print("Dataset structure:")
    print(f"Shape: {df.shape} (rows, columns)")
    print("Data types:")
    print(df.dtypes)
    print("\n")

    # Check for missing values
    print("Missing values:")
    print(df.isnull().sum())
    print("\n")

    # Clean the dataset
    print("The Iris dataset is already clean with no missing values.")

except Exception as e:
    print(f"Error loading or exploring the dataset: {e}")

# Task 2: Basic Data Analysis
print("\n------ TASK 2: BASIC DATA ANALYSIS ------")

try:
    # Compute basic statistics of numerical columns
    print("Basic statistics of numerical columns:")
    print(df.describe())
    print("\n")

    # Group by species and compute mean of numerical columns
    print("Mean of numerical columns grouped by species:")
    species_means = df.groupby('species').mean()
    print(species_means)
    print("\n")

    # Identify patterns or interesting findings
    print("Interesting findings:")
    print("1. Setosa species has the smallest petal length and width.")
    print("2. Virginica species has the largest sepal length and petal dimensions.")
    print("3. Versicolor species has intermediate values for most measurements.")
    print("4. There appears to be a strong correlation between petal length and petal width.")

except Exception as e:
    print(f"Error performing data analysis: {e}")

# Task 3: Data Visualization
print("\n------ TASK 3: DATA VISUALIZATION ------")

try:
    # Create figure with 2x2 subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))

    # 1. Line chart showing trends
    # Creating a line chart showing the sorted values of sepal length by species
    for species in iris.target_names:
        sorted_values = df[df['species'] ==
                           species]['sepal length (cm)'].sort_values()
        axes[0, 0].plot(sorted_values.index, sorted_values, label=species)

    axes[0, 0].set_title('Sepal Length Trends by Species')
    axes[0, 0].set_xlabel('Index (sorted)')
    axes[0, 0].set_ylabel('Sepal Length (cm)')
    axes[0, 0].legend()

    # 2. Bar chart showing comparison of numerical values across categories
    species_means.plot(kind='bar', ax=axes[0, 1])
    axes[0, 1].set_title('Average Measurements by Species')
    axes[0, 1].set_xlabel('Species')
    axes[0, 1].set_ylabel('Measurement (cm)')

    # 3. Histogram of a numerical column
    axes[1, 0].hist(df['petal length (cm)'], bins=20,
                    color='skyblue', edgecolor='black')
    axes[1, 0].set_title('Distribution of Petal Length')
    axes[1, 0].set_xlabel('Petal Length (cm)')
    axes[1, 0].set_ylabel('Frequency')

    # 4. Scatter plot to visualize relationship between two numerical columns
    for i, species in enumerate(iris.target_names):
        species_data = df[df['species'] == species]
        axes[1, 1].scatter(
            species_data['sepal length (cm)'],
            species_data['petal length (cm)'],
            label=species,
            s=50,
            alpha=0.7
        )

    axes[1, 1].set_title('Sepal Length vs. Petal Length')
    axes[1, 1].set_xlabel('Sepal Length (cm)')
    axes[1, 1].set_ylabel('Petal Length (cm)')
    axes[1, 1].legend()

    # Adjust layout and save figure
    plt.tight_layout()
    plt.savefig('iris_data_visualization.png')
    print("Visualizations have been created and saved as 'iris_data_visualization.png'")

    # Show the plots
    plt.show()

    # Additional visualization: Pairplot using seaborn
    print("\nCreating a pairplot to visualize relationships between all features...")
    sns.pairplot(df, hue='species', height=2.5)
    plt.suptitle('Iris Dataset - Pairplot of All Features', y=1.02)
    plt.savefig('iris_pairplot.png')
    print("Pairplot has been created and saved as 'iris_pairplot.png'")

    # Show the pairplot
    plt.show()

except Exception as e:
    print(f"Error creating visualizations: {e}")

# Summary of findings
print("\n------ SUMMARY OF FINDINGS ------")
print("1. The Iris dataset consists of 150 samples, with 50 samples from each of three species.")
print("2. The features measured are sepal length, sepal width, petal length, and petal width.")
print("3. Iris setosa is clearly distinguishable from the other two species based on petal dimensions.")
print("4. Iris virginica and Iris versicolor have some overlap but can generally be differentiated based on their measurements.")
print("5. Petal length and width show strong correlation and are particularly useful for species identification.")
print("6. The dataset is clean with no missing values, making it ideal for analysis and modeling.")
print("\nAnalysis completed")
