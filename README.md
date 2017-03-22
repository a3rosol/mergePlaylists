# mergePlaylists
Spotify is removing the folder feature on iOS, this is a quick&amp;dirty approach to replace that feature
v 0.1


# Requirements 
* spotipy - Install with pip install spotipy
* your Spotify username - google it ;)
* your client ID and ~secret - get it at https://developer.spotify.com/my-applications and create one
* redirect URI - keep it the way it is, but add it during registration of your app

# shortcomings

There are a *lot* of shortcomings in this script. I threw this quickly together in 15mins and will improve these shortcomings in the future

As of now here are the problems:
* You have to manually enter the playlist IDs you want to merge
  * This is because I haven't found a different way to get those IDs since spotify removed Folder support from their API -.-
* Currently it only shows 50 playlists. There's an API limit and I was too lazy to get all of them. Will come in the next version though :)
* It's not pretty. Will probably not be fixed in the future. Deal with it.

# Pull requests

YAY! Just do it!

# Issues

If you find some errors, create an issue.
I'll try to fix it.