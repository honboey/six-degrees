from six_degrees import (
    get_artist_spotify_id,
    reveal_song_and_artists,
    create_list_of_artists,
    artist_is_valid,
)


# Test data
##########################

raw_list_of_artists = [
    {
        "external_urls": {
            "spotify": "https://open.spotify.com/artist/5K4W6rqBFWDnAN6FQUkS6x"
        },
        "href": "https://api.spotify.com/v1/artists/5K4W6rqBFWDnAN6FQUkS6x",
        "id": "5K4W6rqBFWDnAN6FQUkS6x",
        "name": "Kanye West",
        "type": "artist",
        "uri": "spotify:artist:5K4W6rqBFWDnAN6FQUkS6x",
    },
    {
        "external_urls": {
            "spotify": "https://open.spotify.com/artist/0Mz5XE0kb1GBnbLQm2VbcO"
        },
        "href": "https://api.spotify.com/v1/artists/0Mz5XE0kb1GBnbLQm2VbcO",
        "id": "0Mz5XE0kb1GBnbLQm2VbcO",
        "name": "Mos Def",
        "type": "artist",
        "uri": "spotify:artist:0Mz5XE0kb1GBnbLQm2VbcO",
    },
    {
        "external_urls": {
            "spotify": "https://open.spotify.com/artist/1i4q97Tz8xmGWJps51J7WT"
        },
        "href": "https://api.spotify.com/v1/artists/1i4q97Tz8xmGWJps51J7WT",
        "id": "1i4q97Tz8xmGWJps51J7WT",
        "name": "Albe Back",
        "type": "artist",
        "uri": "spotify:artist:1i4q97Tz8xmGWJps51J7WT",
    },
]

##########################
# get_spotify_artist_id
##########################


def test_get_spotify_artist():
    assert get_artist_spotify_id("Mos Def") == "0Mz5XE0kb1GBnbLQm2VbcO"


def test_get_spotify_artist__no_results():
    assert get_artist_spotify_id("alksdfjiafdnl C") == "No results found"


###########################
# reveal_song_and_artists()
###########################


def test_reveal_song_and_artists():
    assert reveal_song_and_artists("Good Night", "Mos Def") == (
        "Good Night",
        ["Kanye West", "Mos Def", "Albe Back"],
    )


###########################
# create_list_of_artists()
###########################


def test_create_list_of_artists():
    assert create_list_of_artists(raw_list_of_artists) == (
        ["Kanye West", "Mos Def", "Albe Back"]
    )


###########################
#  artist_is_valid()
###########################


def test_artist_is_valid():
    assert artist_is_valid("Mos Def", ["Kanye West", "Mos Def", "Albe Back"]) == True
