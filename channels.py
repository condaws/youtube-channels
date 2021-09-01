from secrets import api_key
from datetime import datetime
from googleapiclient.discovery import build

def valid_date(date_published):
    clean_date = date_published[0:10].split('-')

    final_date = datetime(
        int(clean_date[0]),
        int(clean_date[1]),
        int(clean_date[2])
    )

    elapsed_time = datetime.utcnow() - final_date

    if elapsed_time.days > 6:
        return False
    else:
        return True


def get_videos():
    youtube = build('youtube', 'v3', developerKey = api_key)

    # input desired channel IDs here
    channels = [
        'UCVls1GmFKf6WlTraIb_IaJg'
    ]

    video_ids = []

    # make a GET request to youtube data api for each channel
    for channel in channels:
        request = youtube.search().list(
            part='snippet',
            channelId=channel,
            maxResults=7,
            order='date',
            type='video'
        )

        response = request.execute()

        for item in response['items']:
            if valid_date(item['snippet']['publishedAt']):
                video_ids.append(item['id']['videoId'])

        return video_ids


if __name__ == "__main__":
    print(get_videos())

