# start for a class that has the info in the info.dat files (may change based on file version?)

class Difficulty_Beatmap_Sets:
    def __init__(self, difficulty, difficulty_rank, beatmap_filename)
        # these are the things that make up one
        # difficulty_rank = 1,
        #         beatmap_filename = "EasyStandard.dat",
        #         note_jump_movement_speed = 10,
        #         note_jump_start_beat_offset = 1.0399999618530273,
        #         editor_offset = 0,
        #         editor_old_offset = 0,
        #         warnings = ["EpilepsyWarning: Map contains flashing lights"],
        #         information = [],
        #         suggestions = [],
        #         requirements = []

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
        # probably able to do this with just a difficulty variable, all varables in the value of the dict is the same
        # self.difficulty_beatmap_sets = {
        #     "Easy": [
        #         difficulty_rank = 1,
        #         beatmap_filename = "EasyStandard.dat",
        #         note_jump_movement_speed = 10,
        #         note_jump_start_beat_offset = 1.0399999618530273,
        #         editor_offset = 0,
        #         editor_old_offset = 0,
        #         warnings = ["EpilepsyWarning: Map contains flashing lights"],
        #         information = [],
        #         suggestions = [],
        #         requirements = []
        #     ],
        #     "Normal": [
        #         difficulty_rank = 3,
        #         beatmap_filename = "NormalStandard.dat",
        #         note_jump_movement_speed = 10,
        #         note_jump_start_beat_offset = 0.9900000095367432,
        #         editor_offset = 0,
        #         editor_old_offset = 0,
        #         warnings = ["EpilepsyWarning: Map contains flashing lights"],
        #         information = [],
        #         suggestions = [],
        #         requirements = []
        #     ],
        #     "Hard": [
        #         difficulty_rank = 5,
        #         beatmap_filename = "HardStandard.dat",
        #         note_jump_movement_speed = 13,
        #         note_jump_start_beat_offset = 0.2590000033378601,
        #         editor_offset = 0,
        #         editor_old_offset = 0,
        #         warnings = ["EpilepsyWarning: Map contains flashing lights"],
        #         information = [],
        #         suggestions = [],
        #         requirements = []
        #     ],
        #     "Expert": [
        #         difficulty_rank = 7,
        #         beatmap_filename = "ExpertStandard.dat",
        #         note_jump_movement_speed = 13,
        #         note_jump_start_beat_offset = -0.20000000298023224,
        #         editor_offset = 0,
        #         editor_old_offset = 0,
        #         warnings = ["EpilepsyWarning: Map contains flashing lights"],
        #         information = [],
        #         suggestions = [],
        #         requirements = []
        #     ],
        #     "ExpertPlus": [
        #         difficulty_rank = 9,
        #         beatmap_filename = "ExpertPlusStandard.dat",
        #         note_jump_movement_speed = 19,
        #         note_jump_start_beat_offset = -0.5,
        #         editor_offset = 0,
        #         editor_old_offset = 0,
        #         warnings = ["EpilepsyWarning: Map contains flashing lights"],
        #         information = [],
        #         suggestions = [],
        #         requirements = []
        #     ]
        # }