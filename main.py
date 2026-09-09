from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk

window = Tk()
window.title("Watermarking")
window.geometry("500x500")
window.config(padx=10, pady=10)

def open_image():
    file = filedialog.askopenfilename(
        title = "Select file",
        filetypes = [("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if not file:
        return

    img = Image.open(file)
    img = img.resize((400, 400))
    tk_img = ImageTk.PhotoImage(img)

    label.config(image=tk_img)
    label.image = tk_img

label = tk.Label(window)
label.pack()

btn = tk.Button(window, text="Open Image", command=open_image)
btn.pack()


window.mainloop()