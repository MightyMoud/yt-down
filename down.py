import pytube
from tqdm import tqdm

playlist_link = "https://www.youtube.com/watch?v=7z3i6JPUqws&list=PLpu1p7deoYJjNHEfOR2O_H8FYgKOfSson"
# video_url = "https://www.youtube.com/watch?v=BlVwbVygVrM"

# audio = pytube.YouTube(video_url).streams.get_audio_only()
# audio.download("video/")

playlist = pytube.Playlist(playlist_link)

print("Downloadng the videos from the playlist")
songs_list = ""
for index, video in enumerate(tqdm(playlist.videos), start=1):
    audio = video.streams.get_audio_only("mp4")
    file_name = f"{index} - {video.title}"
    songs_list += file_name + "\n"
    # print(f"Dowloading the audio of {audio.title}")
    audio.download(output_path="audio/", filename_prefix=f"{index} - ")


with open("songs_list.txt", "w") as f:
    f.write(songs_list)
