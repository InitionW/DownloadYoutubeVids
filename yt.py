from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}...")
        stream.download()
        print("Download complete!")
    except Exception as e:
        print("Error:", e)

def main():
    url = input("Enter the YouTube video URL: ")
    download_video(url)

if __name__ == "__main__":
    main()
