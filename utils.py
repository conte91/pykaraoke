import os

def getHomeDirectory():
    """ Returns the user's home directory, if we can figure that
    out. """
    # First attempt: ask wx, if it's available.
    try:
        import wx
        return wx.GetHomeDir()
    except:
        pass

    # Second attempt: look in $HOME
    home = os.getenv('HOME')
    if home:
        return home

    # Give up and return the current directory.
    return '.'
