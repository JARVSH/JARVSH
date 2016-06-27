'''
   author: Ashutosh Das
   email: mail@ashutoshdas.com
   
   This module is used to play youtube video from command line.

'''


import os
import time
import tts
import sys
from speech import speech

def youtube(video):
    pid=os.fork()
    if pid == 0:
        tts.tts("Going to play {}".format(video))
        video= "mpsyt ." + video + ",1"
        print("I entered this {0}".format(video))
        os.system(video)
        time.sleep(20)
    else:
        time.sleep(150)
        print("parent end\n")
        os.kill(pid, 9)

            

if __name__ == '__main__':
    youtube(sys.argv[1])


