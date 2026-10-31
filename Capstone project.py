# ==========================================
# CODINGAL CAPSTONE PROJECT - FINAL CODE
# ==========================================

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------
# Step 1: Import the dataset using Pandas
# ------------------------------------------
df = pd.read_csv("IMDB Dataset.csv")

# ------------------------------------------
# Step 2: Print first 3 and last 3 rows
# ------------------------------------------
print("--- FIRST 3 ROWS ---")
print(df.head(3))

print("\n--- LAST 3 ROWS ---")
print(df.tail(3))

# ------------------------------------------
# Step 3: Check detailed information
# ------------------------------------------
print("\n--- DATASET INFORMATION ---")
df.info()

# ------------------------------------------
# Step 4: Check for null values
# ------------------------------------------
print("\n--- NULL VALUES COUNT PER COLUMN ---")
print(df.isnull().sum())

print("\nAre there any null values in the dataset?", df.isnull().values.any())

# ------------------------------------------
# Step 5: Create a subset (row numbers 41 to 75)
# ------------------------------------------
subset_df = df.iloc[40:76]
print("\n--- SUBSET (Rows 41 to 75) ---")
print(subset_df)

# ------------------------------------------
# Step 6: Movie with the highest votes
# ------------------------------------------
print("\n--- MOVIE WITH HIGHEST VOTES ---")
highest_votes_movie = df[df['No_of_Votes'] == df['No_of_Votes'].max()]
print(highest_votes_movie)

# ------------------------------------------
# Step 7: Boxplots for IMDB_Rating and Runtime
# ------------------------------------------
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
sns.boxplot(y=df['IMDB_Rating'], color='skyblue')
plt.title("Boxplot of IMDB Rating")

plt.subplot(1, 2, 2)
sns.boxplot(y=df['Runtime'], color='lightgreen')
plt.title("Boxplot of Runtime")

plt.tight_layout()
plt.show()

# ------------------------------------------
# Step 8: Relationship using Matplotlib
# ------------------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(df['Runtime'], df['IMDB_Rating'], alpha=0.5, color='purple')
plt.title("Relationship between Runtime and IMDB Rating")
plt.xlabel("Runtime")
plt.ylabel("IMDB Rating")
plt.grid(True)
plt.show()

# ------------------------------------------
# Step 9: Distribution plots
# ------------------------------------------
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
sns.histplot(df['IMDB_Rating'], kde=True, color='blue')
plt.title("Distribution of IMDB Rating")

plt.subplot(1, 2, 2)
sns.histplot(df['Runtime'], kde=True, color='green')
plt.title("Distribution of Runtime")

plt.tight_layout()
plt.show()

# ------------------------------------------
# Step 10: Count plot of feature Rating
# ------------------------------------------
plt.figure(figsize=(12, 5))
sns.countplot(data=df, x='Rating', order=df['Rating'].value_counts().index, palette='viridis')
plt.title("Number of Movies per Rating")
plt.xticks(rotation=45)
plt.show()