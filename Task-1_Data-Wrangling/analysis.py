import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_netflix_data.csv")

# Movies vs TV Shows
df['type'].value_counts().plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.show()

# Content added over years
df['year_added'].value_counts().sort_index().plot()
plt.title("Content Added Over Years")
plt.show()