"""
Author: Asish Panda
email: asishrocks95@gmail.com



The main module to parse user's input for an output. This is meant to be used directly by the
main module responisble for running the whole server. The user's input should be converted
to string and passed here.
"""

from parse import parse
from KEYS import LOCATION, STATE, CLIENTS


class main:
    #this will not handle if there are two clients mentioned in a single
    #string or user's input. For eg "switch on the light and the fan"
    #This will also not handle the location of a given client.


    def __init__(self, string):
        #create parse objecti
        try:
            
            self.engine = parse(string)
            self.chunk = self.engine.parse()
            self.get_keys()
            self.get_command()

        except:
            raise ValueError("input must be a string")


    def get_keys(self):
        #extract the keywords from the chunk

        self.keys = []
        for word in self.chunk:
            if type(word) is not tuple:
                for key in word:
                    self.keys.append(key)
                    

    def get_command(self):

        self.client = []
        self.state = []
        self.location = []
        for x in self.keys:
            if x[0] in CLIENTS:
                self.client.append(x[0])

            elif x[0] in LOCATION:
                self.location.append(x[0])

            elif x[0] in STATE:
                self.state.append(x[0])
                
    def execute(self):
        if len(self.client) > 1:
            raise NotImplementedError("Only one client command supported at this time")
        
        cl = self.client[0]
        if cl == 'fan':
            #call fan module
            #fan(cl, self.state[0], self.location[0])

            raise NotImplementedError("No module to work with fan")

        elif cl == 'light' or cl == 'tubelight':
            #call light module
            #light(cl, self.state[0], self.location[0])

            raise NotImplementedError("No module work with light")

            
if __name__ == '__main__':
    #get user's input
    #string = voice()
    #do = main(string)

    do = main("switch of the light")
    print(do.keys)
    do.execute()
