from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk


# Initial settings of my GUI (name,size, padding)
window = Tk()
window.title("Watermarking")
window.geometry("500x500")
window.config(padx=10, pady=10)


#function for opening images
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


def save_text():
    text = input.get()
    print(text)



#GUI elements (buttons, text entry, image placeholder
btn = tk.Button(window, text="Open Image", command=open_image)
btn.grid(row=0, column=0, padx=5, pady=5)

input = Entry(width=40)
input.insert(END, string="Enter your watermark text")
input.grid(row=0, column=1, padx=5, pady=5)

btn_submit = tk.Button(window, text="Submit", command=save_text)
btn_submit.grid(row=0, column=2, padx=5, pady=5)


label = tk.Label(window)
label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)


window.mainloop()