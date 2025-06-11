import re
import string

import nltk
from nltk.corpus import stopwords


# download if isn't downloaded
# nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
stemmer = nltk.SnowballStemmer("english", ignore_stopwords=True)
stem_cache = {}


def process_document(document: str) -> set:
    """
    Processes a given document, removes punctuation and splits document into token words. Also uses the SnowballStemmer
    """
    document = document.lower()

    punctuation = string.punctuation.replace("'", "") + "“”_—‘"
    document = re.sub(f"[{punctuation}]", " ", document)

    tokens = document.split()
    tokens_filtered = set()

    for token in tokens:
        # for simplicity of searching, ignores apostrophes in words
        if "'" in token:
            token = token.split("'")[0]

        if token.isalpha() and token not in stop_words:
            # use stem cache for faster processing
            if token not in stem_cache:
                stem_cache[token] = stemmer.stem(token)
            tokens_filtered.add(stem_cache[token])
    return tokens_filtered
