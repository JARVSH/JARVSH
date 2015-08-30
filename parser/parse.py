"""
Author: Asish Panda
email: asishrocks95@gmail.com

class to parse user's input and analyse the text. Uses a simple grammar rule to detect
any number of determiners or preposition follwed by a single noun(fan) or adjective
(light). The noun or adjective will help to identify the client, the preposition will
help to identify the state.
"""
import nltk

class parse:

    def __init__(self, text):
        self.token = nltk.word_tokenize(text)
        self.tags = nltk.pos_tag(self.token)

    def grammar(self):
        return r"""
               NP : {<IN|DT>*<NN|JJ>}
               """

    def parse(self):
        return nltk.RegexpParser(self.grammar()).parse(self.tags)


if __name__ == '__main__':
    raise ValueError("Not meant to use directly")
