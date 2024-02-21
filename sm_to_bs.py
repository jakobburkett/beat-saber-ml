import re as regex
import json
# from parse import *

# info.dat structure
info_dat = dict(
    _version = "2.0.0",
    _songName = "",
    _songSubName = "",
    _songAuthorName = "",
    _levelAuthorName = "",
    _beatsPerMinute = -1,
    _shuffle = 0,           # im not sure what these two mean exactly but they deal with
    _shufflePeriod = 0.0,   # "swing" stlye songs and the wiki says theyre rarely used
    _previewStartTime = 0.0,
    _previewDuration = 0.0,
    _songFileName = "",
    _coverImageFilename = "",
    _environmentName = "",
    _songTimeOffset = 0,
    # _customData = dict(),   # not gonna be using this
    _difficultyBeatmapSets = [
        
    ]
)

DBMS = dict( # "difficultyBeatmapSets"
    _beatmapCharacteristicName = "Standard",
    _difficultyBeatmaps = [
        # DIFF    
    ]
)

DIFF = dict(
    _difficulty = "Easy", #hardcoded
    _difficultyRank = 1,
    _beatmapFilename = "EasyStandard.dat", #hardcoded
    _noteJumpMovementSpeed = 8, # hardcoded, im not really sure what this means 
    _noteJumpStartBeatOffset = 0.0,
    # _beatmapColorSchemeIdx = 0, # Introduced in version 2.1.0 - shouldnt need
    # _environmentNameIdx = 0, # Introduced in version 2.1.0 - shouldnt need
    # _customData = dict()    # not gonna be using this
)


#difficulty.dat structure
difficulty_dat = dict(
    _version = "2.0.0", # i dont think its ever gonna not be 2.0.0
    _customData = dict( #custom data is not necessary and usually its children are not even populated
        # if nothing is in _customData it should be omitted
        _time = [], #number
        _BPMChanges = [], #this seems like a necesary element so im confused why its in _customData. I guess BS just handles notes differently.
        _bookmarks = [],
    ),
    _events = [ # optional 
        # EVENT
    ],
    _notes = [
        # NOTE
    ],
    _obstacles = [ # ignoring for now
        # OBSTACLE
    ]
)

#if a field doesnt have anything in it, dont make it a "dict." it messes with the bracket type which probably dont matter but just in case
EVENT = {
    # all lighting events are gonna be ignored for now cuz they
    # arent imortant to gameplay 
}

NOTE = dict(
    _time = [],
    _lineIndex = [],
    _lineLayer = [],
    _type = [],
    _cutDirection = [],
)

OBSTACLE = {
    # also just going to ignore these for now for simplicity's sake
}

def get_attribute(name):
    i = regex.search(name, sm)
    j = regex.search(";", sm[i.span()[0]:])

    return sm[i.span()[1]:(i.span()[0] + j.span()[0])] #nooo python is super readable guys!!!



# =================================================================
# ----------------------------- MAIN ------------------------------
# =================================================================

f = open("stepmania maps/MWOK's Stream Pack/Actualized/Actualized.sm", "r")
sm = f.read()


# ================= difficulty.dat file creation ==================


# get an array of arrays of measures
notes = []
measure = []
for line in sm.splitlines():
    if regex.search("^[0-4M]{4,4}", line):
        measure.append(line[0:4])

    if regex.search("^,|;", line) and measure.__sizeof__() != 40: # '40' is the size of measure if empty
        notes.append(measure.copy())
        measure.clear()

# get timing data
offset = get_attribute("#OFFSET:")

# get bpms (can be multiple things seperated by commas, ending in semicolon)
# tmp solution for no bpm changes (aka one 'change' starting at beat 0)
i = regex.search("#BPMS:", sm)
j = regex.search("\n;", sm[i.span()[0]:])
tmp = sm[i.span()[1]:(i.span()[0] + j.span()[0])]

starting_BPM = tmp.split('=')[1] # we can ignore the '0.00000=' cuz we know the BPM is going to be at the start anyway

# convert stepmania notes into beatsaber blocks
time = offset # starting time to be updated as the conversion happens
bpm_coef = float(starting_BPM) / 60

BS_NOTES = []
m = 0 # keep track of what measure were on
for mesr in notes:
    beats = len(mesr)
    l = 0 # to count what line were on to do math with the time var
    for line in mesr:
        j = 0 # to keep track of what arrow we're on
        for step in line:
            if step[0] != "0": # step detected, convert
                NOTE["_time"] = (m + (l / beats)) * 4
                NOTE["_lineIndex"] = j
                NOTE["_lineLayer"] = 1 # just gonna hardcode all blocks to be on the middle row
                NOTE["_type"] = 0 if j < 2 else 1
                NOTE["_cutDirection"] = 8 # dot block
                difficulty_dat["_notes"].append(NOTE.copy()) # "copy()" needed, python moment
            j += 1 #increment arrow counter going from left to right
        l += 1 #increment line counter
    m += 1 #increment measure counter

# print(json.dumps(difficulty_dat).replace(" ", ""))

difficulty_dat_file = open("EasyStandard.dat", "w")
difficulty_dat_file.write(json.dumps(difficulty_dat).replace(" ", "")) 


# ==================== info.dat file creation =====================


info_dat["_songName"] = get_attribute("#TITLE:")
info_dat["_songSubName"] = get_attribute("#SUBTITLE:")
info_dat["_songAuthorName"] = get_attribute("#ARTIST:") # this and the next line don't translate well between games
info_dat["_levelAuthorName"] = get_attribute("#CREDIT:")
info_dat["_beatsPerMinute"] = starting_BPM
# no stepmania equivalent for _shuffle & _shuffperiod afaik
info_dat["_previewStartTime"] = get_attribute("#SAMPLESTART:")
info_dat["_previewDuration"] = get_attribute("#SAMPLELENGTH:")
info_dat["_songFileName"] = get_attribute("#MUSIC:")
info_dat["_coverImageFileName"] = "" # again not really a good equivalent. There is a 'banner' in sm but that could be completely the wrong size so i dont wanna mess with it
info_dat["_environmentName"] = "DefaultEnvironment" #hardcoded, just for looks on bs' end
info_dat["_songTimeOffset"] = offset

# i know this looks like crap but it works ok
# all for the square brackets bro
DBMS["_difficultyBeatmaps"].append(DIFF)
info_dat["_difficultyBeatmapSets"].append(DBMS)

# print(json.dumps(info_dat))

info_dat_file = open("info.dat", "w")
info_dat_file.write(json.dumps(info_dat))
