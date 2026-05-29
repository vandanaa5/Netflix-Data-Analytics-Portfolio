import pandas as pd

df = pd.read_csv("netflix_titles.csv")

# Basic overview
print(df.head())
print(df.info())
print(df.describe())

print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)

print(df['type'].unique())
print(df['rating'].unique())
print(df['country'].unique()[:10])

# Fill missing values
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Not Available")
df['country'] = df['country'].fillna("Unknown")
df['rating'] = df['rating'].fillna("Not Rated")

df = df.dropna(subset=['date_added'])

df = df.drop_duplicates()

# Remove extra spaces
df['date_added'] = df['date_added'].str.strip()

# Convert to datetime safely
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Drop rows where conversion failed
df = df.dropna(subset=['date_added'])

df['duration_int'] = df['duration'].str.extract(r'(\d+)').astype(float)

df['duration_type'] = df['duration'].apply(lambda x: 'Season' if isinstance(x, str) and 'Season' in x else 'Minutes')


# Year added
df['year_added'] = df['date_added'].dt.year

# Month added
df['month_added'] = df['date_added'].dt.month

# Content age
df['content_age'] = 2024 - df['release_year']

df.to_csv("cleaned_netflix_data.csv", index=False)

print(df['type'].value_counts())
print(df['year_added'].value_counts().sort_index())
print(df['country'].value_counts().head())

