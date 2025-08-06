import pandas as pd
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load JSON files into a DataFrame
json_dir = '/Users/roberto/OneDrive/Azure/Spotify/MyData2'
dataframes = []

for file in os.listdir(json_dir):
    if file.endswith('.json'):
        with open(os.path.join(json_dir, file), 'r') as f:
            data = json.load(f)
            dataframes.append(pd.DataFrame(data))

df = pd.concat(dataframes, ignore_index=True)

# Convert timestamp to datetime
df['ts'] = pd.to_datetime(df['ts'])

# Extract time-based features
df['hour'] = df['ts'].dt.hour
df['day_of_week'] = df['ts'].dt.day_name()
df['month'] = df['ts'].dt.month_name()
df['year'] = df['ts'].dt.year

# Convert milliseconds to hours
df['hours_played'] = df['ms_played'] / 3600000

# Set theme
sns.set_theme(style="whitegrid")

# Time series of total listening time
plt.figure(figsize=(12, 6))
df['year_month'] = df['ts'].dt.to_period('M')
monthly_hours = df.groupby('year_month')['hours_played'].sum()
monthly_hours.plot(kind='line', marker='o', color='tab:blue', linewidth=2)
plt.title('Monthly Listening Time', fontsize=16)
plt.ylabel('Hours Played', fontsize=14)
plt.xlabel('Month/Year', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Heatmap of listening hours vs. days of the week
plt.figure(figsize=(14, 8))
heatmap_data = df.groupby(['day_of_week', 'hour'])['hours_played'].sum().unstack()
sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt='.1f', linewidths=.5, cbar_kws={'label': 'Hours Played'})
plt.title('Listening Hours vs. Days of the Week', fontsize=16)
plt.xlabel('Hour of the Day', fontsize=14)
plt.ylabel('Day of the Week', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Heatmap of listening hours per month of the year
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
monthly_heatmap_data = df.groupby(['year', 'month'])['hours_played'].sum().unstack()[month_order]

plt.figure(figsize=(14, 8))
sns.heatmap(monthly_heatmap_data, cmap='YlGnBu', annot=True, fmt='.1f', linewidths=.5, cbar_kws={'label': 'Hours Played'})
plt.title('Total Listening Hours per Month of the Year', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Year', fontsize=14)
plt.tight_layout()
plt.show()

# Top 30 Tracks
plt.figure(figsize=(12, 8))
top_tracks = df.groupby('master_metadata_track_name')['hours_played'].sum().nlargest(30)
ax = top_tracks.plot(kind='barh', color='tab:blue')
plt.title('Top 30 Tracks by Listening Time', fontsize=16)
plt.xlabel('Hours Played', fontsize=14)
plt.ylabel('Track Name', fontsize=14)

for i, v in enumerate(top_tracks):
    ax.text(v + 0.1, i, f"{v:.1f}", color='black', va='center')

plt.tight_layout()
plt.show()

# Top 50 Artists
plt.figure(figsize=(12, 8))
top_artists = df.groupby('master_metadata_album_artist_name')['hours_played'].sum().nlargest(50)
ax = top_artists.plot(kind='barh', color='tab:green')
plt.title('Top 50 Artists by Listening Time', fontsize=16)
plt.xlabel('Hours Played', fontsize=14)
plt.ylabel('Artist Name', fontsize=14)

for i, v in enumerate(top_artists):
    ax.text(v + 0.1, i, f"{v:.1f}", color='black', va='center')

plt.tight_layout()
plt.show()

# Interactive Scatter Plot for Top 101 Artists
top_101_artists = df.groupby('master_metadata_album_artist_name')['hours_played'].sum().nlargest(101).reset_index()

fig = px.scatter(
    top_101_artists,
    x='hours_played',
    y='master_metadata_album_artist_name',
    size='hours_played',
    color='hours_played',
    hover_name='master_metadata_album_artist_name',
    hover_data={'hours_played': ':.1f'},
    title='Top 101 Artists by Listening Time',
    labels={'hours_played': 'Hours Played', 'master_metadata_album_artist_name': 'Artist Name'},
    color_continuous_scale='viridis'
)

fig.update_layout(
    xaxis_title='Hours Played',
    yaxis_title='Artist Name',
    showlegend=False,
    template='plotly_white'
)

fig.show()