import pandas as pd
import matplotlib.pyplot as plt

# STYLE (Netflix Theme)

plt.style.use('dark_background')

# STEP 1: Load Dataset

df = pd.read_csv("C:\\Users\\vanda\\OneDrive\\Desktop\\dsproj\\Eda Task\\cleaned_netflix_data.csv")

print("🔹 First 5 Rows:")
print(df.head())

print("\n🔹 Dataset Info:")
print(df.info())

print("\n🔹 Summary Statistics:")
print(df.describe())

# STEP 2: Basic Analysis

print("\n🔹 Content Type Distribution:")
print(df['type'].value_counts())

print("\n🔹 Top Countries:")
print(df['country'].value_counts().head())

print("\n🔹 Ratings Distribution:")
print(df['rating'].value_counts())

# STEP 3: Visualizations

# Movies vs TV Shows
plt.figure()
df['type'].value_counts().plot(kind='bar', color='red')
plt.title("Movies vs TV Shows", color='red')
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# Top 10 Countries
plt.figure()
df['country'].value_counts().head(10).plot(kind='bar', color='red')
plt.title("Top 10 Countries", color='red')
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Ratings Distribution
plt.figure()
df['rating'].value_counts().plot(kind='bar', color='red')
plt.title("Ratings Distribution", color='red')
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# STEP 4: Time-based Analysis

# Content growth over years
plt.figure()
df['release_year'].value_counts().sort_index().plot(color='red')
plt.title("Content Growth Over Years", color='red')
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

# Content added trend
plt.figure()
df['year_added'].value_counts().sort_index().plot(color='red')
plt.title("Content Added Over Time", color='red')
plt.xlabel("Year Added")
plt.ylabel("Count")
plt.show()

# STEP 5: Business Questions

# Top Genres
print("\n🔹 Top Genres:")
print(df['listed_in'].value_counts().head())

# Movies vs TV Shows count
print("\n🔹 Movies vs TV Shows:")
print(df['type'].value_counts())

# Top Countries
print("\n🔹 Top 5 Countries:")
print(df['country'].value_counts().head())

# Most Common Ratings
print("\n🔹 Most Common Ratings:")
print(df['rating'].value_counts().head())

# STEP 6: Duration Analysis

plt.figure()
df['duration_int'].hist(color='red')
plt.title("Duration Distribution", color='red')
plt.xlabel("Duration")
plt.ylabel("Frequency")
plt.show()

# STEP 7: Insights (Print)

print("\n🔹 KEY INSIGHTS:")
print("1. Netflix has more Movies than TV Shows.")
print("2. Content production increased significantly after 2016.")
print("3. United States produces the highest number of titles.")
print("4. TV-MA and TV-14 are the most common ratings.")
print("5. Drama and International genres are most popular.")