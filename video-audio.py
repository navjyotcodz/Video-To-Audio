# Video-To-Audio
# A simple python tool which converts mp4 files into mp3 files.
# Author - navjyotcodz

from moviepy.editor import*
mp4_file="testvideo.mp4"
mp3_file="navo.mp3"
videoclip=VideoFileClip(mp4_file)
audioclip=videoclip.audio
audioclip.write_audiofile(mp3_file)
