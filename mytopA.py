import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
load_dotenv()

app_id = os.getenv("SPOTIPY_CLIENT_ID")
app_key = os.getenv("SPOTIPY_CLIENT_SECRET")

scope = 'user-top-read'
ranges = ['short_term', 'medium_term', 'long_term']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

for sp_range in ['short_term', 'medium_term', 'long_term']:
    print("range:", sp_range)

    results = sp.current_user_top_artists(time_range=sp_range, limit=50)

    for i, item in enumerate(results['items']):
        print(i, item['name'])
    print()