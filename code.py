#Make sure you have installed pytube3 on your system. If not done, follow these steps:-
#Open your anaconda or python3 app and use the following command:
# pip install pytube3
#This will install the pytube3 which will be required.

from pytube import Youtube

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)

#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")
