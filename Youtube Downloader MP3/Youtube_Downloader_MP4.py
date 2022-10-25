from pytube import YouTube
import os
from os.path import exists

print("Youtube MP4 downloader")
file = open("urls.txt", "r")
urls = file.read().split("\n")
format = ".mp4"
destination = "<destination path>"

for url in urls:
    try:
        print(url)
        yt = YouTube(url)
        print(yt.title)
        if not exists(destination + "/" + yt.title + format):
            video = yt.streams.get_highest_resolution()
            out_file = video.download(output_path=destination)
            print("Finished download " + yt.title)
        else:
            print("File exist!")
    except:
        continue
