from pytube import YouTube

link = input("Enter YouTube Link: ")
yt = YouTube(link)
videos = yt.streams.all()
video = list(enumerate(videos))
for i in video:
	print(i)

print("Enter the formart")
dn_option = int(input("Ente the option(0, 1 or 2):"))
dn_video = videos[dn_option]
dn_video.download()

print(" Download complete")
