
import sys
from subprocess import getstatusoutput


#ffmpeg -i video.avi ~/Desktop/VideoDemo/sample/%03d.bmp

def split(filename,filepath):
    p = "\n = EMPTY RETURN"

    #current file path is ~/desktop/videodemo/
    # call in here is    ffmpeg -i + ' ' + sample/%03d.jpg
    # set a variable to store the absolute path then concat with the desired directory
    cmnd = 'ffmpeg -i '+filename +' '+ filepath + '/%03d.jpg '
    p = getstatusoutput([cmnd])
    return True

def unsplit(directory):
    cmnd = 'ffmpeg -i ' +directory+' /%03d.jpg sample/test.avi'
    p = getstatusoutput([cmnd])
    print('Done')