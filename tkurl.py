import tkinter as tk
from tkinter import X
from processingurls import ProcessingUrl


class URLForm1(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.font = ('Verdana', 10)
        self.geometry("600x150+150+150")
        self.entry = tk.Entry(self, width=85,  font=self.font, highlightbackground='beige')

        self.title("MY APPLICATION ")
        self.labelText = tk.StringVar()
        self.labelText.set(" URL analyser ")
        self.label = tk.Label(self, textvariable=self.labelText, height=3, bg='beige', fg="black")
        self.label.pack(fill=X)
        self.button = tk.Button(self, text="Submit", bg='beige', command=self.on_submit, height=1, width=10)
        self.button.pack(side=tk.BOTTOM)
        self.entry.pack(ipady=30)

    def on_submit(self):
        ProcessingUrl(self.entry.get()).asynchronous_requests()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "")
        return


