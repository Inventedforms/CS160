#!/usr/bin/python3
import sys
from subprocess import getstatusoutput


#ffmpeg -i video.avi ~/Desktop/VideoDemo/sample/%03d.bmp

def ffmpeg_VidtoImg(video, file):
    #path = '~/Desktop/VideoDemo/sample/%03d.bmp'
    #cmnd = 'ffmpeg -i '+filename
    #print ('#####    INIT    #####')

    p = "\n = EMPTY RETURN"
    cmnd = 'ffmpeg -i '+video + ' ' + file + '/%03d.jpg '
    p = getstatusoutput([cmnd])
    #subprocess.check_output([cmnd])
    return p

        
