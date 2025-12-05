import tkinter as tk
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

# Function to change the label text
def change_text():
    label.config(text="Hello, Tkinter!")

# Create the main window (root window)
root = tk.Tk()

# Set the window title
root.title("Tkinter")

# Set the window icon (use a .ico file for Windows or .png for other platforms)
root.iconbitmap('shopify.png')  # Path to your icon file


# Create a label widget
label = tk.Label(root, text="Click the button!", font=("Arial", 14))
label.pack()  # Add the label to the window

# Create a button widget
button = tk.Button(root, text="Click Me", command=change_text)
button.pack()  # Add the button to the window


# Add the exit button to the window
button_exit = tk.Button(root, text="Click to exit", command=exit)
button_exit.pack()

def change_text():
    label.config(text="Exiting...")
    root.after(1000, exit)  # Wait 1 second before exiting  

# Run the Tkinter event loop (this keeps the window open)
root.mainloop()
