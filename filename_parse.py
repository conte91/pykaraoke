import os

"""
Functions to extract song informations from a filename.
"""

def ParseTitle(self, filepath, settings):
    """ Parses the file path and returns the title of the song. If the filepath cannot be parsed a KeyError exception is thrown. If the settings contains a file naming scheme that we do not support a KeyError exception is thrown."""
    title = ''
    # Make sure we are to parse information
    if settings.CdgDeriveSongInformation:
        if settings.CdgFileNameType == 0: # Disc-Track-Artist-Title.Ext
            # Make sure we can parse the filepath
            if len(filepath.split("-")) == 4:
                title = filepath.split("-")[3] # Find the Title in the filename
            else:
                raise KeyError("Invalid type for file: %s!" % filepath)
        elif settings.CdgFileNameType == 1: # DiscTrack-Artist-Title.Ext
            # Make sure we can parse the filepath
            if len(filepath.split("-")) == 3:
                title = filepath.split("-")[2] # Find the Title in the filename
            else:
                raise KeyError("Invalid type for file: %s!" % filepath)
        elif settings.CdgFileNameType == 2: # Disc-Artist-Title.Ext
            # Make sure we can parse the filepath
            if len(filepath.split("-")) == 3:
                title = filepath.split("-")[2] # Find the Title in the filename
            else:
                raise KeyError("Invalid type for file: %s!" % filepath)
        elif settings.CdgFileNameType == 3: # Artist-Title.Ext
            # Make sure we can parse the filepath
            if len(filepath.split("-")) == 2:
                title = filepath.split("-")[1] # Find the Title in the filename
            else:
                raise KeyError("Invalid type for file: %s!" % filepath)
        else:
            raise KeyError("File name type is invalid!")
        # Remove the first and last space
        title = title.strip(" ")
        # Remove the filename extension
        title = os.path.splitext(title)[0]
    #print "Title parsed: %s" % title
    return title

def ParseArtist(self, filepath, settings):
    """ Parses the filepath and returns the artist of the song. """
    artist = ''
    # Make sure we are to parse information
    if settings.CdgDeriveSongInformation:
        if settings.CdgFileNameType == 0: # Disc-Track-Artist-Title.Ext
            artist = filepath.split("-")[2] # Find the Artist in the filename
        elif settings.CdgFileNameType == 1: # DiscTrack-Artist-Title.Ext
            artist = filepath.split("-")[1] # Find the Artist in the filename
        elif settings.CdgFileNameType == 2: # Disc-Artist-Title.Ext
            artist = filepath.split("-")[1] # Find the Artist in the filename
        elif settings.CdgFileNameType == 3: # Artist-Title.Ext
            artist = filepath.split("-")[0] # Find the Artist in the filename
            artist = os.path.basename(artist)
        else:
            raise KeyError("File name type is invalid!")
        # Remove the first and last space
        artist = artist.strip(" ")
    #print "Artist parsed: %s" % artist
    return artist

def ParseDisc(self, filepath, settings):
    """ Parses the filepath and returns the disc name of the song. """
    disc = ''
    # Make sure we are to parse information
    if settings.CdgDeriveSongInformation:
        if settings.CdgFileNameType == 0: # Disc-Track-Artist-Title.Ext
            disc = filepath.split("-")[0] # Find the Disc in the filename
        elif settings.CdgFileNameType == 1: # DiscTrack-Artist-Title.Ext
            disc = filepath.mid(0, filepath.length - 2) # Find the Disc in the filename
        elif settings.CdgFileNameType == 2: # Disc-Artist-Title.Ext
            disc = filepath.split("-")[0] # Find the Disc in the filename
        elif settings.CdgFileNameType == 3: # Artist-Title.Ext
            disc = ''
        else:
            raise KeyError("File name type is invalid!")
        # Remove the first and last space
        disc = disc.strip(" ")
        # Remove the filename path
        disc = os.path.basename(disc)
    #print "Disc parsed: %s" % disc
    return disc

def ParseTrack(self, filepath, settings):
    """ Parses the file path and returns the track for the song. """
    track = ''
    # Make sure we are to parse information
    if settings.CdgDeriveSongInformation:
        if settings.CdgFileNameType == 0: # Disc-Track-Artist-Title.Ext
            track = filepath.split("-")[1] # Find the Track in the filename
        elif settings.CdgFileNameType == 1: # DiscTrack-Artist-Title.Ext
            track = filepath.mid(filepath.length - 2, 2) # Find the Track in the filename
        elif settings.CdgFileNameType == 2: # Disc-Artist-Title.Ext
            track = ''
        elif settings.CdgFileNameType == 3: # Artist-Title.Ext
            track = ''
        else:
            raise KeyError("File name type is invalid!")
        # Remove the first and last space
        #track = track.strip(" ")
    #print "Track parsed: %s" % track
    return track

def ParseMetadata(self, filepath, settings):
    return pykdb.SongMetadata(
        Title = ParseTitle(filepath, settings),    # Title for display in playlist
        Artist = ParseArtist(filepath, settings),  # Artist for display
        Disc = ParseDisc(filepath, settings),      # Disc for display
        Track = ParseTrack(filepath, settings)     # Track for display
        )
