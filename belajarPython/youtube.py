from pytube import YouTube
link = input("https://youtu.be/6wUjZPjDSbI")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
