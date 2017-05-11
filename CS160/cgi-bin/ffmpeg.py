import sys
from subprocess import getstatusoutput


#ffmpeg -i video.avi ~/Desktop/VideoDemo/sample/%03d.bmp

def split(filename,filepath):
    p = "\n = EMPTY RETURN"

    #current file path is ~/desktop/videodemo/
    # call in here is    ffmpeg -i + ' ' + sample/%03d.jpg
    # set a variable to store the absolute path then concat with the desired directory
    cmnd = 'ffmpeg -i '+filename +' '+ filepath + '/%d.jpg '
    p = getstatusoutput([cmnd])
    #print(p)
    return p
#unsplit(file, videoname, codec)
def unsplit(directory, videoname):
    #print ('#####    INIT    #####')
    cmnd = 'ffmpeg -i ' +directory+'/%d.jpg -vcodec libx264 -vcodec libx264 -vf scale=640:-2,format=yuv420p ' + videoname +'_NEW.mp4'
    #cmnd = 'ffmpeg -i ' +directory+'/%03d.jpg -vcodec '+codec +' sample/test.avi'
    p = getstatusoutput([cmnd])
    return p
#git audio
def extractMp3(filename,filepath):
    cmnd = 'ffmpeg -i '+filename +' '+ filepath + filename + 'SOUND.mp3'
    p = getstatusoutput([cmnd])