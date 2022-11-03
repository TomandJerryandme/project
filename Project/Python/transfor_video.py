import sys
import os

from ffmpy import FFmpeg

for x in os.walk(r"D:\Visual_Studio_Code\Project\videoMP4"):
    print(x)
# ff = FFmpeg(r"D:\Ffmpeg\ffmpeg-4.3.1-2021-01-01-essentials_build\bin\ffmpeg.exe", inputs={r"D:\Visual_Studio_Code\Project\videoMP4\video1666782766932285.mp4": None}, outputs={r"D:\abc.mp4": ['-v', 'quiet', '-c', 'copy']})
# ff.run()