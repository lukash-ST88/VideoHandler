from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from src.utils.downloaders import download_youtube_file, download_torrent_file
from pydantic import BaseModel
from src.utils.handlers import handle_video
from enum import Enum


class VideoFileType(str, Enum):
    torrent = "torrent"
    YouTube = "YouTube"
    local = "local"


class VideoFile(BaseModel):
    type: VideoFileType
    video_path: str
    new_video_name: str


app = FastAPI(
    title='ToDoApp'
)

origins = [
    "http://localhost:8000",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)


@app.post("/video-handler")
async def manage_video(video_file: VideoFile):
    if video_file.type == "torrent":
        downloaded_video = download_torrent_file(video_file.video_path)
        handle_video(downloaded_video, video_file.new_video_name)
    elif video_file.type == "YouTube":
        downloaded_video = download_youtube_file(video_file.video_path)
        downloaded_folder = 'DownloadedVideo/'
        handle_video(downloaded_folder + downloaded_video, video_file.new_video_name)
    elif video_file.type == "local":
        handle_video(video_file.video_path, video_file.new_video_name)
    else:
        return {"error": "Video type is not supported, try YouTube, torrent or local type"}
    return {"success": "video is handled"}

# magnet:?xt=urn:btih:c9e15763f722f23e98a29decdfae341b98d53056&dn=Cosmos+Laundromat&tr=udp%3A%2F%2Fexplodie.org%3A6969&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Ftracker.empire-js.us%3A1337&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=wss%3A%2F%2Ftracker.btorrent.xyz&tr=wss%3A%2F%2Ftracker.fastcast.nz&tr=wss%3A%2F%2Ftracker.openwebtorrent.com&ws=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2F&xs=https%3A%2F%2Fwebtorrent.io%2Ftorrents%2Fcosmos-laundromat.torrent
# https://www.youtube.com/watch?v=NeQM1c-XCDc
