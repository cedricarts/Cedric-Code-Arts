# Password Generator By Cedric Arts

## Overview

This is a desktop-based password generator built using Python and Tkinter. The application allows users to generate customizable passwords, copy them to the clipboard, and store them locally for reference.

The project is designed as a practical implementation of GUI development, file handling, and basic security concepts.

## Features

* Custom password length input
* Selectable character sets:

  * Alphabetic characters (uppercase and lowercase)
  * Numeric digits
  * Special symbols
* Random password generation
* Clipboard copy functionality
* Persistent password storage using JSON
* Scrollable password history view

## Application Preview

The application provides a simple graphical interface with:

* Input field for password length
* Checkbox options for character types
* Generate and copy buttons
* Display area for generated password
* Password history panel

## Technologies Used

* Python 3
* Tkinter (GUI framework)
* JSON (data storage)
* OS module (file management)
* Random module (password generation)

## Project Structure

```
password-generator/
│
├── main.py
├── passwords.json (auto-generated)
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/password-generator.git
cd password-generator
```

### 2. Verify Python installation

```
python --version
```

### 3. Run the application

```
python main.py
```

## Usage

1. Enter the desired password length
2. Select at least one character type:

   * Characters
   * Digits
   * Symbols
3. Click "Generate"
4. Copy the password if needed
5. View saved passwords in the history panel

## Data Storage

* Passwords are stored locally in:

  ```
  passwords.json
  ```
* Format:

  ```
  ["password1", "password2", "password3"]
  ```
* The file is created automatically if it does not exist

## Known Issues

* No validation for empty character selection (can cause runtime error)
* No validation for invalid or zero password length
* Passwords are stored in plain text
* Character set is manually defined and slightly incomplete
* UI is not responsive to scaling


## Security Considerations

This application is intended for educational and low-risk use cases.

Important limitations:

* Passwords are not encrypted
* Clipboard data is not protected
* No secure random generation (uses `random` instead of `secrets`)

For real-world usage:

* Replace `random` with `secrets`
* Encrypt stored passwords
* Avoid storing sensitive credentials locally

## Suggested Improvements

### Core Improvements

* Input validation (length > 0, at least one option selected)
* Use `secrets.choice()` for cryptographic randomness
* Add error handling with user feedback (messagebox)

### Security Enhancements

* Encrypt stored passwords (e.g., Fernet)
* Add optional master password protection
* Auto-clear clipboard after a timeout

### UI/UX Improvements

* Improve layout and spacing
* Add password strength indicator
* Add "Clear History" button
* Add export functionality (CSV or TXT)

### Code Improvements

* Refactor character pools into constants
* Separate logic from UI (modular design)
* Add comments and docstrings

## Example Improvement (Secure Random)

Replace:

```python
import random
random.choice(pass1)
```

With:

```python
import secrets
secrets.choice(pass1)
```

## Author

Njabulo Cedric Mnisi (Cedric Arts)
Founder of Horizon Synergy
Developer focused on systems, tools, and scalable digital infrastructure


## License

This project is open-source and available for educational use. Modify and distribute as needed.
