"""A video player class."""

from Google_Challenge.video_library import VideoLibrary
from Google_Challenge.video_playlist import Playlist
from random import choice  # from solution 2


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self.the_playing_video = None
        self.the_pausing_video = False

        self.the_video_lib = VideoLibrary()
        self.the_list = {}

    def number_of_videos(self):
        video_count = len(self.the_video_lib.get_all_videos())
        print(f"{video_count} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("here's a list of all available videos:")
        file = open('videos.txt', 'r')
        print(file.read())
        file.close()

        '''other methods
        Ⅰ
        videoList=list(['Funny Dogs | funny_dogs__id |  #dog , #animal'\n
                        'Amazing Cats | amazing_cats__id |  #cat , #animal'\n
                        'Another Cat Video | another_cat__id |  #cat , #animal'\n
                        'Life at Google_Challenge | life_at_google__id |  #google , #career'\n
                        'Video about nothing | nothing__id |'])
        print(videoList)

        Ⅱ
        for video in sorted(self.the_video_lib.get_all_videos(), key=lambda x: x.title):
            print(video) //from solution 2
        '''

    def play_video(self, _id):
        """Plays the respective video.

        Args:
            _id: The _id to be played.
        """
        video = self.the_video_lib.get_video(_id)

        if video.flag is not None:
            print(f"Cannot play video: Video is currently flagged (reason: {video.flag})")
            return

        if video is None:
            print("Cannot play video: Video does not exist")
            return

        if self.the_playing_video:
            self.stop_video()

        print(f"Playing video: {video.title}")
        self.the_playing_video = video

        '''other methods that could not be implemented because of fixed structure

        input_playing_video = input('')
        bool playing_amazing_cats_video = False
        bool playing_another_cat__id = False
        bool playing_funny_dogs__id = False
        bool playing_life_at_google__id = False
        bool playing_nothing__id = False

        if input_playing_video == 'PLAY_amazing_cats__id':
            print('Playing video: Amazing Cats')
            playing = True

        elif input_playing_video == 'PLAY_another_cat__id':
            print('Playing video: Another Cat Video')
            playing = True

        elif input_playing_video == 'PLAY_funny_dogs__id':
            print('Playing video: Funny Dogs')
            playing = True

        elif input_playing_video == 'PLAY_life_at_google__id)':
            print('Playing video: Life at Google_Challenge')
            playing = True

        elif input_playing_video == 'nothing__id':
            print('Playing video: Video about nothing')
            playing = True

        else:
            print('Cannot play video: Video does not exist')
        '''

    def stop_video(self):
        """Stops the current video."""

        self.the_pausing_video = False
        self.the_playing_video = None

        if self.the_playing_video is None:
            print("Cannot stop video: No video is currently playing")
            return

        print(f"Stopping video: {self.the_playing_video.title}")

    '''
    input_pausing_video = input('')
    if input_pausing_video == 'STOP' and playing = True:

    elif input_pausing_video == 'STOP' and playing = True:
        print('Pausing video:)

    elif input_pausing_video == 'STOP' and playing = True:
        print('Pausing video:)

    elif input_pausing_video == 'STOP' and playing = True:
        print('Pausing video:)

    elif input_pausing_video == 'STOP' and playing = True:
        print('Pausing video:)

    else:
        pass
    '''

    def play_random_video(self):
        """Plays a random video from the video library."""

        if self.the_playing_video:
            self.stop_video()

        videos = [v for v in self.the_video_lib.get_all_videos() if v.flag is None]

        if not videos:
            print("No videos available")
            return

        self.play_video(choice(videos)._id)

    def pause_video(self):
        """Pauses the current video."""

        self.the_pausing_video = True

        if self.the_pausing_video:
            print(f"Video already paused: {self.the_playing_video.title}")
            return

        elif self.the_playing_video is None:
            print("Cannot pause video: No video is currently playing")
            return

        print(f"Pausing video: {self.the_playing_video.title}")

    def continue_video(self):
        """Resumes playing the current video."""

        self.the_pausing_video = False

        if self.the_playing_video is None:
            print("Cannot continue video: No video is currently playing")
            return

        elif not self.the_pausing_video:
            print("Cannot continue video: Video is not paused")
            return

        print(f"Continuing video: {self.the_playing_video.title}")

    def show_playing(self):
        """Displays video currently playing."""

        if not self.the_playing_video:
            print("No video is currently playing")
            return

        print(f"Currently playing: {self.the_playing_video}{' - PAUSED' if self.the_pausing_video else ''}")

    def create_playlist(self, _name):
        """Creates a playlist with a given name.

        Args:
            _name: The playlist name.
        """
        if _name.lower() in self.the_list:
            print("Cannot create playlist: A playlist with the same name already exists")
            return

        print(f"Successfully created new playlist: {_name}")

        self.the_list[_name.lower()] = Playlist(_name)

    def add_to_playlist(self, _name, _id):
        """Adds a video to a playlist with a given name.

        Args:
            _name: The playlist name.
            _id: The _id to be added.
        """
        video = self.the_video_lib.get_video(_id)

        if _name.lower() not in self.the_list:
            print(f"Cannot add video to {_name}: Playlist does not exist")
            return

        if not video:
            print(f"Cannot add video to {_name}: Video does not exist")
            return

        if video.flag is not None:
            print(f"Cannot add video to {_name}: Video is currently flagged (reason: {video.flag})")
            return

        playlist = self.the_list[_name.lower()]

        if video in playlist.videos:
            print(f"Cannot add video to {_name}: Video already added")
            return

        playlist.videos.append(self.the_video_lib.get_video(_id))
        print(f"Added video to {_name}: {video.title}")

    def show_allthe_list(self):
        """Display all playlists."""

        if not self.the_list:
            print("No playlists exist yet")
            return

        print("Showing all playlists:")

        for playlist in sorted(self.the_list):
            print(f"{self.the_list[playlist].name}")

    def show_playlist(self, _name):
        """Display all videos in a playlist with a given name.

        Args:
            _name: The playlist name.
        """
        if _name.lower() not in self.the_list:
            print(f"Cannot show playlist {_name}: Playlist does not exist")
            return

        playlist = self.the_list[_name.lower()]

        print(f"Showing playlist: {_name}")

        if not playlist.videos:
            print("No videos here yet")

        for video in playlist.videos:
            print(video)

    def remove_from_playlist(self, _name, _id):
        """Removes a video to a playlist with a given name.

        Args:
            _name: The playlist name.
            _id: The _id to be removed.
        """
        if _name.lower() not in self.the_list:
            print(f"Cannot remove video from {_name}: Playlist does not exist")
            return

        playlist = self.the_list[_name.lower()]
        video = self.the_video_lib.get_video(_id)

        if not video:
            print(f"Cannot remove video from {_name}: Video does not exist")
            return

        if video not in playlist.videos:
            print(f"Cannot remove video from {_name}: Video is not in playlist")
            return

        print(f"Removed video from {_name}: {video.title}")

        playlist.videos.remove(video)

    def clear_playlist(self, _name):
        """Removes all videos from a playlist with a given name.

        Args:
            _name: The playlist name.
        """
        if _name.lower() not in self.the_list:
            print(f"Cannot clear playlist {_name}: Playlist does not exist")
            return

        print(f"Successfully removed all videos from {_name}")

        self.the_list[_name.lower()].videos = []

    def delete_playlist(self, _name):
        """Deletes a playlist with a given name.

        Args:
            _name: The playlist name.
        """

        if _name.lower() not in self.the_list:
            print(f"Cannot delete playlist {_name}: Playlist does not exist")
            return

        print(f"Deleted playlist: {_name}")

        self.the_list.pop(_name.lower())

    def output_search_res(self, res, val):
        """Displays search res.

        Args:
            res: List of Videos, the search res.
            val: The val used to search.
        """
        if not res:
            print(f"No search res for {val}")
            return

        res = sorted(res, key=lambda x: x.title)

        print(f"Here are the res for {val}:")

        for i, result in enumerate(res):
            print(f"{i + 1}) {result}")

        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        num = input()

        if num.isnumeric() and 0 <= int(num) <= len(res):
            self.play_video(res[int(num) - 1]._id)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        res = []

        for video in self.the_video_lib.get_all_videos():
            if search_term.lower() in video.title.lower() and video.flag is None:
                res.append(video)

        self.output_search_res(res, search_term)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        res = []

        for video in self.the_video_lib.get_all_videos():
            if video_tag.lower() in video.tags and video.flag is None:
                res.append(video)

        self.output_search_res(res, video_tag)

    def flag_video(self, _id, flag_reason="Not supplied"):
        """Mark a video as flagged.

        Args:
            _id: The _id to be flagged.
            flag_reason: Reason for flagging the video.
        """

        video = self.the_video_lib.get_video(_id)

        if not video:
            print("Cannot flag video: Video does not exist")
            return

        if video.flag is not None:
            print("Cannot flag video: Video is already flagged")
            return
        video.set_flag(flag_reason)

        if self.the_playing_video and self.the_playing_video._id == video._id:
            self.stop_video()

        print(f"Successfully flagged video: {video._title} (reason: {flag_reason})")

    def allow_video(self, _id):
        """Removes a flag from a video.

        Args:
            _id: The _id to be allowed again.
        """

        video = self.the_video_lib.get_video(_id)

        if not self.the_video_lib.get_video(_id):
            print("Cannot remove flag from video: Video does not exist")
            return

        if not video.flag:
            print("Cannot remove flag from video: Video is not flagged")
            return

        print(f"Successfully removed flag from video: {video.title}")

        video.set_flag(None)

