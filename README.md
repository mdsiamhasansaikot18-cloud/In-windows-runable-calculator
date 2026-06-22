# In-windows-runable-calculator

# GUI Calculator

A simple, clean desktop calculator built with Python and Tkinter. No external dependencies — just install Python and run.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey) ![License](https://img.shields.io/badge/License-MIT-green)

## Features

- Clean, dark-themed GUI
- Mouse and keyboard support
- Basic operations: addition, subtraction, multiplication, division
- Percentage (%) and sign toggle (±)
- Clear (C) and backspace (←)
- Decimal support
- Zero dependencies beyond Python itself (uses the built-in tkinter module)

## Requirements

- Python 3.7 or later (Tkinter ships with standard Python installs on Windows/macOS)
- No internet connection required to run
- No third-party packages required

## Installation

1. Install Python from https://www.python.org/downloads/ if you don't already have it.
   - On Windows, check "Add python.exe to PATH" during setup.
2. Clone or download this repository:

   git clone https://github.com/your-username/gui-calculator.git
   cd gui-calculator

## Usage

Run directly with Python:

   python calculator.py

Or on Windows, simply double-click calculator.py.

### Keyboard shortcuts

| Key             | Action                |
|-----------------|------------------------|
| 0-9, .          | Enter numbers/decimal  |
| + - * /         | Operators              |
| Enter or =      | Calculate result       |
| Backspace       | Delete last character  |
| Esc             | Clear                  |

## Building a standalone .exe (Windows)

To create a single executable that runs without Python installed:

   pip install pyinstaller
   pyinstaller --onefile --windowed calculator.py

The output will be at dist/calculator.exe — portable and shareable.

Note: PyInstaller must be run on the target OS. Build on Windows to get a Windows .exe.

## Project Structure

gui-calculator/
├── calculator.py     # Main application
├── README.md
└── LICENSE

## How It Works

The app uses Tkinter (Python's standard GUI toolkit) to render the window and buttons. Button presses and key events update an internal expression string, which is displayed live and evaluated safely (restricted to numeric/operator characters) when = is pressed.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License

This project is licensed under the MIT License — see the LICENSE file for details.
