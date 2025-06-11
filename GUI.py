import tkinter as tk
from tkinter import messagebox


class GUI:
    """
    A class that represents the graphical user interface for the Boolean search engine.
    """
    def __init__(self, root, model, parser):
        """
        Initializes the GUI components and sets up the search interface.
        """
        self.model = model
        self.parser = parser

        root.title("Boolean Search Engine")
        root.geometry("600x400")

        self.label = tk.Label(root, text="Enter Boolean Query:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=80)
        self.entry.pack(pady=5)

        self.search_button = tk.Button(root, text="Search", command=self.search)
        self.search_button.pack(pady=5)

        self.info_label = tk.Label(root, text="The matching documents:")
        self.info_label.pack(pady=10)

        self.result_box = tk.Text(root, height=15, width=80)
        self.result_box.pack(pady=10)

        root.bind('<Return>', self.on_enter_key)

    def search(self):
        """
        Executes the Boolean query and displays the matching documents in the result box.
        """
        query = self.entry.get()
        try:
            result = self.parser.parse(query)
            self.result_box.delete(1.0, tk.END)

            if not result:
                self.result_box.insert(tk.END, "No documents match your query.")
            else:
                docs = self.model.get_doc_names(result)
                for doc in docs:
                    self.result_box.insert(tk.END, f"{doc}\n")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_enter_key(self, event=None):
        """Handle Enter key press"""
        self.search()
