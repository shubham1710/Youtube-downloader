#Make sure you have installed pytube3 on your system. If not done, follow these steps:-
#Open your anaconda or python3 app and use the following command:
# pip install pytubeX
#This will install the pytubeX which will be required.

from pytube import YouTube

#Asking for all the video links
n = int(input("Enter the number of youtube videos to download:   "))

# A list to store all the links
links = []

# Asking for the links one per line
print("\nEnter all the links one per line:")

for i in range(0, n):
    temp = input()
    links.append(temp)

#Showing all details for videos and downloading them one by one
for i in range(0, n):
    link = links[i]
    yt = YouTube(link)
    print("\nDetails for Video", i+1, "\n")
    print("Title of video:   ", yt.title)
    print("Number of views:  ", yt.views)
    print("Length of video:  ", yt.length, "seconds")
    
    # Filter to select only progressive streams
    stream = str(yt.streams.filter(progressive=True))
    stream = stream[1:]
    stream = stream[:-1]
    streamlist = stream.split(", ")
    print("\nAll available options for downloads:\n")
    
    # loop around all available streams and print them for user to decide
    for i in range(0, len(streamlist)):
        st = streamlist[i].split(" ")
        print(i+1, ") ", st[1], " and ", st[3], sep='')
    
    # ask user the tag forthe stream to download
    tag = int(input("\nEnter the itag of your preferred stream to download:   "))
    ys = yt.streams.get_by_itag(tag)
    print("\nDownloading...")
    ys.download()
    print("\nDownload completed!!")
    print()
