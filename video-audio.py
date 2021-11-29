from moviepy.editor import*
mp4_file="testvideo.mp4"
mp3_file="navo.mp3"
videoclip=VideoFileClip(mp4_file)
audioclip=videoclip.audio
audioclip.write_audiofile(mp3_file)

