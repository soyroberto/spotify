import pandas as pd
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns
import mplcursors

# Load JSON files into a DataFrame
json_dir = '/Users/roberto/OneDrive/Azure/Spotify/MyData2'
dataframes = []

for file in os.listdir(json_dir):
    if file.endswith('.json'):
        with open(os.path.join(json_dir, file), 'r') as f:
            data = json.load(f)
            dataframes.append(pd.DataFrame(data))

df = pd.concat(dataframes, ignore_index=True) # One large dataframe creation from json files

# Convert timestamp to datetime
df['ts'] = pd.to_datetime(df['ts'])

# Extract time-based features
df['hour'] = df['ts'].dt.hour
df['day_of_week'] = df['ts'].dt.day_name()
df['month'] = df['ts'].dt.month_name()
df['year'] = df['ts'].dt.year

# Convert milliseconds to hours
df['hours_played'] = df['ms_played'] / 3600000

## Visualizations

# Time series of total listening time
plt.figure(figsize=(12, 6))
df['year_month'] = df['ts'].dt.to_period('M')
monthly_hours = df.groupby('year_month')['hours_played'].sum()
ax = monthly_hours.plot(kind='bar', width=0.8, color=monthly_hours.index.year.map(lambda x: plt.cm.tab20(x % 20)))
plt.title('Monthly Listening Time')
plt.ylabel('Hours Played')
plt.xlabel('Month/Year')
ax.set_xticklabels([f"{x.month:02d}/{x.year % 100:02d}" for x in monthly_hours.index], rotation=90)

# Add labels inside the bars
for i, (index, value) in enumerate(monthly_hours.items()):
    position = 'top' if i % 2 == 0 else 'bottom'
    y = value + 0.5 if position == 'top' else value - 0.5
    ax.text(i, y, f"{value:.1f}", ha='center', va=position, color='black')

plt.tight_layout()
plt.show()

# Heatmap of listening hours vs. days of the week
plt.figure(figsize=(14, 8))
heatmap_data = df.groupby(['day_of_week', 'hour'])['hours_played'].sum().unstack()
sns.heatmap(heatmap_data, cmap='viridis', annot=True, fmt='.1f', linewidths=.5, cbar_kws={'label': 'Hours Played'})
plt.title('Listening Hours vs. Days of the Week')
plt.xlabel('Hour of the Day')
plt.ylabel('Day of the Week')
plt.tight_layout()
plt.show()

# Heatmap of listening hours per month of the year
plt.figure(figsize=(14, 8))
monthly_heatmap_data = df.groupby(['year', 'month'])['hours_played'].sum().unstack()
sns.heatmap(monthly_heatmap_data, cmap='viridis', annot=True, fmt='.1f', linewidths=.5, cbar_kws={'label': 'Hours Played'})
plt.title('Total Listening Hours per Month of the Year')
plt.xlabel('Month')
plt.ylabel('Year')
plt.tight_layout()
plt.show()

## Data Analysis
# Top 30 tracks
plt.figure(figsize=(12, 6))
top_tracks = df.groupby('master_metadata_track_name')['hours_played'].sum().nlargest(30)
top_tracks.plot(kind='bar', title='Top 10 Tracks by Listening Time')
plt.ylabel('Hours Played')
plt.xlabel('Track Name')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Top 50 artists by listening time  
plt.figure(figsize=(12, 6))
top_artists = df.groupby('master_metadata_album_artist_name')['hours_played'].sum().nlargest(101)
top_artists.plot(kind='bar', title='Top Artists by Listening Time')
plt.ylabel('Hours Played')
plt.xlabel('Artist Name')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Heatmap of top 101 artists by listening time
plt.figure(figsize=(12, 12))
top_101_artists = df.groupby('master_metadata_album_artist_name')['hours_played'].sum().nlargest(50)
top_101_artists_df = top_101_artists.reset_index()

# Create a scatter plot with square markers
plt.figure(figsize=(10, 10))
scatter = plt.scatter(
    x=top_101_artists_df['hours_played'],
    y=range(len(top_101_artists_df)),  # Use index for y-axis
    s=top_101_artists_df['hours_played'] * 12,  # Adjust the size of the squares
    c=top_101_artists_df['hours_played'],
    cmap='viridis',
    alpha=0.6,
    edgecolors='w',
    linewidth=0.5
)

# Add artist names next to the dots
for i in range(len(top_101_artists_df)):
    plt.text(
        top_101_artists_df['hours_played'][i],
        i,  # Use index for y-axis
        top_101_artists_df['master_metadata_album_artist_name'][i],
        fontsize=9,
        ha='right' if i % 2 == 0 else 'left',
        va='center'
    )

plt.colorbar(scatter, label='Hours Played')
plt.title('Top 101 Artists by Listening Time')
plt.xlabel('Hours Played')
plt.yticks(range(len(top_101_artists_df)), [''] * len(top_101_artists_df))  # Remove y-axis labels
plt.tight_layout()

# Add interactive tooltips
cursor = mplcursors.cursor(scatter, hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(
    f"{top_101_artists_df['master_metadata_album_artist_name'][sel.index]}: {top_101_artists_df['hours_played'][sel.index]:.1f} hours"))

plt.show()