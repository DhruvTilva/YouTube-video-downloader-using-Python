from pytube import YouTube
link= input("Enter the Video URL:")
youtube_1= YouTube(link)
print("Please Wait Fetching Processing...............")

# print(youtube_1.title) #for get link title
# print(youtube_1.thumbnail_url) #to get the thumbnail phto url

# videos= youtube_1.streams.all() #display all formate list
# videos= youtube_1.streams.filter(only_audio=True) #to get only audio formate list
videos= youtube_1.streams.filter(only_video=True)  #to get only videos formate
vid= list(enumerate(videos)) #list ma number get index with enumerate
for i in vid:
    print(i) #print data on list

strm= int(input("enter the index of  quality you want!:"))
videos[strm].download()
print(" Video Download Successfully!")

