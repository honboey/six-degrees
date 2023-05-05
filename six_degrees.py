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

artist_list = json.load(open("data/rapper-list.json"))
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
        song_name = input(f"Song {i + 1}: ")
        artist_name = input(f"Artist: ")
        # TODO: check that the artist is in the previous song choice
        if artist_is_valid(artist_name, list_of_artists):
            song_name, artist_name = reveal_song_and_artists(song_name, artist_name)
        else:
            # go back to ask for artist_name
            pass
        print(f"{song_name} by {artist_name}")


# Str -> Array, Str
# Given a song name and an artist, search the SPotify API and return the song name and a lists of artists
def reveal_song_and_artists(song_name, artist_name):
    song_details = spotify.search(q=f"{song_name} {artist_name}", limit=1, type="track")
    track_name = song_details["tracks"]["items"][0]["name"]
    artists = create_list_of_artists(song_details["tracks"]["items"][0]["artists"])
    return track_name, artists


# Array -> Array
def create_list_of_artists(raw_list_of_artists):
    list_of_artists = []
    for i in range(len(raw_list_of_artists)):
        list_of_artists.append(raw_list_of_artists[i]["name"])
    return list_of_artists


# Str, Array -> Boolean
def artist_is_valid(artist_name, list_of_artists):
    return artist_name in list_of_artists


# six_degrees_game()
