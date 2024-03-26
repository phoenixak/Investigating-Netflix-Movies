# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# data set
netflix_df = pd.read_csv("dataset/netflix_data.csv")

# Inspect the first few rows
print(netflix_df.head())


# Subset the DataFrame for movies
netflix_movies = netflix_df[netflix_df['type'] == 'Movie']
# Subset the columns
netflix_movies = netflix_movies[['title', 'country', 'genre', 'release_year', 'duration']]
# Filter movies by duration
short_movies = netflix_movies[netflix_movies['duration'] < 60]
# Assign colors to genres
colors = ['blue' if genre == 'Children' else 'green' if genre == 'Documentaries' else 'red' if genre == 'Stand-Up' else 'black' for genre in netflix_movies['genre']]

# Create a scatter plot
fig, ax = plt.subplots()
scatter = ax.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)

# Set labels and title
ax.set_xlabel('Release year')
ax.set_ylabel('Duration (min)')
ax.set_title('Movie Duration by Year of Release')

# Show the plot
plt.show()

answer="no"