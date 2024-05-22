## Description

The Auto-Typer script simulates random typing in a Notepad window. This script opens a new instance of Notepad, types random characters at random intervals, and provides a GUI with an exit button to stop the typing.

## Features

- Opens a new Notepad instance
- Types random characters at random intervals to simulate human typing
- Provides a GUI with an exit button to stop the typing

## Requirements

- Python 3.12
- The following Python packages:
  - `pyautogui`
  - `pygetwindow`
  - `tkinter`

## Installation

1. **Clone the Repository:**

    ```sh
    git clone <repository-url>
    cd auto-typer
    ```

2. **Install the Required Packages:**

    ```sh
    pip install pyautogui pygetwindow psutil
    ```

## Usage

1. **Run the Script:**

    ```sh
    python main.py
    ```

2. **Create an Executable (Optional):**

    If you want to create a standalone executable, use `PyInstaller`. First, install `PyInstaller` if you haven't already:

    ```sh
    pip install pyinstaller
    ```

    Then, navigate to the script directory and run `PyInstaller`:

    ```sh
    cd path/to/auto-typer
    pyinstaller --onefile main.py
    ```

    This will create an executable in the `dist` directory.

3. **Run the Executable:**

    Navigate to the `dist` directory and run the executable:

    ```sh
    cd dist
    ./main.exe
    ```

## How It Works

1. The script opens a new instance of Notepad.
2. After a brief delay to ensure Notepad is open, it positions and resizes the Notepad window.
3. The script then starts typing random characters at random intervals into the Notepad window.
4. A GUI window is provided with an "Exit" button to stop the typing and close the script.
