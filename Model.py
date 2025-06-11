from preprocessing import process_document


class BooleanModel:
    """
    A class that represents a Boolean retrieval model for querying documents.
    """

    def __init__(self):
        """
        Initializes a new instance of the BooleanModel class with empty attributes.
        """
        self.inverted_index = {}
        self.all_documents = []
        self.frequencies = {}

    def add_document(self, doc: str, text: str):
        """Processes a given document and adds it into the Boolean model"""
        terms = process_document(text)

        self.all_documents.append(doc)
        doc_id = len(self.all_documents) - 1
        for term in terms:
            if term not in self.inverted_index:
                self.inverted_index[term] = set()
                self.frequencies[term] = 0
            self.frequencies[term] += 1
            self.inverted_index[term].add(doc_id)

    def get_doc_name(self, doc_id: int):
        """Returns the name of a document with given id."""
        return self.all_documents[doc_id]

    def get_documents(self, term: str) -> set[int]:
        """Returns set of document indices that contain given term."""
        return set(self.inverted_index.get(term, set()))

    def search_not(self, doc) -> set[int]:
        """Returns document ids that don't contain the term."""
        return set(range(len(self.all_documents))) - doc

    def get_doc_names(self, doc_ids: set[int]) -> list[str]:
        """"Returns documents in ascending order."""
        return [self.get_doc_name(doc_id) for doc_id in sorted(doc_ids)]
