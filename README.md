# RansomViper Password Generator

## Description
RansomViper is a versatile password generator that offers both Command Line Interface (CLI) and Graphical User Interface (GUI) modes. With text-to-speech functionality and password strength evaluation, RansomViper provides a user-friendly experience for creating secure passwords. The program allows users to customize passwords by specifying the number of uppercase letters, lowercase letters, symbols, and digits, and includes features like password saving and clipboard copying.

---

## Features
### CLI Version:
- Generate passwords with a text-based interface.
- Text-to-speech functionality for accessibility.
- Save generated passwords to a file (`generated_password.txt`).

### GUI Version:
- Interactive graphical interface using `Tkinter`.
- Fields to specify the total password length and character distribution.
- Password strength evaluation (Weak, Medium, Strong, Very Strong).
- Automatically saves passwords with timestamps in `password_history.txt`.
- Copies the generated password to the clipboard.
- Displays success messages and handles input errors gracefully.

---

## Requirements
- Python 3.6 or higher
- Required libraries (install via `requirements.txt`):
  - `pyttsx3`: Text-to-speech functionality
  - `pyperclip`: Clipboard support
  - `tkinter`: For the GUI (comes pre-installed with Python)
  - `string`: Character manipulation (standard library)

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ransomviper-password-generator.git
   cd ransomviper-password-generator

## Install the required dependencies:

Bash
pip install -r requirements.txt



## How to Run

### CLI Version:

Run the CLI version with

bash

python ransomviper_cli.py

### GUI Version
Run the GUI version with:

bash

python ransomviper_gui.py


### How to Use (GUI Version)

1. Enter the total password length.
2. Specify the number of uppercase letters, lowercase letters, symbols, and digits.
3. Click the "Generate Password" button.
4. The generated password and its strength will appear on the screen.
5. The password will be:
Spoken using text-to-speech.
6. Copied to the clipboard.
7. Saved to password_history.txt with a timestamp.


## Example (GUI)
After filling in the details:

- Input: Total Length: 12, Uppercase: 3, Lowercase: 4, Symbols: 2, Digits: 3.
- Output:
- Generated Password: @Aa1Bb2Cc3D*
- Strength: Strong
- Saved as: 2024-12-31 12:00:00 - @Aa1Bb2Cc3D* in password_history.txt.

## Contributions
Feel free to contribute by submitting issues or pull requests.

## License
This project is licensed under the MIT License.

