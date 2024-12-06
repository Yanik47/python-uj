import tkinter as tk
from PIL import Image, ImageTk
import random

def roll_dice():
    result = random.randint(1, 6)
    label_result.config(image=dice_images[result - 1])

# Create the main window
root = tk.Tk()
root.title("Dice Roll Simulation with Images")
root.geometry("800x600")

# Load images for each dice side
image_paths = [
    "dice-1.png",  # Provide correct paths to the images
    "dice-2.png",
    "dice-3.png",
    "dice-4.png",
    "dice-5.png",
    "dice-6.png"
]

# Load images and store them in a list
dice_images = [ImageTk.PhotoImage(Image.open(img)) for img in image_paths]

# Instruction label
label_instruction = tk.Label(root, text="Click the button to roll the dice.", font=("Arial", 12))
label_instruction.pack(pady=10)

# Button to roll the dice
button_roll = tk.Button(root, text="Roll the Dice", command=roll_dice, font=("Arial", 12))
button_roll.pack(pady=10)

# Label displaying the result (dice image)
label_result = tk.Label(root, image=dice_images[0])  # Default to image 1
label_result.pack(pady=10)

# Run the application
root.mainloop()
