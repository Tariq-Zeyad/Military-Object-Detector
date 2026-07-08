import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk

from model import ImageClassifier


class DetectorUI:


    def __init__(self):

        self.classifier = ImageClassifier()

        self.window = tk.Tk()

        self.window.title(
            "Military Detector"
        )

        self.window.geometry(
            "700x700"
        )


        self.image_label = tk.Label(
            self.window
        )

        self.image_label.pack(
            pady=20
        )


        self.result = tk.Label(
            self.window,
            text="Select Image",
            font=("Arial", 22)
        )

        self.result.pack()



        button = tk.Button(
            self.window,
            text="Open Image",
            font=("Arial", 16),
            command=self.select_image
        )

        button.pack(
            pady=20
        )



    def select_image(self):

        path = filedialog.askopenfilename(
            filetypes=[
                ("Images",
                 "*.jpg *.png *.jpeg")
            ]
        )


        if not path:
            return


        prediction, image = self.classifier.predict(path)


        image.thumbnail(
            (500,500)
        )

        photo = ImageTk.PhotoImage(
            image
        )


        self.image_label.configure(
            image=photo
        )

        self.image_label.image = photo


        self.result.config(
            text=prediction
        )



    def run(self):

        self.window.mainloop()