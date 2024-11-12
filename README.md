# Python-FTPBruteForce
# FTP Brute Force Script

This Python script attempts to connect to an FTP server using a brute-force approach. It cycles through a list of potential passwords from a specified file, attempting to log in with a given username and IP address. If a password is correct, the script outputs the successful credentials.

## Requirements

- Python 3.x
- `ftplib` (This module is included in Python's standard library)

## Usage

1. **Specify Connection Details**:
   - **IP Address**: The IP address of the FTP server.
   - **Username**: The username to attempt to authenticate with.
   - **Password List File**: A text file containing a list of passwords, each on a new line.

2. **Run the Script**:
   Modify the connection details in the `ftpConnect()` function call at the end of the script.

   ```python
   ftpConnect('ip', 'YourUsername', 'path/to/password_list.txt')
