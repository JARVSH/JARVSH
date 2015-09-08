"""
Author: Asish Panda
email: asishrocks95@gmail.com



The main module to parse user's input for an output. This is meant to be used directly by the
main module responisble for running the whole server. The user's input should be converted
to string and passed here.
"""

from parse import client_parse, general_parse
from KEYS import LOCATION, STATE, CLIENTS


class main:

    def __init__(self, string):
        #Best way would be to check each parse class
        #and give the most accurate result
            
        self.cp = client_parse(string)
        self.gp = general_parse(string)


    def do():
        value = self.cp.extract()
        if value:
            #do something with value

        else:
            #do something with gp parser
            #self.gp.extract()

            
if __name__ == '__main__':
    #get user's input
    #string = voice()
    #do = main(string)
