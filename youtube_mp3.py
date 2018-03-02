import os
import subprocess
import pytube

list = ["https://www.youtube.com/watch?v=JB-vcBj_X5o"]
# list.append("https://www.youtube.com/watch?v=0RGIIBLI3rI")
# list.append("https://www.youtube.com/watch?v=tEpLqkMRY6k")
# list.append("https://www.youtube.com/watch?v=AdjFL1xr4K8")
# list.append("https://www.youtube.com/watch?v=5dHcVjj_Kq0")
# list.append("https://www.youtube.com/watch?v=aW4ebaprPnw")
# list.append("https://www.youtube.com/watch?v=ZEdZqZy9Yr0")

down_dir = "F:\음악\youtube-mp3"
for i in range(len(list)):
    youtube = pytube.YouTube(list[i])
    default_filename = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().default_filename
    if len(default_filename) > 0:
        youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(down_dir)
        subprocess.call(['ffmpeg', '-i',  # cmd 명령어 수행
                         os.path.join(down_dir, default_filename),
                         os.path.join(down_dir, default_filename.replace("mp4","mp3"))
                         ])

