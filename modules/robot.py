'''
   author: Ashutosh Das
   email: mail@ashutoshdas.com
   
   Module to control robot.

'''

import RPi.GPIO as G
from tts import tts
    
def robot(dire):
    G.setmode(G.BCM)
    G.setwarnings(False)
    G.setup(23, G.OUT)
    G.setup(24, G.OUT)
    G.setup(14, G.OUT)
    G.setup(15, G.OUT)
    if ('clean' in dire):
        tts("i do not have hardware to clean house, so sorry")
    if ( 'stop' in dire):
        G.output(23, G.LOW)
        G.output(24, G.LOW)
        G.output(14, G.LOW)
        G.output(15, G.LOW)
    if ( 'forward' in dire):
        G.output(23, G.LOW)
        G.output(24, G.LOW)
        G.output(14, G.HIGH)
        G.output(15, G.HIGH)
    if ( 'backward' in dire):
        G.output(23, G.HIGH)
        G.output(24, G.HIGH)
        G.output(14, G.LOW)
        G.output(15, G.LOW)
    if ( 'left' in dire):
        G.output(23, G.LOW)
        G.output(24, G.HIGH)
        G.output(14, G.HIGH)
        G.output(15, G.LOW)
    if ( 'right' in dire):
        G.output(23, G.HIGH)
        G.output(24, G.LOW)
        G.output(14, G.LOW)
        G.output(15, G.HIGH)



if __name__ == '__main__':
    import sys
    robot(sys.argv[1])

