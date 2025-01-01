# Password Manager Application

This project is a **Password Manager** built using Python and the `tkinter` library. The application provides functionalities to generate strong passwords, save them securely, and retrieve saved credentials for different websites.

---

## Features

1. **Password Generator**
   - Generates strong and random passwords containing letters, numbers, and symbols.
   - Passwords are shuffled for additional security.

2. **Save Passwords**
   - Saves website, email/username, and password details to a local `data.txt` file.
   - Ensures no fields are left empty before saving.
   - Prompts user confirmation before adding new entries.

3. **Search Functionality**
   - Quickly retrieves saved credentials for a specified website.
   - Notifies the user if the website is not found.

4. **User-Friendly Interface**
   - Built using the `tkinter` library with an intuitive layout for easy use.
   - Displays a logo image at the top of the application window.

---

## Requirements

- Python 3.x
- `tkinter` (comes pre-installed with Python)
- A `logo.png` file for the application logo.

---

## How to Run

1. Clone or download this repository.
2. Ensure that `logo.png` is in the same directory as the script.
3. Run the Python script using:
   ```bash
   python password_manager.py
