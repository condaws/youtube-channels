from secrets import api_key
from googleapiclient.discovery import build

youtube = build('youtube', 'v3', developerKey = api_key)

channels = [
    'UCVls1GmFKf6WlTraIb_IaJg'
]

for channel in channels:
    request = youtube.search().list(
        part='snippet',
        channelId=channel,
        maxResults=7,
        order='date',
        type='video'
    )

    response = request.execute()
    print(response)
