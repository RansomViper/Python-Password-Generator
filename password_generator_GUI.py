import tkinter as tk
from tkinter import messagebox
import random
import pyttsx3
import string
import pyperclip
from datetime import datetime

# Function for text-to-speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to evaluate password strength
def evaluate_strength(password):
    length = len(password)
    if length < 8:
        return "Weak"
    elif length < 12:
        return "Medium"
    elif length < 16:
        return "Strong"
    else:
        return "Very Strong"

# Function to generate password
def generate_password():
    try:
        # Get user input from GUI
        total_length = int(length_entry.get())
        nr_uppercase = int(uppercase_entry.get())
        nr_lowercase = int(lowercase_entry.get())
        nr_symbols = int(symbols_entry.get())
        nr_numbers = int(numbers_entry.get())
        
        # Create character pools
        uppercase_letters = string.ascii_uppercase
        lowercase_letters = string.ascii_lowercase
        symbols = '!#$%&()*+'
        numbers = string.digits
        all_chars = uppercase_letters + lowercase_letters + symbols + numbers
        
        # Build the password
        password = []
        password += [random.choice(uppercase_letters) for _ in range(nr_uppercase)]
        password += [random.choice(lowercase_letters) for _ in range(nr_lowercase)]
        password += [random.choice(symbols) for _ in range(nr_symbols)]
        password += [random.choice(numbers) for _ in range(nr_numbers)]
        
        # Ensure total length matches the specified length, filling with random characters if necessary
        if len(password) < total_length:
            remaining_length = total_length - len(password)
            password += random.choices(all_chars, k=remaining_length)
        
        # Shuffle the password
        random.shuffle(password)
        
        # Convert the list to a string
        final_password = ''.join(password)
        
        # Display the password and password strength
        result_label.config(text=f"Generated Password: {final_password}")
        strength = evaluate_strength(final_password)
        strength_label.config(text=f"Password Strength: {strength}")
        
        # Save password to a file (append mode)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("password_history.txt", "a") as file:
            file.write(f"{timestamp} - {final_password}\n")
        
        # Speak the password
        speak(f"Your generated password is: {final_password}")
        
        # Copy password to clipboard
        pyperclip.copy(final_password)
        
        # Show success message
        messagebox.showinfo("Success", "Password generated, saved, and copied to clipboard!")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields!")

# Function to move focus to the next field
def move_focus(event, next_widget):
    next_widget.focus_set()

# Create main window
root = tk.Tk()
root.title("RansomViper Password Generator")

# GUI Title Banner
title_label = tk.Label(root, text="RansomViper Password Generator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Input fields
frame = tk.Frame(root)
frame.pack(pady=10)

length_label = tk.Label(frame, text="Total Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
length_entry = tk.Entry(frame)
length_entry.grid(row=0, column=1, padx=10, pady=5)

uppercase_label = tk.Label(frame, text="Number of Uppercase Letters:")
uppercase_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
uppercase_entry = tk.Entry(frame)
uppercase_entry.grid(row=1, column=1, padx=10, pady=5)

lowercase_label = tk.Label(frame, text="Number of Lowercase Letters:")
lowercase_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
lowercase_entry = tk.Entry(frame)
lowercase_entry.grid(row=2, column=1, padx=10, pady=5)

symbols_label = tk.Label(frame, text="Number of Symbols:")
symbols_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
symbols_entry = tk.Entry(frame)
symbols_entry.grid(row=3, column=1, padx=10, pady=5)

numbers_label = tk.Label(frame, text="Number of digits:")
numbers_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
numbers_entry = tk.Entry(frame)
numbers_entry.grid(row=4, column=1, padx=10, pady=5)

# Bind "Enter" key to move focus
length_entry.bind("<Return>", lambda event: move_focus(event, uppercase_entry))
uppercase_entry.bind("<Return>", lambda event: move_focus(event, lowercase_entry))
lowercase_entry.bind("<Return>", lambda event: move_focus(event, symbols_entry))
symbols_entry.bind("<Return>", lambda event: move_focus(event, numbers_entry))
numbers_entry.bind("<Return>", lambda event: generate_password())

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="blue", fg="white", font=("Helvetica", 12))
generate_button.pack(pady=10)

# Result and Strength Labels
result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="green")
result_label.pack(pady=10)

strength_label = tk.Label(root, text="", font=("Helvetica", 12), fg="orange")
strength_label.pack(pady=5)

# Run the application
root.mainloop()
