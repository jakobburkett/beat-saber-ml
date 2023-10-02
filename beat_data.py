# start for a class that has the info in the info.dat files (may change based on file version?)

class Info:
    def __init__(self, version = None, song_name = None, song_sub_name = None, 
                 song_author = None, level_author = None, bpm = None, song_file = None,
                 cover_file = None, song_time_offset = None):
        self.version = "2.0.0" if version == None else version,
        self.song_name = "no_song_name" if song_name == None else song_name
        self.song_sub_name = "" if song_sub_name == None else song_sub_name
        self.song_author_name = "no_artist" if song_author == None else song_author
        self.level_author_name = "no_level_author" if level_author == None else level_author
        self.bpm = 120 if bpm == None else bpm
        self.shuffle = 0
        self.shuffle_period = 0.5
        self.preview_start_time = 61.70000076293945
        self.preview_duration = 17.299999237060547
        self.song_file_name = "song.egg" if song_file == None else song_file
        self.cover_file_name = "cover.jpg" if cover_file == None else cover_file
        self.environment_name = "NiceEnvironment"
        self.song_time_offset = 0 if song_time_offset == None else song_time_offset
        # self.customData:
        self.contributors = []