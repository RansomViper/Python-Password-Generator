import pyttsx3
import random

# ASCII Banner
banner = """
####################################################
#                                                  #
#       RANSOMVIPER PASSWORD GENERATOR             #
#                                                  #
####################################################
"""
print(banner)

# Initialize pyttsx3 engine for text-to-speech
engine = pyttsx3.init()

# Function to make the program speak the given text
def speak(text):
    print(text)  # Print text for reference in the console
    engine.say(text)  # Queue the text for text-to-speech
    engine.runAndWait()  # Wait until speaking is finished

# List and set voices for debugging (optional)
voices = engine.getProperty('voices')
for index, voice in enumerate(voices):
    print(f"{index}: {voice.name}")  # Display available voices
engine.setProperty('voice', voices[0].id)  # Explicitly set the first available voice

# Lists of characters for generating passwords
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Speak a welcome message
speak("Welcome to RansomViper Password Generator!")

# Get user input for the number of letters
speak("How many letters would you like in your password?")
nr_letters = int(input("Enter the Letters you want?\n"))

# Get user input for the number of symbols
speak("How many symbols would you like?") 
nr_symbols = int(input("Enter the symbols you want?\n"))

# Get user input for the number of numbers
speak("How many numbers would you like?")
nr_numbers = int(input("Enter the Numbers you like?\n"))

# Speak a summary of the user's choices
speak(f"You want a password with {nr_letters} letters, {nr_symbols} symbols, and {nr_numbers} numbers.")

# Initialize an empty password
password = ""

# Add random letters to the password
for char in range(1, nr_letters + 1): 
    password += random.choice(letters)

# Add random symbols to the password
for symb in range(1, nr_symbols + 1):
    password += random.choice(symbols)

# Add random numbers to the password
for number in range(1, nr_numbers + 1): 
    password += random.choice(numbers)

# Convert the password string into a list for shuffling
password_split = list(password)
random.shuffle(password_split)  # Shuffle the characters
new_password = ''.join(password_split)  # Join the shuffled characters back into a string

# Speak and display the generated password
speak(f"Here is your new password: {new_password}")
print(f"Generated Password: {new_password}")

# Function to save the password to a text file
def save_password(password):
    with open("generated_password.txt", "w") as file:  # Open a file in write mode
        file.write(f"Generated Password: {password}\n")  # Write the password to the file
    speak("Your password has been saved to 'generated_password.txt'.")

# Call the function to save the password
save_password(new_password)

# Speak a thank-you message
speak("Thank you for using RansomViper Password Generator!")
