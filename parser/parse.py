"""
Author: Asish Panda
email: asishrocks95@gmail.com

class to parse user's input and analyse the text. Uses a simple grammar rule to detect
any number of determiners or preposition follwed by a single noun(fan) or adjective
(light). The noun or adjective will help to identify the client, the preposition will
help to identify the state.


#Machine learning approach to parse data using Unigram algorithm. Cannot be used now due to lack
#of good corpus as well as naivity of the idea.

class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t,c) for w, t ,c in nltk.chunk.tree2conlltags(sent)]for sent in train_sents]
        self.tagger = nltk.UnigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word, pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word, pos), chunktag) in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)
        #return conlltags

if __name__ == '__main__':
    corpus = nltk.corpus.reader.ConllChunkCorpusReader('.', r'.*\.txt', ("NP"))
    p = UnigramChunker(corpus.chunked_sents())
    x = "turn on the fan in the bedroom"
    y = nltk.word_tokenize(x)
    y = nltk.pos_tag(y)
    print(p.parse(y))
"""

import nltk
from KEYS import CLIENTS, LOCATIONS, STATES


class client_parse:

    def __init__(self, text):
        self.token = nltk.word_tokenize(text)
        self.tags = nltk.pos_tag(self.token)

        #process chunk data using the parser(grammar rule)
        #processing it here to save time

        self.chunk = nltk.RegexpParser(self.grammar()).parse(self.tags)


    def grammar(self):
        return r"""
               NP : {<IN|RP|DT>*<NN|NNP|JJ|JJR|VB>}
               """

    def parse(self):
        return self.chunk

    def extract(self):
        """
           This function extracts any relevant information related to clients of the house.
           For eg, "Switch on the fan", "Decrease AC temperature" and returns the list of 
           related information in a tuple of three lists. If no useful information is extracted
           it is handled accordingly.

        """

        info = []
        #store NP in a list with tags of words
        for chunked in self.chunk:
            if type(chunked) != tuple:
                info.extend(chunked)

        state = []
        client = []
        location = []
        for word_tag in info:
            print(word_tag)

            if word_tag[0] in STATES:
                state.append(word_tag[0])

            if word_tag[0] in CLIENTS:
                client.append(word_tag[0])

            if word_tag[0] in LOCATIONS:
                location.append(word_tag[0])

        # check if sentence is 
        # 1) ambigious. 
        # see if state, location and client length doesn't match. 
        # In that case user has provided us with less input. 
        # An error message is returned
        # 2) if it belongs to some other parser
        # in this case, no NP chunk exists and therefore the sentence should be parsed with
        # a different parser.

        print(state, client, location)

        if len(state) != len(client) or len(location) != len(state) or len(location) != len(client):
            raise ValueError("The sentence is ambigious. Please provide more details")


        #we don't check length of state as it can be(very frequently) used in other queries
        if len(client) == 0 and len(location) == 0:
            return False

        #else return information extracted
        return (state, client, location)


class query_parse:

    """This class checks whether the query is within the capabilties of the system 
       to give a feedback. If no, the query should be forwarded to internet and
       more advanced system, such as wolframalpha
    """

    def __init__(self, text):
        return False
    


if __name__ == '__main__':
    x = "lower AC temperature of the kitchen"
    p = client_parse(x)
    print(p.chunk)
    print(p.extract())
