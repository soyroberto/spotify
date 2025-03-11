import pandas as pd
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns
import mplcursors
import plotly.express as px

# Load JSON files into a DataFrame
json_dir = '/Users/roberto/OneDrive/Azure/Spotify/MyData2'
dataframes = []

for file in os.listdir(json_dir):
    if file.endswith('.json'):
        with open(os.path.join(json_dir, file), 'r') as f:
            data = json.load(f)
            dataframes.append(pd.DataFrame(data))

df = pd.concat(dataframes, ignore_index=True)  # Combine JSONs into one DataFrame

# Convert timestamp to datetime
df['ts'] = pd.to_datetime(df['ts'])

# Extract time-based features
df['hour'] = df['ts'].dt.hour
df['day_of_week'] = df['ts'].dt.day_name()
df['month'] = df['ts'].dt.month_name()
df['year'] = df['ts'].dt.year

# Convert milliseconds to hours
df['hours_played'] = df['ms_played'] / 3600000

## --- IMPROVED VISUALIZATIONS ---

# 1. Monthly Listening Time (Better Colors & Labels)
plt.figure(figsize=(12, 6))
df['year_month'] = df['ts'].dt.to_period('M')
monthly_hours = df.groupby('year_month')['hours_played'].sum()
ax = monthly_hours.plot(kind='bar', width=0.85, cmap='plasma')

plt.title('Monthly Listening Time', fontsize=14, fontweight='bold')
plt.ylabel('Hours Played', fontsize=12)
plt.xlabel('Month/Year', fontsize=12)
ax.set_xticklabels([f"{x.month:02d}/{x.year % 100:02d}" for x in monthly_hours.index], rotation=90)

# Add labels inside bars
for i, (index, value) in enumerate(monthly_hours.items()):
    plt.text(i, value + 1, f"{value:.1f}", ha='center', va='bottom', fontsize=10, color='black')

plt.tight_layout()
plt.show()

# 2. Heatmap: Listening Hours vs. Days of the Week (Better Colors & Readability)
plt.figure(figsize=(14, 8))
heatmap_data = df.groupby(['day_of_week', 'hour'])['hours_played'].sum().unstack()
sns.heatmap(heatmap_data, cmap='magma', annot=True, fmt='.1f', linewidths=.5, cbar_kws={'label': 'Hours Played'})

plt.title('Listening Hours vs. Days of the Week', fontsize=14, fontweight='bold')
plt.xlabel('Hour of the Day', fontsize=12)
plt.ylabel('Day of the Week', fontsize=12)
plt.xticks(rotation=0)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

# 3. Top 30 Tracks (Better Bar Plot)
top_tracks = df.groupby('master_metadata_track_name')['hours_played'].sum().nlargest(30)
plt.figure(figsize=(12, 8))
sns.barplot(y=top_tracks.index, x=top_tracks.values, palette="coolwarm")
plt.title('Top 30 Tracks by Listening Time', fontsize=14, fontweight='bold')
plt.xlabel('Hours Played', fontsize=12)
plt.ylabel('Track Name', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()

# 4. Top Artists (Using Plotly for Interactivity)
top_artists = df.groupby('master_metadata_album_artist_name')['hours_played'].sum().nlargest(50).reset_index()

fig = px.bar(top_artists, 
             x="hours_played", 
             y="master_metadata_album_artist_name", 
             orientation='h', 
             color='hours_played',
             title="Top Artists by Listening Time",
             color_continuous_scale='viridis')

fig.update_layout(xaxis_title="Hours Played", yaxis_title="Artist", height=800)
fig.show()

# 5. Scatter Plot of Top 50 Artists (Better Aesthetics)
top_50_artists = df.groupby('master_metadata_album_artist_name')['hours_played'].sum().nlargest(50).reset_index()

plt.figure(figsize=(12, 8))
scatter = plt.scatter(
    x=top_50_artists['hours_played'],
    y=range(len(top_50_artists))[::-1],  # Reverse y-axis order
    s=top_50_artists['hours_played'] * 15,  # Adjust marker size
    c=top_50_artists['hours_played'],
    cmap='plasma',
    alpha=0.75,
    edgecolors='white',
    linewidth=0.8
)

# Add artist names next to markers
for i in range(len(top_50_artists)):
    plt.text(top_50_artists['hours_played'][i], 
             len(top_50_artists) - 1 - i, 
             top_50_artists['master_metadata_album_artist_name'][i], 
             fontsize=10, ha='right' if i % 2 == 0 else 'left', color='white')

plt.colorbar(scatter, label='Hours Played')
plt.title('Top 50 Artists by Listening Time', fontsize=14, fontweight='bold')
plt.xlabel('Hours Played', fontsize=12)
plt.yticks(range(len(top_50_artists)), [''] * len(top_50_artists))  # Hide y-axis labels
plt.gca().set_facecolor('#222222')  # Dark background for contrast
plt.grid(alpha=0.3)

# Interactive tooltip
cursor = mplcursors.cursor(scatter, hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(
    f"{top_50_artists['master_metadata_album_artist_name'][sel.index]}: {top_50_artists['hours_played'][sel.index]:.1f} hrs"
))

plt.tight_layout()
plt.show()
