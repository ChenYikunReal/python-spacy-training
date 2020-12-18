import spacy

nlp = spacy.load('en')
doc = nlp(u'I am learning how to build chat robots using python')
for token in doc:
    print(token.text, token.pos_)
