"""
Image Colorizer: Back to Life

By Ralph Cajipe
CS50's Introduction to Programming with Python
Final Project
2022
"""

from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import *

import torch

if not torch.cuda.is_available():
    print('GPU not available.')

import tkinter as tk
from tkinter import filedialog

import customtkinter as ctk
from PIL import ImageTk

import warnings

# Setting the device to GPU1 (in my case). Set it according to your device.
# If you have multiple GPUs, you can change the device to GPU2, GPU3, etc.
device.set(device=DeviceId.GPU1)

# Ignoring the warnings that are being displayed in the console.
warnings.filterwarnings("ignore")

# Initialize DeOldify Artistic Model
colorizer = get_image_colorizer(artistic=True)


def browse_image():
    """
    It opens a file dialog box and returns the path of the selected file.
    """
    file_path = filedialog.askopenfilename()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)


def colorize_image():
    """
    It takes the file path from the input entry, colorizes the image,
    and displays the result.
    """
    # Get the file path
    file_path = input_entry.get()

    # Colorize the image
    result_path = colorizer.plot_transformed_image(
        path=file_path, render_factor=25, compare=True
    )

    app.update()

    # Display the image
    image = Image.open(result_path)
    # Set resize to 256x256 with antialiasing
    image = image.resize((256, 256), Image.ANTIALIAS)
    # image = image.resize((int(image.size[0] / 1), int(image.size[1] / 1)),
    # Image.ANTIALIAS) image = image.resize((256, 256), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    image_label.configure(image=photo)
    image_label.image = photo


def save_image():
    """
    It takes the file path from the input entry, colorizes the image,
    and saves the result to a file.
    """
    file_path = input_entry.get()

    # Colorize the image
    result_path = colorizer.plot_transformed_image(
        path=file_path, render_factor=25, compare=True
    )

    # Save the image
    file_name = filedialog.asksaveasfilename(
        defaultextension=".jpg", filetypes=[("JPG", "*.jpg"), ("PNG", "*.png")]
    )
    image = Image.open(result_path)
    image.save(file_name)


# Create the app
app = ctk.CTk()

# Set a geometry that is regular for all screens
app.geometry("600x400")

# app.geometry("400x240")
app.title("Image Colorizer")

# Set the title icon
app.iconbitmap("assets/logo.ico")

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Create the widgets
input_label = ctk.CTkLabel(app, text="File Path")
input_entry = ctk.CTkEntry(app, width=350)
input_button = ctk.CTkButton(master=app, text="2. Colorize",
                             command=colorize_image)
image_label = ctk.CTkLabel(app, text="Image will be displayed here")
save_button = ctk.CTkButton(master=app, text="3. Save", command=save_image)

browse_button = ctk.CTkButton(master=app, text="1. Browse",
                              command=browse_image)
browse_button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Display the widgets
browse_button.pack(pady=5)
input_label.pack(pady=5)
input_entry.pack(pady=5)
input_button.pack(pady=5)
image_label.pack(pady=5)
save_button.pack(pady=5)


def main():
    """
    `main()` is a function that runs the mainloop of the `app` object
    """
    app.mainloop()


# Run the app
if __name__ == "__main__":
    main()
