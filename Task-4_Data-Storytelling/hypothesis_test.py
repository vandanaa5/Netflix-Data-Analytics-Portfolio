import pandas as pd
from scipy.stats import ttest_ind

print("Program Started...")

# Load dataset
df = pd.read_csv("cleaned_netflix_data.csv")

print("Dataset Loaded Successfully")

# Movies
movies = df[df['type'] == 'Movie']
movies_duration = movies['duration'].str.extract('(\d+)').dropna().astype(int)

# TV Shows
tvshows = df[df['type'] == 'TV Show']
tv_duration = tvshows['duration'].str.extract('(\d+)').dropna().astype(int)

print("Running T-Test...")

# T-Test
t_stat, p_value = ttest_ind(movies_duration, tv_duration)

print("T-Statistic:", t_stat)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")