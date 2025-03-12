import pandas as pd
import panel as pn
import json
import os

# Load JSON files into a DataFrame
json_dir = '/Users/roberto/OneDrive/Azure/Spotify/MyData2'  # Replace with your JSON directory
dataframes = []

for file in os.listdir(json_dir):
    if file.endswith('.json'):
        with open(os.path.join(json_dir, file), 'r') as f:
            data = json.load(f)
            dataframes.append(pd.DataFrame(data))

# Combine all JSON data into a single DataFrame
df = pd.concat(dataframes, ignore_index=True)

# Convert timestamp to datetime
df['ts'] = pd.to_datetime(df['ts'])

# Convert milliseconds to hours
df['hours_played'] = df['ms_played'] / 3600000

# Create widgets
artist_input = pn.widgets.TextInput(name='Artist', placeholder='Enter artist name')
query_button = pn.widgets.Button(name='Query', button_type='primary')
export_button = pn.widgets.Button(name='Export to CSV', button_type='success')

# Output widget
output = pn.widgets.DataFrame()

# Define the query function
def query_artist_data(event):
    try:
        artist = artist_input.value

        if not artist:
            output.value = pd.DataFrame({'Error': ['Please enter an artist name.']})
            return

        # Case-insensitive and partial match filtering
        filtered_df = df[df['master_metadata_album_artist_name'].str.contains(artist, case=False, na=False)]

        if filtered_df.empty:
            output.value = pd.DataFrame({'Error': [f"No data found for artist '{artist}'."]})
        else:
            # Group by track and sum hours played
            result = filtered_df.groupby('master_metadata_track_name')['hours_played'].sum().reset_index()
            result = result.rename(columns={'master_metadata_track_name': 'Track', 'hours_played': 'Hours Played'})
            output.value = result
    except Exception as e:
        output.value = pd.DataFrame({'Error': [f"An error occurred: {str(e)}"]})

# Define the export function
def export_data(event):
    try:
        if output.value.empty:
            print("No query results to export.")
            return
        
        artist = artist_input.value
        output.value.to_csv(f"{artist}_listening_history.csv", index=False)
        print(f"Exported results to '{artist}_listening_history.csv'.")
    except Exception as e:
        print(f"An error occurred while exporting: {str(e)}")

# Attach the query function to the button
query_button.on_click(query_artist_data)

# Attach the export function to the button
export_button.on_click(export_data)

# Create a layout
layout = pn.Column(
    artist_input,
    query_button,
    export_button,
    output
)

# Launch the app
if __name__ == '__main__':
    layout.show()