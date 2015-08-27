"""Main class to parse user's input and analyse the text
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
    p = parse("Would you turn on the light?")
    print(p.parse())

