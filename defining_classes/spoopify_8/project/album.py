from typing import List
from defining_classes.spoopify_8.project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.songs = list(songs)
        self.name = name

        self.published = False

    def add_song(self, song: Song):
        if song.singe:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        song = [s for s in self.songs if s.name == song_name]
        if not song:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        self.songs.remove(song[0])
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}" + "\n"
        for song in self.songs:
            result += "== " + song.get_info() + "\n"
        return result

    


