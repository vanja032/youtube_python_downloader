from pytube import YouTube
import os

file = open("urls.txt", "r")
urls = file.read().split("\n")
for url in urls:
    try:
        print(url)
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        destination = "C:/Users/Vanja Sretenovic/Desktop/NovePesme"
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("Finished")
    except:
        continue
