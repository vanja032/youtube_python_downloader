from pytube import YouTube
import os
from os.path import exists

print("Youtube MP3 downloader")
file = open("urls.txt", "r")
urls = file.read().split("\n")
format = ".mp3"
destination = "<destination path>"

number = 0
for url in urls:
    number += 1
    try:
        print("[" + str(number) + "]" + " " + url)
        yt = YouTube(url)
        print(yt.title)
        if not exists(destination + "/" + str(number) + " " + yt.title + format):
            video = yt.streams.filter(only_audio=True).first()
            if "/" in yt.title:
                out_file = video.download(output_path=destination, filename=str(number) + " " + yt.title.replace("/", "-"))
            else:
                out_file = video.download(output_path=destination, filename=str(number) + " " + yt.title)
            base, ext = os.path.splitext(out_file)
            new_file = base + format
            os.rename(out_file, new_file)
            print("Finished")
        else:
            print("File exist!")
    except:
        try:
            os.remove(out_file)
            print("Removed " + out_file)
        except:
            print("Error")
            pass
        continue
