from six_degrees import get_artist_spotify_id, reveal_song_and_artists

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
    assert reveal_song_and_artists("Good Night", "Mos Def") == "Good Night"