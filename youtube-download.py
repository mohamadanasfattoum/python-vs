'''
from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)
'''


from pytube import YouTube

# Enter the URL of the YouTube video you want to download
video_url = "https://www.youtube.com/watch?v=o9l1TOxYxGY&ab_channel=OmarFatoom"

try:
    # Create a YouTube object with the video URL
    yt = YouTube(video_url)

    # Get the highest resolution stream
    stream = yt.streams.get_highest_resolution()

    # Download the video
    print("Downloading video...")
    stream.download()
    print("Video downloaded successfully!")

except Exception as e:
    print("An error occurred while downloading the video:", str(e))