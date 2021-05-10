import json
import boto3

def load(music, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('music')
    for song in music['songs']:
        artist = song['artist']
        title = song['title']

        print("Adding music:", artist, title)
        table.put_item(Item=song)

if __name__ == '__main__':
    with open("../a2.json") as json_file:
        music_list = json.load(json_file)
        load(music_list)
