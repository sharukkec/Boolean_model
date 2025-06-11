import tkinter as tk

from GUI import GUI
from QueryParser import BooleanQueryParser
from wrapper import initialize_model_from_directory
import time


# just for testing:
# bm.add_document("doc1", "apple orange")
# bm.add_document("doc2", "cucumber potato orange")
# bm.add_document("doc3", "apple banana")
# bm.add_document("doc4", "banana orange")
# bm.add_document("doc5", "grape apple")
# bm.add_document("doc6", "cucumber carrot apple")
# bm.add_document("doc7", "apple carrot banana")
# bm.add_document("doc8", "grape")
# bm.add_document("doc9", "potato carrot")
# bm.add_document("doc10", "carrot orange apple")


def main():
    # Initialize model
    model_wrapper = initialize_model_from_directory()
    bm = model_wrapper.model

    # Initialize the query parser
    parser = BooleanQueryParser(bm)
    # Set up the GUI
    root = tk.Tk()
    app = GUI(root, bm, parser)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Doba běhu: {end - start:.2f} sekund")
