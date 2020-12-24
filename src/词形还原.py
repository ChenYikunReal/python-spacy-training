from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer

porter_stemmer = PorterStemmer()
snowball_stemmer = SnowballStemmer("english")

print(porter_stemmer.stem("fastest"))
print(snowball_stemmer.stem("fastest"))
