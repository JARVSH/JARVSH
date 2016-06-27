import os
from speech import speech
def robotBrain():
    while(1):
        txt = speech()
        control = 'sudo python robot.py "{0}"'.format(txt)
        print(control)
        os.system(control)
        if( 'stop' in txt):
            break
