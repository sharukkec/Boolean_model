import os
import pickle

from Model import BooleanModel

MODEL_PATH = "model.pkl"
FILEPATH = "Documents"


class BooleanModelWrapper:
    """
    Wrapper helper class for BooleanModel.
    Loads and saves the model for better performance
    """

    def __init__(self):
        self.model = BooleanModel()

    def save(self, path=MODEL_PATH):
        with open(path, "wb") as f:
            pickle.dump(self.model, f)

    @staticmethod
    def load(path=MODEL_PATH):
        with open(path, "rb") as f:
            wrapper = BooleanModelWrapper()
            wrapper.model = pickle.load(f)
            return wrapper


def initialize_model_from_directory() -> BooleanModelWrapper:
    """
    Process documents from FILEPATH and add them into a model.
    uses BooleanModelWrapper to save the model and load it for further runs

    """
    current_docs = sorted(os.listdir(FILEPATH))

    if os.path.exists(MODEL_PATH):
        saved_model = BooleanModelWrapper.load()
        saved_docs = saved_model.model.all_documents

        if set(saved_docs) == set(current_docs):
            print("Loaded model (exact match)")
            return saved_model

        elif all(doc in current_docs for doc in saved_docs):
            print("Updating model with new documents")
            new_docs = [doc for doc in current_docs if doc not in saved_docs]
            for doc in new_docs:
                with open(os.path.join(FILEPATH, doc), "r", encoding="utf-8") as f:
                    saved_model.model.add_document(doc, f.read())
            saved_model.model.all_documents.extend(new_docs)
            saved_model.save()
            return saved_model

        else:
            print("Documents changed significantly. Rebuilding model.")

    # Build model from scratch
    model_wrapper = BooleanModelWrapper()
    for doc in current_docs:
        with open(os.path.join(FILEPATH, doc), "r", encoding="utf-8") as f:
            model_wrapper.model.add_document(doc, f.read())
    model_wrapper.model.all_documents = current_docs
    model_wrapper.save()
    return model_wrapper
