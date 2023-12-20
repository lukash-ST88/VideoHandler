from pytube import YouTube
from torrentp import TorrentDownloader, TorrentInfo


def download_youtube_file(video_url: str):
    my_video = YouTube(video_url)
    my_video.streams.get_highest_resolution().download("DownloadedVideo/")
    print(my_video)
    print(my_video.metadata)
    return my_video.title + ".mp4"


def download_torrent_file(torrent_file: str):
    torrent_file = TorrentDownloader(torrent_file, 'DownloadedVideo/')
    torrent_file.start_download()
    return torrent_file



