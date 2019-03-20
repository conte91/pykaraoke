#!/usr/bin/env python3
import ctypes
import sys
import vlc
import time

videowidth = 4096
videoheight = 4096
size = videowidth * videoheight * 4
buf = (ctypes.c_ubyte * size)()
buf_p = ctypes.cast(buf, ctypes.c_void_p)

CorrectVideoLockCb = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
@CorrectVideoLockCb
def _lockcb(opaque, planes):
    print("lock", file=sys.stderr)
    planes[0] = buf_p

class VlcAudio():
    def __init__(self, filename):
        self.instance = vlc.Instance()


        #Create a MediaPlayer with the default instance
        self.player = self.instance.media_player_new()
        #Load the media file
        self.media = self.instance.media_new(filename)
        vlc.libvlc_video_set_callbacks(self.player, _lockcb, None, None, None)

    def play(self):
        #Add the media to the player
        self.player.set_media(self.media)
        self.player.play()

    def pause(self):
        self.player.set_pause(1)

    def stop(self):
        self.player.stop()

    def unpause(self):
        self.player.set_pause(0)

    def getTime(self):
        return self.player.get_time()

    def volumeUp(self):
        volume = self.player.audio_get_volume()
        volume = min(volume + 10, 100)
        self.player.audio_set_volume(volume)

    def volumeDown(self):
        volume = self.player.audio_get_volume()
        volume = min(volume - 10, 0)
        self.player.audio_set_volume(volume)

    def getVolume(self):
        return self.player.audio_get_volume()
