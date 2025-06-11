from Model import BooleanModel
from helpers import tokenize_query


class BooleanQueryParser:
    """
    This class parses Boolean queries with AND, OR, and NOT operators.
    """

    def __init__(self, model: BooleanModel):
        """
        Initialize the parser with a given BooleanModel.
        """
        self.model = model
        self.tokens = []
        self.pos = 0

    def parse(self, query: str) -> set[int]:
        """
        Main entry point to parse a query string.
        Resets the token list and starts the expression parsing.
        """
        self.tokens = tokenize_query(query)
        self.pos = 0
        return self.expr()

    def expr(self) -> set[int]:
        """
        Parses a Boolean expression involving 'and' and 'or'.
        """
        result = self.term()

        while self.pos < len(self.tokens) and self.tokens[self.pos] in {"and", "or"}:
            op = self.tokens[self.pos]
            self.pos += 1
            right = self.term()
            if op == "and":
                result &= right
            elif op == "or":
                result |= right

        return result

    def term(self) -> set[int]:
        """
        Handles a term or a negation (not).
        """
        if self.pos >= len(self.tokens):
            return set()

        token = self.tokens[self.pos]

        if token == "not":
            self.pos += 1
            return self.model.search_not(self.atom())
        else:
            return self.atom()

    def atom(self) -> set[int]:
        """
        Parses individual terms or grouped expressions inside parentheses.
        """
        token = self.tokens[self.pos]

        if token == "(":
            self.pos += 1
            result = self.expr()
            if self.tokens[self.pos] != ")":
                raise ValueError("Expected ')'")
            self.pos += 1
            return result
        else:
            self.pos += 1
            return self.model.get_documents(token)
