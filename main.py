# pip install pytubefix
# docs: https://pytube.io/en/latest/user/quickstart.html
from pytubefix import Playlist
from pytubefix import YouTube


def calculate_playlist_time(playlist_link: str):
    p = Playlist(playlist_link)
    time = 0
    for url in p.video_urls:
        yt = YouTube(url)
        time += yt.length
    print(f'# videos: {p.length}')
    print(f'hour: {time//3600} | minute: {(time%3600)//60} | second: {time%60}')
    
def download_playlist(playlist_link: str, save_path: str):
    # playlist_path = 'https://youtube.com/playlist?list=...'
    p = Playlist(playlist_link)

    for video in p.videos:
        print(f'Downloading: {video.title}')
        video.streams.filter(progressive=True, file_extension='mp4').first().download(output_path=save_path)
    
def download_video(video_link: str, save_path: str):
    yt = YouTube(video_link)
    yt.streams.filter(progressive=True, file_extension='mp4').first().download(output_path=save_path)

if __name__ == '__main__':
    video_link = '<url>'
    save_path = 'path/to/the/dir'
    download_video(video_link, save_path)
