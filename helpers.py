import re


def tokenize_query(query: str) -> list[str]:
    """
      Tokenizes a Boolean query string into a list of lowercase terms and operators.
    """
    return re.findall(r'\w+|AND|OR|NOT|\(|\)', query.lower())
