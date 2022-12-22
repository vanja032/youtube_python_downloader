from pytube import YouTube
import os
from os.path import exists

print("Youtube MP4 downloader")
file = open("urls.txt", "r")
urls = file.read().split("\n")
format = ".mp4"
destination = "<destination path>"

number = 0
for url in urls:
    number += 1
    try:
        print("[" + str(number) + "]" + " " + url)
        yt = YouTube(url)
        print(yt.title)
        if not exists(destination + "/" + str(number) + yt.title + format):
            video = yt.streams.get_highest_resolution()
            out_file = video.download(output_path=destination, filename=str(number) + yt.title)
            print("Finished")
        else:
            print("File exist!")
    except:
        try:
            os.remove(out_file)
            print("Removed " + out_file)
        except:
            pass
        continue
