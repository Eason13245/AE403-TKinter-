from pytube import YouTube

progress = 0
res_text = 0
res_level = 0

def showProgress(stream, chunk, bytes_remaining):
    size = stream.filesize

    global progress
    preProgress = progress

    currentProgress = (size - bytes_remaining) *100 // size
    progress = currentProgress

    if progress == 100:
        print("Download finish!")

    elif preProgress != progress:
        print("Currrent progress" + str(progress) + "%")

res_level = int(input(print("What is te res for the video?")))

def res_levels(an,res_text,res_level):

    if res_level == 144:
        res_text = "144p"

    elif res_level == 240:
        res_text = "240p"

    elif res_level == 3600:
        res_text = "360p"

    elif res_level == 480:
        res_text = "480p"

    elif res_level == 720:
        res_text = "720p"

    else:
        print("Please type it again.")

yt = YouTube('https://www.youtube.com/watch?v=dy90tA3TT1c', on_progress_callback= showProgress)

stream = yt.streams.filter(res= res_level, fps = 60).first()

stream.download("/Users/gaoyixun/Desktop", "Downloaded_video_" + str(res_text))