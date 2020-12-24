import spacy

nlp = spacy.load('en')
doc = nlp(u'TheShy and iG started the season with a strong showing in the LPL, placing 2nd in the LPL Spring Season '
          u'en route to their first domestic win in the organization\'s history. TheShy and iG win 3-0 against JD '
          u'Gaming in the finals, qualifying iG for the 2019 Mid-Season Invitational. TheShy was named the Finals MVP '
          u'of the 2019 Spring Split.')

for token in doc:
    print(token.text)
