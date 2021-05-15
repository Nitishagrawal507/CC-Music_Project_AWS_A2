from assessment2.models import aws_login, aws_subs, aws_img, aws_music
from flask import render_template, request, redirect
from assessment2.v import v
import urllib.parse


@v.route('/', methods=['GET', 'POST'])
def index():
    email = request.cookies.get('email')

    if email:
        uname = aws_login.get_user(email).get('user_name')
        subssong_result = aws_subs.get_user_subscriptions(email)

        subs = []
        for ret_details in subssong_result:
            artist, title = separate_song_key(ret_details['artist#title'])

            song = aws_music.get_song(artist, title)
            song['db_url'] = aws_img.get_image_url(artist + '.jpg')
            subs.append(song)

        scan_error = ''
        scan_songs = None
        if request.method == 'POST':
            artist_query = request.form['artist'] if 'artist' in request.form else None
            title_query = request.form['title'] if 'title' in request.form else None
            year_query = request.form['year'] if 'year' in request.form else None

            scan_songs = aws_music.scan_music(artist_query, title_query, year_query)
            print(scan_songs)
            if scan_songs:
                for song in scan_songs:
                    song['db_url'] = aws_img.get_image_url(song['artist'] + '.jpg')
            else:
                scan_error = 'No result is retrieved. Please query again'

        return render_template('main.html',
                               user_name=uname,
                               subscriptions=subs,
                               scan_songs=scan_songs,
                               scan_error=scan_error
                               )
    else:
        return redirect('/login')

# eg. here can be '/remove_subscription'
# similarly every route should be explicitly defined
# this would also affect the page redirection and also in frontend code
@v.route('/remove', methods=['POST'])
def remove_subscription():
    song_key = request.form['song_key']
    email = request.cookies.get('email')
    aws_subs.remove_subscription(email, song_key)
    return redirect('/')


@v.route('/subscribe', methods=['POST'])
def add_subscription():
    song_key = request.form['song_key']
    email = request.cookies.get('email')
    aws_subs.add_subscription(email, song_key)
    return redirect('/')


def separate_song_key(song_key):
    key_splits = song_key.split('#', 1)
    return key_splits[0], key_splits[1]
