'''
A quick script to merge several playlists to one
by a3rosol
v 0.1

Requirements: 
	spotipy - Install with pip install spotipy
	your Spotify username - google it ;)
	your client ID and ~secret - get it at https://developer.spotify.com/my-applications and create one
	redirect URI - keep it the way it is, but add it during registration of your app
'''

import spotipy
import spotipy.util as util

username = "" # Add user name here or ID here
clientID = '' # add client ID here
clientSecret = '' # add client secret here
uri = 'http://localhost:8888/callback' # try not to change it

combinedPlaylistName = 'New Playlist' # the created playlist will have this name

'''
This is really ugly, I will replace this with something prettier in the future 
For now this will suffice
The script dumps your playlists and their corresponding playlist IDs - but only 50.
Will improve in the future
Copy and paste them inside the brackets in this format:
'playlistid', 'playlistid',....
Sadly, I haven't found a different way to get those IDs since spotify removed Folder support
from their API -.-
'''
playlistArray = []

'''
The script will prompt you to paste the redirect URI in
'''

token = util.prompt_for_user_token(username, scope="playlist-read-private playlist-modify-private", client_id = clientID,
									client_secret = clientSecret, redirect_uri = uri)


def getTracks(results):
	ids = []
	for i, item in enumerate(tracks['items']):
		track = item['track']['id']
		if track is None:
			continue
		else:
			ids.append(track)
	return ids

if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username, limit=50)
    for playlist in playlists:
    	print('%s : %s') % (playlist['name'], playlist['id'])
    newList = sp.user_playlist_create(username, combinedPlaylistName, public=False)
    for playlistID in playlistArray:
    	results = sp.user_playlist(username, playlistID, fields="tracks,next")
    	tracks = results['tracks']
        trackIDs = getTracks(tracks)
        sp.user_playlist_add_tracks(username, newList['id'], trackIDs)
        while tracks['next']:
        	tracks = sp.next(tracks)
        	additionalTracks = getTracks(tracks)
        	sp.user_playlist_add_tracks(username, newList['id'], additionalTracks)
