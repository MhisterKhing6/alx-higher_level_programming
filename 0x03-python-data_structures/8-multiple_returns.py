#!/usr/bin/python3
def multiple_returns(sentence):

    if len(sentence) == 0:
        retu = (None,)
        return retu
    else:
        retu = (sentence[0], len(sentence))
        return retu
