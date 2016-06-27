'''
   author: Ashutosh Das
   email: mail@ashutoshdas.com

   This module sends query to wolframalpha and return pods.
   
   Have to process the pods.

   Example
   =======

   @raspberrypi ~/project/smartHome/JARVSH $ python wolfram.py "How are you"
   you entered: How are you
   I am doing well, thank you.
   
'''
import tts
import wolframalpha
from speech import speech as s

# Get a free API key at http://products.wolframalpha.com/api/
# Only 2000 queries per month, so please get your own API key
app_id='YOUR-API-KEY'      #use this key for testing purpose only

def wolf(string):
    flag = 0
    client = wolframalpha.Client(app_id)
    print("you entered: {0}".format(string))
    res = client.query(string)
    #print(next(res.results).text)
    if len(res.pods) > 0:
        texts = ""
        pod = res.pods[1]
        if pod.text:
            texts = pod.text
        else:
            texts = "Sorry,No annswer for that"
        texts = texts.encode('ascii', 'ignore')
        texts = texts.split('\n')
        
        if(len(texts)>1):
            tts.tts("there are {0}".format(texts[-1]))
            tts.tts("{0}".format(texts[-2]))
            flag = 1
        tts.tts("{0}".format(texts[0]))
        if(flag == 1):
            tts.tts("Should I read more meanings?")
            speech = s()
            if ('yes' or 'yeah' or 'yup' or 'yo' in speech):
                tts.tts(speech[1:len(texts)-2])
                
    else:
        tts.tts("Sorry, something seems wrong. ")

if __name__ == '__main__':
    import sys
    wolf(sys.argv[1])

