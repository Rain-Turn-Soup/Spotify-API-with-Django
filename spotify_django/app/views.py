from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Create your views here.

def spotify(request):
    justin_uri = 'spotify:artist:3WwGRA2o4Ux1RRMYaYDh7N'
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='8067fc4e38af43f698011dc914959b1f',
            client_secret='fa50ecef4af8499f92aa8e84245512d1',))

    results = spotify.artist_albums(justin_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])
    return render(request,'spotify.html',{'albums':albums})

def index(request):
    if request.method=='POST':
        artist_uri = request.POST.get('uri')
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='8067fc4e38af43f698011dc914959b1f',client_secret='fa50ecef4af8499f92aa8e84245512d1',))
        results = spotify.artist_top_tracks(artist_uri)
        final_result=results['tracks'][:5]
        return render(request,'base.html',{"results":final_result})
    else:
# for track in results['tracks'][:10]:
#     print('track    : ' + track['name'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()
      return render(request,'base.html',)
