from pytube import YouTube
import os
from os.path import exists

print("Youtube MP3 downloader")
file = open("urls.txt", "r")
urls = file.read().split("\n")
format = ".mp3"
destination = "<destination path>"

for url in urls:
    try:
        print(url)
        yt = YouTube(url)
        print(yt.title)
        if not exists(destination + "/" + yt.title + format):
            video = yt.streams.filter(only_audio=True).first()
            out_file = video.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + format
            os.rename(out_file, new_file)
            print("Finished")
        else:
            print("File exist!")
    except:
        continue
