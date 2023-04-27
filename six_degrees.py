from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import random

load_dotenv()

# Authorise and connect to Spotify API

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Data

artist_list = json.load(open("rapper-list.json"))
first_artist_name = random.choice(artist_list)
second_artist_name = random.choice(artist_list)


# Str -> Object
# Given the name of a rapper, return their Spotify profile
def get_artist_spotify_id(str):
    results = spotify.search(str, limit=1, type="artist")
    try:
        return results["artists"]["items"][0]["id"]
    except IndexError:
        return "No results found"


first_artist_spotify_id = get_artist_spotify_id(first_artist_name)
second_artist_spotify_id = get_artist_spotify_id(second_artist_name)


# Str, Str -> Str
def six_degrees_game():
    print(f"Start at: {first_artist_name}")
    print(f"Finish at: {second_artist_name}")
    for i in range(6):
        song_input = input(f"Song {i + 1}. Choose a song: ")
        print("song_input", song_input)
        artists, track_name = reveal_song_and_artists(song_input, first_artist_name)


# Str -> Array, Str
def reveal_song_and_artists(song_name, artist_name):
    print("song_name", song_name)
    print("search", f"remaster%20track:{song_name} {artist_name}")
    song_details = spotify.search(
        q=f"remaster%20track:{song_name} {artist_name}", limit=1, type="track"
    )
    artists = song_details["tracks"]["items"][0]["artists"]
    track_name = song_details["tracks"]["items"][0]["name"]
    print(track_name, artists)
    return artists, track_name


six_degrees_game()
