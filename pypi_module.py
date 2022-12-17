from spotify_recommender_api.recommender import start_api
from pprint import pprint

def spotify_funck():
    playlist_url = 'https://open.spotify.com/playlist/37i9dQZF1DWZeKCadgRdKQ?si=7fc19ce2a83c4592'
    user_id = '31o546n62u7ra6ieodewkwj5rmhi'
    token = ''
    api = start_api(playlist_url=playlist_url, user_id=user_id)
    api.playlist_to_csv()
    pprint(api.get_playlist())
    
if __name__ == '__main__':
    spotify_funck()